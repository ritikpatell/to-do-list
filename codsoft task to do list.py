import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        
        self.tasks = []

        self.task_entry = tk.Entry(root, font=("Helvetica", 14))
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.tasks_listbox = tk.Listbox(root, font=("Helvetica", 14), selectmode=tk.SINGLE)
        self.tasks_listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_tasks_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty.")

    def remove_task(self):
        selected_index = self.tasks_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            removed_task = self.tasks.pop(index)
            self.update_tasks_listbox()
            messagebox.showinfo("Removed", f"Task '{removed_task}' removed.")
        else:
            messagebox.showwarning("Warning", "Select a task to remove.")

    def update_tasks_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task)

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
