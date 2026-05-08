# from src.models.student import Student
import sqlite3
from models.student import Student
#student_manager.py
class StudentManager:
    def __init__(self,db_name="students.db"):
        self.db_name = db_name
        self.setup_database()
        
    def setup_database(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS students(
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL)""")
        conn.commit()
        conn.close()
        

    def add_student(self, student: Student) -> bool:
        
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO students (id, name, age) VALUES(?,?,?)",
                           (student.id, student.name,student.age))
            conn.commit()
            conn.close()
            return True
        #haddle duplicate id
        except sqlite3.IntegrityError:
            return False
           

    def find_by_id(self, student_id: str) -> Student | None:
        
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE id = ?",(student_id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return Student(row[0],row[1],row[2])
        return None

    def get_all(self) -> list[Student]:
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        conn.close()
        return [Student(row[0],row[1],row[2]) for row in rows]
    

    def delete_student(self, student_id: str) -> bool:
        
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id = ?",(student_id,))
        changes = conn.total_changes
        conn.commit()
        conn.close()
        return changes > 0
        