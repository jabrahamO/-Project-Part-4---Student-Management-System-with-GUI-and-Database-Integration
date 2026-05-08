from data.student_manager import StudentManager
from ui.main_window import main_window

if __name__ == "__main__":
    manager = StudentManager()
    
    app = main_window(manager)
    app.mainloop()
