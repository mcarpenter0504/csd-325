import tkinter as tk
from tkinter import Menu

class Todo(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()

        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks

        self.title("Carpenter-ToDo")
        self.geometry("300x400")

        menu_bar = Menu(self)
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        self.config(menu=menu_bar)

        # DIY title because linux is so great and wont display using self.title:D
        title_bar = tk.Frame(self, bg="white", height=30)
        title_bar.pack(fill=tk.X)

        title_label = tk.Label(title_bar, text="Carpenter-ToDo", bg="orange", fg="white")
        title_label.pack(expand=True, fill=tk.X, pady=5)

        todol = tk.Label(self, text="Right click on task to delete it", pady=10, bg="white", fg="black")
        self.tasks.append(todol)

        for task in self.tasks:
            task.pack(side=tk.TOP, fill=tk.X)

        self.task_create = tk.Text(self, height=3, bg="white", fg="black")
        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()

        self.bind("<Return>", self.add_task)

        self.colour_schemes = [
            {"bg": "orange", "fg": "white"},
            {"bg": "blue", "fg": "white"}
        ]

    def add_task(self, event=None):
        task_text = self.task_create.get(1.0, tk.END).strip()
        if len(task_text) > 0:
            new_task = tk.Label(self, text=task_text, pady=10)
            _, task_style_choice = divmod(len(self.tasks), 2)
            my_scheme_choice = self.colour_schemes[task_style_choice]
            new_task.configure(bg=my_scheme_choice["bg"])
            new_task.configure(fg=my_scheme_choice["fg"])
            new_task.pack(side=tk.TOP, fill=tk.X)
            new_task.bind("<Button-3>", self.remove_task)
            self.tasks.append(new_task)
            self.task_create.delete(1.0, tk.END)

    def remove_task(self, event):
        event.widget.destroy()
        self.tasks.remove(event.widget)

if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()
    