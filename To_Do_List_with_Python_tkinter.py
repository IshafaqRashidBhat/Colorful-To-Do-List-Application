import tkinter as tk
from tkinter import ttk

def add_task():
    """Function to add a task to the list."""
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)  # Add the task to the end of the listbox
        task_entry.delete(0, tk.END)  # Clear the task entry field

def remove_task():
    """Function to remove the selected task from the list."""
    try:
        selected_index = task_listbox.curselection()[0]  # Get the index of the selected task
        task_listbox.delete(selected_index)  # Remove the task from the listbox
    except IndexError:
        pass

def mark_completed():
    """Function to mark the selected task as completed."""
    try:
        selected_index = task_listbox.curselection()[0]  # Get the index of the selected task
        task_listbox.itemconfig(selected_index, {'bg': 'light gray', 'fg': 'gray', 'font': ('Arial', 10, 'italic')})
    except IndexError:
        pass

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Entry field for adding tasks
task_entry = tk.Entry(root, width=40, font=('Arial', 12))
task_entry.pack(pady=10)

# Button to add tasks
add_button = tk.Button(root, text="Add Task", command=add_task, bg='light green', fg='black', font=('Arial', 12, 'bold'))
add_button.pack(pady=5)

# Button to remove tasks
remove_button = tk.Button(root, text="Remove Task", command=remove_task, bg='light coral', fg='black', font=('Arial', 12, 'bold'))
remove_button.pack(pady=5)

# Button to mark tasks as completed
completed_button = tk.Button(root, text="Mark Completed", command=mark_completed, bg='light sky blue', fg='black', font=('Arial', 12, 'bold'))
completed_button.pack(pady=5)

# Listbox to display tasks
task_listbox = tk.Listbox(root, width=50, height=10, font=('Arial', 12), bg='white', fg='black', selectbackground='light yellow')
task_listbox.pack()

# Start the Tkinter event loop
root.mainloop()
