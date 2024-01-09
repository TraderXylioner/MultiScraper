from dataclasses import dataclass

from type import Request


@dataclass
class Task:
    def __init__(self, task: list[Request] | None = None):
        self.task = task if task else []

    def add(self, task: Request):
        self.task.append(task)

    def remove(self, task: Request):
        self.task.remove(task)

    def __repr__(self):
        return f'{self.task}'

    def __len__(self):
        return len(self.task)

    def __getitem__(self, index):
        return self.task[index]

    def __setitem__(self, index, value):
        self.task[index] = value

    def __delitem__(self, index):
        del self.task[index]
