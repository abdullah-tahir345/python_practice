class TaskList:
    def __init__(self):
        self.tasks = []
        
    def add_task(self, task):
        task_ = task.lower()
        self.tasks.append(task_.title())
        return f"Your task {task} is added successfully."
    
    def remove_task(self, task):
        task_ = task.lower()
        self.tasks.remove(task_.title())
        return f"Your task {task} is deleted successfully."
    
    def list_tasks(self):
        return self.tasks
    
    def clear_tasks(self):
        self.tasks.clear()
        return "All tasks deleted successfully."
    
if __name__ == "__main__":
    tas1 = TaskList()
    print(tas1.add_task('Learn About classes using Python'))
    print(tas1.add_task('Class Practice'))
    print(tas1.add_task('Approximately 10 tasks on Classes using ChatGPT'))
    
    print()
    print(tas1.list_tasks())
    
    print()
    print(tas1.remove_task('learn about classes using python'))
    print(tas1.list_tasks())
    
    print()
    print('Clear All Tasks')
    print(tas1.clear_tasks())