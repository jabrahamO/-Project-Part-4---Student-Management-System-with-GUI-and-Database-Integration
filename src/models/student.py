class Student:
    def __init__(self, student_id: str, name: str, age: int):
        self.id = student_id
        self.name = name
        self.age = age


    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
           
        }
