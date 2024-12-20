from models.__init__ import create_conn

class Shift:

    all = {}

    def __init__(self,time_in, time_out, restaurant_id, id_ = None):
        self.time_in = time_in
        self.time_out = time_out
        self.restaurant_id = restaurant_id
        self.id_ = id_
        type(self).create_table()

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS shifts (
            id INTEGER PRIMARY KEY,
            time_in INTEGER,
            time_out INTEGER,
            restaurant_id INTEGER,
            FOREIGN KEY (restaurant_id) REFERENCES restaurants(id)
            )
        """
        with create_conn() as CONN:
            CURSOR = CONN.cursor()
            CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS shifts
        """
        with create_conn() as CONN:
            CURSOR = CONN.cursor()
            CURSOR.execute(sql)

    @classmethod
    def create(cls, time_in, time_out, restaurant_id):
        shift = cls(time_in, time_out, restaurant_id)
        shift.save()
        return shift

    @classmethod
    def instance_from_db(cls, row):
        shift = cls.all.get(row[0])
        if shift:
            shift.time_in = row[1]
            shift.time_out = row[2]
            shift.restaurant_id = row[3]
        else:
            shift = cls(row[1], row[2], row[3], row[0])
            cls.all.update({row[0] : shift})
        return shift
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM shifts
        """
        with create_conn() as CONN:
            CURSOR = CONN.cursor()
            shifts = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(shift) for shift in shifts ] if shifts else None

    @classmethod
    def find_by_id(cls, id_):
        sql = """
            SELECT * 
            FROM shifts
            WHERE id = ? 
        """
        with create_conn() as CONN:
            CURSOR = CONN.cursor()
            shift = CURSOR.execute(sql, (id_,)).fetchone()
        return cls.instance_from_db(shift) if shift else None

    def save(self):
        sql = """
            INSERT INTO shifts( time_in, time_out, restaurant_id)
            VALUES ( ?, ?, ?)
        """
        with create_conn() as CONN:
            CURSOR = CONN.cursor()
            CURSOR.execute(sql, (self.time_in, self.time_out, self.restaurant_id))
            CONN.commit()
            self.id_ = CURSOR.lastrowid

    def update(self):
        sql = """
            UPDATE shifts
            SET time_in = ?, time_out = ?, restaurant_id = ?
            WHERE id = ?
        """
        with create_conn() as CONN:
            CURSOR = CONN.cursor()
            CURSOR.execute(sql, (self.time_in, self.time_out, self.restaurant_id, self.id_))
    
    def delete(self):
        sql = """
            DELETE FROM shifts
            WHERE id = ?
        """
        with create_conn() as CONN:
            CURSOR = CONN.cursor()
            CURSOR.execute(sql, (self.id_,))
        
        del type(self).all[self.id_]
        self.id_ = None

    def workers(self):
        from models.worker import Worker
        sql = """
            SELECT *
            FROM workers
            WHERE workers.shift_id = ?
        """
        with create_conn() as CONN:
            CURSOR = CONN.cursor()
            workers = CURSOR.execute(sql, (self.id_,)).fetchall()

        return [Worker.instance_from_db(worker) for worker in workers] if workers else None


    def __repr__(self):
        return f"time_in = {self.time_in}, time_out = {self.time_out}, restaurant_id = {self.restaurant_id}, Id = {self.id_}"