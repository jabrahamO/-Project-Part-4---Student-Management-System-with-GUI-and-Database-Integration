import customtkinter as ctk
from tkinter import messagebox
from models.student import Student

#main_window.py

class main_window(ctk.CTk):
    def __init__(self, manager):
        super().__init__()
        self.manager = manager



        self.title("Student Management System")
        self.geometry("780x600")

        self.formFrame = ctk.CTkFrame(self)
        self.formFrame.pack(fill= "x",padx=10,pady=10)
        self.formFrame.columnconfigure(0, weight = 1)
        self.formFrame.columnconfigure(1, weight = 2)
        self.formFrame.columnconfigure(2, weight = 1)


        # Id entry
        self.idLabel = ctk.CTkLabel(self.formFrame, text = "ID entry")
        self.idEntry = ctk.CTkEntry(self.formFrame)
        # Id entry settings
        self.idLabel.grid(column=0, row=0, sticky="w", padx=10, pady=5)
        self.idEntry.grid(column=1, row=0, sticky="ew", padx=10, pady=5)

        # student name
        self.nameLabel = ctk.CTkLabel(self.formFrame, text = "Name entry")
        self.nameEntry = ctk.CTkEntry(self.formFrame)
        # student name settings
        self.nameLabel.grid(column=0, row=1, sticky="w", padx=10, pady=5)
        self.nameEntry.grid(column=1, row=1, sticky="ew", padx=10, pady=5)

        # student Age entry
        self.ageLabel = ctk.CTkLabel(self.formFrame, text = "Age entry")
        self.ageEntry = ctk.CTkEntry(self.formFrame)
        # student Age entry settings
        self.ageLabel.grid(column=0, row=2, sticky="w", padx=10, pady=5)
        self.ageEntry.grid(column=1, row=2, sticky="ew", padx=10, pady=5)

        #freme for button
        self.buttonsFrame = ctk.CTkFrame(self)
        self.buttonsFrame.pack(fill = "x", padx=10, pady=10)

        # button for add student and setting
        self.btnAdd = ctk.CTkButton(self.buttonsFrame, text="Add Student", command=self.add_student )
        self.btnAdd.pack(side="left", padx=10, pady=10, fill="x", expand=True)

        # button for view student and setting
        self.btnview = ctk.CTkButton(self.buttonsFrame, text="View Students", command=self.view_students)
        self.btnview.pack(side="left", padx=10, pady=10, fill="x", expand=True)

        # button for search student and setting
        self.btnsearch = ctk.CTkButton(self.buttonsFrame, text="Search Student", command=self.search_student)
        self.btnsearch.pack(side="left", padx=10, pady=10, fill="x", expand=True)

        # button for delete student and setting
        self.btndelete = ctk.CTkButton(self.buttonsFrame, text="Delete Student", command=self.delete_student)
        self.btndelete.pack(side="left", padx=10, pady=10, fill="x", expand=True)
        
        self.outputLabel = ctk.CTkLabel(self, text="Result Area")
        self.outputLabel.pack(padx=10, anchor='w')
        
        self.outputArea = ctk.CTkTextbox(self, height=250)
        self.outputArea.pack(fill="both",padx=10, pady=(0,10), expand= True)
        
     # button handel
    def add_student(self):
        student_id =self.idEntry.get().strip()
        name =self.nameEntry.get().strip()
        age =self.ageEntry.get().strip()
        #vadidation
        if not student_id or not name or not age:
            messagebox.showwarning("Validation","All field are required!")
            return
        if not age.isdigit():
            messagebox.showwarning("Validation", "Age must be numeric!")
            return
        new_student = Student(student_id,name,int(age))
        if self.manager.add_student(new_student):
            messagebox.showinfo("Success", "Student added successfully!")
            self.clear_entries()
            self.view_students()
        else:
            messagebox.showerror("Error", "Duplicate ID detected!")
    
    def view_students(self):
        self.outputArea.delete("1.0", "end")
        students =self.manager.get_all()
        
        if not students:
            self.outputArea.insert('end',"No students in the record.")
            return
        for s in students:
            self.outputArea.insert("end", f"ID: {s.id} / Name: {s.name} / Age: {s.age}\n")
    
    def search_student(self):
        student_id = self.idEntry.get().strip()
        if not student_id:
            messagebox.showwarning("Search","Please enter student ID to search.")
            return
        
        student = self.manager.find_by_id(student_id)
        self.outputArea.delete("1.0","end")
        
        if student:
            self.outputArea.insert("end",f'Student Found:\nID: {student.id}\nName: {student.name}\nAge:{student.age}')
        else:
            self.outputArea.insert("end", "Student not found.")
    
    def delete_student(self):
        student_id = self.idEntry.get().strip()
        
        if not student_id:
            messagebox.showwarning("Delete","Please enter student ID to delete.")
            return
        
        if messagebox.askyesno("Confirm", f"Are you sure you want to delete ID: {student_id}?"):
            if self.manager.delete_student(student_id):
                messagebox.showinfo("Deleted","Student record removed.")
                self.view_students()
                self.clear_entries()
            else:
                messagebox.showerror("Error","Student ID not found.")
    
    def clear_entries(self):
        self.idEntry.delete(0,"end")
        self.nameEntry.delete(0,"end")
        self.ageEntry.delete(0,"end")
        