import datetime


class Project:
    def __init__(self, name, priority, start_date, completion=0):
        self.name = name
        self.priority = priority
        self.start_date = start_date
        self.completion = completion

    def __str__(self):
        return f"{self.name} ({self.priority}) - {self.start_date.strftime('%m/%d/%Y')} - {self.completion}%"

    def __lt__(self, other):
        return self.priority < other.priority

    def __eq__(self, other):
        return self.priority == other.priority