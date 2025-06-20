import json

class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {'title': self.title, 'completed': self.completed}

    def __str__(self):
        status = '✔' if self.completed else '✘'
        return f'[{status}] {self.title}'
    

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)

    def show_tasks(self):
        if not self.tasks:
            print('Список задач пуст')
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f'{i}. {task}')

    def complete_task(self, ind):
        ind = ind - 1
        if 0 <= ind < len(self.tasks):
            self.tasks[ind].mark_completed()
        else:
            print('Неверный индекс')

    def delete_task(self, ind):
        ind = ind - 1
        if 0 <= ind < len(self.tasks):
            del self.tasks[ind]
        else:
            print('Неверный индекс')

    def save_tasks(self):
        #преобразовываем объект класса в список словарей, тк json не умеет обрабатывать польз. классы
        #data = [{'title': task.title, 'completed': task.completed} for task in tasks]
        with open('tasks.json', 'w', encoding='utf-8') as file:
            json.dump([task.to_dict() for task in self.tasks], file, ensure_ascii=False, indent=2)

    def load_tasks(self):
        try:
            with open('tasks.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.tasks = [Task(item['title'], item['completed']) for item in data]
        except FileNotFoundError:
            self.tasks =  []