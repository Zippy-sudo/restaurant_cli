from models.__init__ import create_conn

class Restaurant:

    all = {}
    
    def __init__(self, name, location, id_ = None):
        self.name = name
        self.location = location
        self.id_ = id_
        type(self).create_table()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if len(name) > 0 and isinstance(name, str):
            self._name = name
        else:
            raise ValueError (
                "Name must be a non-empty string"
            )
        
    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        if len(location) > 0:
            self._location = location
        else:
            raise ValueError (
                "Location must be a non-empty string"
            )
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS restaurants (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            location TEXT NOT NULL
            )
        """
        with create_conn() as CONN:
            CURSOR = CONN.cursor()
            CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS restaurants
        """
        with create_conn() as CONN:
            CURSOR = CONN.cursor()
            CURSOR.execute(sql)

    @classmethod
    def create(cls, name, location):
        restaurant = cls(name, location)
        restaurant.save()
        return restaurant

    @classmethod
    def instance_from_db(cls, row):
        restaurant = cls.all.get(row[0])
        if restaurant:
            restaurant.name = row[1]
            restaurant.location = row[2]
        else:
            restaurant = cls(row[1], row[2], row[0])
            cls.all.update({row[0] : restaurant})
        return restaurant

    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM restaurants
        """
        with create_conn() as CONN:
            CURSOR = CONN.cursor()
            restaurants = CURSOR.execute(sql).fetchall()
        
        return [cls.instance_from_db(restaurant) for restaurant in restaurants]

    @classmethod
    def find_by_id(cls, id_):
        sql = """
            SELECT *
            FROM restaurants
            WHERE id = ?
        """
        with create_conn() as CONN:
            CURSOR = CONN.cursor()
            restaurant = CURSOR.execute(sql, (id_,)).fetchone()
        
        return cls.instance_from_db(restaurant) if restaurant else None

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM restaurants
            WHERE name is ?
        """
        with create_conn() as CONN:
            CURSOR = CONN.cursor()
            restaurants = CURSOR.execute(sql, (name,)).fetchall()
        
        return [cls.instance_from_db(restaurant) for restaurant in restaurants] if restaurants else None

    def save(self):
        sql = """
            INSERT INTO restaurants(name, location)
            VALUES (?, ?)
        """
        with create_conn() as CONN:
            CURSOR = CONN.cursor()
            CURSOR.execute(sql, (self.name, self.location))
            self.id_ = CURSOR.lastrowid

        type(self).all.update({self.id_: self})

    def update(self):
        sql = """
            UPDATE restaurants
            SET name = ?, location = ?
            WHERE id = ? 
        """
        with create_conn() as CONN:
            CURSOR = CONN.cursor()
            CURSOR.execute(sql, (self.name, self.location, self.id_))

    def delete(self):
        sql = """
            DELETE FROM restaurants
            WHERE id = ? 
        """
        with create_conn() as CONN:
            CURSOR = CONN.cursor()
            CURSOR.execute(sql, (self.id_,))
        del type(self).all[self.id_]
        self.id_ = None

    def shifts(self):
        from models.shift import Shift
        sql = """
            SELECT *
            FROM shifts
            WHERE shifts.restaurant_id = ?
        """
        with create_conn() as CONN:
            CURSOR = CONN.cursor()
            shifts = CURSOR.execute(sql, (self.id_,)).fetchall()
        
        return [Shift.instance_from_db(shift) for shift in shifts] if shifts else None

    def workers(self):
        from models.worker import Worker
        sql = """
            SELECT *
            FROM workers
            WHERE workers.restaurant_id = ?
        """
        with create_conn() as CONN:
            CURSOR = CONN.cursor()
            workers = CURSOR.execute(sql, (self.id_,)).fetchall()

        return [Worker.instance_from_db(worker) for worker in workers] if workers else None

    def __repr__(self):
        return f"Name = {self.name}, Location = {self.location}, Id = {self.id_}"
    
