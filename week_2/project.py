import time

class TODO:
    def __init__(self):
        # store todos per-instance rather than as a class variable
        self.todos = []
    
    def add_todo(self, desc):
        # description is passed in; callers should supply it (useful for tests)
        if not desc:
            # fall back to prompting if nothing provided
            desc = input('Enter a todo: ')
        if desc == "":
            print("Todo cannot be empty")
            return
        
        task = {
            "id": int(time.time()),
            "desc": desc,
            "completed": False,
        }

        self.todos.append(task)
        print(f'-->{desc}: Todo added Successfully')

    def remove_todo(self, id):
        for todo in self.todos:
            if todo["id"] == id:
                self.todos.remove(todo)
                print("Todo removed")
                return
        print("Todo not found")
    
    def display_todos(self):
        if len(self.todos) == 0:
            print("No todos available")
            return

        for todo in self.todos:
            if todo["completed"]:
                status = "Completed"
            else:
                status = "Pending"

            print(todo["id"], ".", todo["desc"], "(", status, ")")


    
    def update_todo(self, id, new_desc):
        for todo in self.todos:
            if todo["id"] == id:
                todo["desc"] = new_desc
                print("Todo updated")
                return
        print("Todo not found")
    

    def toggle_mark_as_completed(self, id):
        for todo in self.todos:
            if todo["id"] == id:
                todo["completed"] = not todo["completed"]
                print("Todo status updated")
                return
        print("Todo not found")

    
    def completed_todos(self):
        if len(self.todos) == 0:
            print("No todos available")
            return
        
        for todo in self.todos:
            if todo.get('completed'):
                print(f"--> {todo['desc']}")
    
    def incompleted_todos(self):
        if len(self.todos) == 0:
            print("No todos available")
            return
        
        for todo in self.todos:
            if not todo.get('completed'):
                print(f"--> {todo['desc']}")
    
