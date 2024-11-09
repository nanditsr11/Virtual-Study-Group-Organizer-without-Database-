import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from datetime import datetime

# App Class
class StudyGroupApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Study Group Organizer")
        self.root.geometry("600x400")
        
        # In-memory storage for groups
        self.groups = []
        
        # UI Setup
        self.create_widgets()

    def create_widgets(self):
        # Group List Display
        self.group_list_label = tk.Label(self.root, text="Study Groups:", font=("Arial", 14))
        self.group_list_label.pack(pady=5)

        self.group_listbox = tk.Listbox(self.root, width=70, height=10)
        self.group_listbox.pack(pady=10)

        # Buttons
        self.add_btn = tk.Button(self.root, text="Add Study Group", command=self.add_group)
        self.add_btn.pack(pady=5)
        
        self.view_btn = tk.Button(self.root, text="View Details", command=self.view_group)
        self.view_btn.pack(pady=5)
        
        self.delete_btn = tk.Button(self.root, text="Delete Study Group", command=self.delete_group)
        self.delete_btn.pack(pady=5)

        # Group Details Display
        self.details_label = tk.Label(self.root, text="Group Details:", font=("Arial", 14))
        self.details_label.pack(pady=5)

        self.details_text = tk.Text(self.root, width=70, height=5, wrap="word", state="disabled")
        self.details_text.pack(pady=5)

    def load_groups(self):
        """Reloads the groups listbox."""
        self.group_listbox.delete(0, tk.END)
        for group in self.groups:
            self.group_listbox.insert(tk.END, group["group_name"])

    def add_group(self):
        """Adds a new group."""
        group_name = simpledialog.askstring("Group Name", "Enter the study group name:")
        topic = simpledialog.askstring("Topic", "Enter the study topic:")
        meeting_time = simpledialog.askstring("Meeting Time", "Enter meeting time (YYYY-MM-DD HH:MM):")
        
        try:
            # Validate meeting time format
            datetime.strptime(meeting_time, "%Y-%m-%d %H:%M")
            new_group = {"group_name": group_name, "topic": topic, "meeting_time": meeting_time}
            self.groups.append(new_group)
            messagebox.showinfo("Success", "Study group added successfully!")
            self.load_groups()
        except ValueError:
            messagebox.showerror("Invalid Date", "Please enter a valid date in format YYYY-MM-DD HH:MM.")

    def view_group(self):
        """Displays details of the selected group."""
        selected = self.group_listbox.curselection()
        if selected:
            index = selected[0]
            group = self.groups[index]
            group_details = f"Group Name: {group['group_name']}\nTopic: {group['topic']}\nMeeting Time: {group['meeting_time']}"
            self.details_text.config(state="normal")
            self.details_text.delete("1.0", tk.END)
            self.details_text.insert(tk.END, group_details)
            self.details_text.config(state="disabled")
        else:
            messagebox.showwarning("No Selection", "Please select a group to view details.")

    def delete_group(self):
        """Deletes the selected group."""
        selected = self.group_listbox.curselection()
        if selected:
            index = selected[0]
            del self.groups[index]
            messagebox.showinfo("Deleted", "Study group deleted successfully.")
            self.load_groups()
            self.details_text.config(state="normal")
            self.details_text.delete("1.0", tk.END)
            self.details_text.config(state="disabled")
        else:
            messagebox.showwarning("No Selection", "Please select a group to delete.")

# Main Application
root = tk.Tk()
app = StudyGroupApp(root)
root.mainloop()
