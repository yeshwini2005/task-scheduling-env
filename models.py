from pydantic import BaseModel
import random

class Observation(BaseModel):
    tasks: list
    task_type: str

class Action(BaseModel):
    order: list

class TaskSchedulingEnv:

    def __init__(self):
        self.tasks = []
        self.correct_order = []
        self.task_type = ""

    def generate_tasks(self):
        # Easy task
        easy = [
            {"name": "A", "deadline": 2, "priority": 3},
            {"name": "B", "deadline": 5, "priority": 1}
        ]

        # Medium task
        medium = [
            {"name": "A", "deadline": 2, "priority": 3},
            {"name": "B", "deadline": 5, "priority": 1},
            {"name": "C", "deadline": 1, "priority": 2}
        ]

        # Hard task
        hard = [
            {"name": "A", "deadline": 4, "priority": 2},
            {"name": "B", "deadline": 2, "priority": 3},
            {"name": "C", "deadline": 1, "priority": 1},
            {"name": "D", "deadline": 3, "priority": 3}
        ]

        choice = random.choice(["easy", "medium", "hard"])

        if choice == "easy":
            self.tasks = easy
        elif choice == "medium":
            self.tasks = medium
        else:
            self.tasks = hard

        self.task_type = choice

    def compute_correct_order(self):
        self.correct_order = sorted(
            range(len(self.tasks)),
            key=lambda i: (-self.tasks[i]["priority"], self.tasks[i]["deadline"])
        )

    def reset(self):
        self.generate_tasks()
        self.compute_correct_order()
        return Observation(tasks=self.tasks, task_type=self.task_type)

    def step(self, action: Action):
        score = 0

        for i in range(len(action.order)):
            if i < len(self.correct_order) and action.order[i] == self.correct_order[i]:
                score += 1

        reward = score / len(self.correct_order)

        # penalty for wrong length
        if len(action.order) != len(self.correct_order):
            reward -= 0.2

        done = True

        return self.reset(), max(0.0, reward), done, {}

    def state(self):
        return self.tasks
    