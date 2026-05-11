""" 
Author:Abraham Jheff Jhoven / Carillo Smith AJ 
Program: Project-Part-4---Student-Management-System-with-GUI-and-Database-Integration
Date: 05-11-2026
"""

from data.student_manager import StudentManager
from ui.main_window import main_window

if __name__ == "__main__":
    manager = StudentManager()
    
    app = main_window(manager)
    app.mainloop()
