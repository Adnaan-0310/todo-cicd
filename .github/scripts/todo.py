class Task:
    def __init__(self, title, status="ToDo"):
        self.title = title
        self.completed = False
        self.status = status

    def mark_completed(self):
        self.completed = True
        self.status = "Done"

    def __repr__(self):
        return f"{self.title} - {self.status}"

    def __str__(self):
        return f"Task: {self.title}, Status: {self.status}"


class TaskPool:
    def __init__(self):
        self.tasks = []

    def populate(self):
        tasks = [Task("Write report"), Task("Review code"), Task("Set up repo"),
                 Task("Add tests"), Task("Deploy site"), Task("Update docs")]
        for t in tasks[:3]:
            t.mark_completed()
        self.tasks = tasks

    def add_task(self, task):
        self.tasks.append(task)

    def get_open_tasks(self):
        return [t for t in self.tasks if t.status == "ToDo"]

    def get_done_tasks(self):
        return [t for t in self.tasks if t.status == "Done"]


def main():
    pool = TaskPool()
    pool.populate()
    print("ToDo Tasks:")
    for title in [t.title for t in pool.get_open_tasks()]:
        print(title)
    print("Done Tasks:")
    for title in [t.title for t in pool.get_done_tasks()]:
        print(title)


if __name__ == "__main__":
    main()
