# todo_app.py
import json
import os
from datetime import datetime

class TodoApp:
    def __init__(self):
        self.tasks = []
        self.filename = "tasks.json"
        self.load_tasks()
    
    def add_task(self, task, priority="Medium"):
        """Add a new task"""
        new_task = {
            "id": len(self.tasks) + 1,
            "task": task,
            "priority": priority,
            "status": "Pending",
            "created": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        self.tasks.append(new_task)
        self.save_tasks()
        print(f" Task added: {task}")
    
    def view_tasks(self, filter_status=None):
        """View all tasks or filter by status"""
        if not self.tasks:
            print(" No tasks found!")
            return
        
        tasks_to_show = self.tasks
        if filter_status:
            tasks_to_show = [t for t in self.tasks if t["status"] == filter_status]
        
        print("\n" + "="*60)
        print(f"{'ID':<5} {'Task':<30} {'Priority':<10} {'Status':<10} {'Created'}")
        print("="*60)
        for task in tasks_to_show:
            print(f"{task['id']:<5} {task['task']:<30} {task['priority']:<10} {task['status']:<10} {task['created']}")
        print("="*60)
    
    def complete_task(self, task_id):
        """Mark a task as completed"""
        for task in self.tasks:
            if task["id"] == task_id:
                task["status"] = "Completed"
                self.save_tasks()
                print(f"🎉 Task '{task['task']}' completed!")
                return
        print(" Task not found!")
    
    def delete_task(self, task_id):
        """Delete a task"""
        self.tasks = [t for t in self.tasks if t["id"] != task_id]
        # Re-number IDs
        for i, task in enumerate(self.tasks, 1):
            task["id"] = i
        self.save_tasks()
        print(" Task deleted!")
    
    def save_tasks(self):
        """Save tasks to file"""
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=2)
    
    def load_tasks(self):
        """Load tasks from file"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.tasks = json.load(f)

def main():
    app = TodoApp()
    while True:
        print("\n TO-DO LIST MENU")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. View Pending Tasks")
        print("4. Complete Task")
        print("5. Delete Task")
        print("6. Exit")
        
        choice = input("Choose (1-6): ")
        
        if choice == "1":
            task = input("Enter task: ")
            priority = input("Priority (High/Medium/Low): ") or "Medium"
            app.add_task(task, priority)
        elif choice == "2":
            app.view_tasks()
        elif choice == "3":
            app.view_tasks("Pending")
        elif choice == "4":
            task_id = int(input("Enter task ID to complete: "))
            app.complete_task(task_id)
        elif choice == "5":
            task_id = int(input("Enter task ID to delete: "))
            app.delete_task(task_id)
        elif choice == "6":
            print("Goodbye! 💕")
            break

if __name__ == "__main__":
    main()
