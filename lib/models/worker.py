from models.__init__ import create_conn

class Worker:

    all={}

    def __init__(self, name, role, shift_id, restaurant_id, id_ = None):
        self.name = name
        self.role = role
        self.shift_id = shift_id
        self.restaurant_id = restaurant_id
        self.id_ = id_
        type(self).create_table()

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS workers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            role TEXT NOT NULL,
            shift_id INTEGER NOT NULL,
            restaurant_id INTEGER NOT NULL,
            FOREIGN KEY (shift_id) REFERENCES shifts(id),
            FOREIGN KEY (restaurant_id) REFERENCES restaurants(id)
            )
        """
        with create_conn() as CONN:
            CURSOR = CONN.cursor()
            CURSOR.execute(sql)
        
    @classmethod
    def drop_table(cls):
        sql = """
        DROP TABLE IF EXISTS workers
        """
        with create_conn() as CONN:
            CURSOR = CONN.cursor()
            CURSOR.execute(sql)

    @classmethod
    def create(cls, name, role, shift_id, restaurant_id):
        worker = cls(name, role, shift_id, restaurant_id)
        worker.save()
        return worker

    @classmethod
    def instance_from_db(cls, row):
        worker = cls.all.get(row[0])

        if worker:
            worker.name = row[1]
            worker.role = row[2]
            worker.shift_id = row[3]
            worker.restaurant_id = row[4]
        else:
            worker = cls(row[1], row[2], row[3], row[4], row[0])
            cls.all.update({row[0] : worker})
        return worker
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM workers
        """
        with create_conn() as CONN:
            CURSOR = CONN.cursor()
            workers = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(worker) for worker in workers]

    @classmethod
    def find_by_id(cls, id_):
        sql = """
            SELECT *
            FROM workers
            WHERE id = ?
        """
        with create_conn() as CONN:
            CURSOR = CONN.cursor()
            worker = CURSOR.execute(sql, (id_,)).fetchone()
        return cls.instance_from_db(worker) if worker else None

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM workers
            WHERE name is ?
        """
        with create_conn() as CONN:
            CURSOR = CONN.cursor()
            workers = CURSOR.execute(sql, (name,)).fetchall()
        
        return [cls.instance_from_db(worker) for worker in workers] if workers else None

    def save(self):
        sql = """
        INSERT INTO workers (name, role, shift_id, restaurant_id)
        VALUES (?, ?, ?, ?) 
        """
        with create_conn() as CONN:
            CURSOR = CONN.cursor()
            CURSOR.execute(sql, (self.name, self.role, self.shift_id, self.restaurant_id))
            self.id_ = CURSOR.lastrowid

        type(self).all.update({self.id_: self})

    def update(self):
        sql = """
            UPDATE workers
            SET name = ?, role = ?, shift_id = ?, restaurant_id =?
            WHERE id = ?
        """
        with create_conn() as CONN:
            CURSOR = CONN.cursor()
            CURSOR.execute(sql, (self.name, self.role, self.shift_id, self.restaurant_id, self.id_))

    def delete(self):
        sql = """
            DELETE FROM workers
            WHERE id = ?
        """
        with create_conn() as CONN:
            CURSOR = CONN.cursor()
            CURSOR.execute(sql, (self.id_,))

    def shifts(self):
        from models.shift import Shift
        sql = """
            SELECT *
            FROM shifts
            WHERE shifts.id = ?
        """
        with create_conn() as CONN:
            CURSOR = CONN.cursor()
            shifts = CURSOR.execute(sql, (self.shift_id,)).fetchall()

        return [Shift.instance_from_db(shift) for shift in shifts] if shifts else None

    def __repr__(self):
        return f"Name = {self.name}, Role = {self.role}, Shift ID = {self.shift_id}, Restaurant ID = {self.restaurant_id}, Id = {self.id_}"
