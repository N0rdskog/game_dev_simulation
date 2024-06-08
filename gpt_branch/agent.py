class Agent:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.performance = 0
        self.tasks = []
        self.performance_metrics = {
            "tasks_completed": 0,
            "quality_of_work": 0,
            "speed": 0
        }

    def send_message(self, receiver, message_type, content):
        token = {
            "sender": self.name,
            "receiver": receiver.name,
            "type": message_type,
            "content": content
        }
        return token

    def receive_message(self, token):
        print(f"{self.name} received a message from {token['sender']}: {token['type']} - {token['content']}")
        self.process_message(token)

    def process_message(self, token):
        pass  # To be implemented by subclasses

    def add_task(self, task):
        self.tasks.append(task)

    def update_task_status(self, task_description, new_status):
        for task in self.tasks:
            if task.description == task_description:
                task.update_status(new_status)
                if new_status == "Completed":
                    self.performance_metrics["tasks_completed"] += 1
                break

    def report_task_status(self):
        for task in self.tasks:
            print(f"Task: {task.description}, Status: {task.status}, Due Date: {task.due_date}, Priority: {task.priority}")

    def update_performance(self, quality, speed):
        self.performance_metrics["quality_of_work"] += quality
        self.performance_metrics["speed"] += speed