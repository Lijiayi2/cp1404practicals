import pickle
from datetime import datetime

MENU = "\
- (L)oad projects\n\
- (S)ave projects\n\
- (D)isplay projects\n\
- (F)ilter projects by date\n\
- (A)dd new project\n\
- (U)pdate project\n\
- (Q)uit"
VALID_CHOICES = "LSDFAUQ"
NAME_INDEX = 0
START_DATE_INDEX = 1
PRIORITY_INDEX = 2
COST_ESTIMATE_INDEX = 3
COMPLETION_PERCENTAGE_INDEX = 4


class Project:
    def __init__(self, name, priority, start_date, completion=0):
        self.name = name
        self.priority = priority
        self.start_date = start_date
        self.completion = 0

    def __str__(self):
        return f"{self.name} ({self.priority}) - {self.start_date.strftime('%m/%d/%Y')} - {self.completion}%"

def main():
    global projects
    print("Welcome to the Project Management Program")
    print(MENU)

    choice = get_valid_choice()
    while choice != "Q":
        if choice == "L":
            projects = load_projects()
        elif choice == "S":
            save_projects(projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            projects = add_project(projects)
        elif choice == "U":
            update_project(projects)
        print(MENU)
        choice = get_valid_choice()
    print("Thank you for using custom-built project management software.")

def get_valid_choice():
    choice = input(">>> ").upper()
    while choice not in VALID_CHOICES:
        print("Invalid choice")
        choice = input(">>> ").upper()
    return choice


def get_valid_project_index(projects):
    project_index = int(input("Project choice: "))
    while project_index < 0 or project_index >= len(projects):
        print("Invalid project number")
        project_index = int(input("Project choice: "))
    return project_index


def get_valid_completion_percentage(minimum, maximum):
    new_completion_percentage = int(input("New Percentage: "))
    while new_completion_percentage < minimum or new_completion_percentage > maximum:
        print("Invalid completion percentage")
        new_completion_percentage = int(input("Completion percentage: "))
    return new_completion_percentage

def load_projects():
    try:
        with open("projects.dat", "rb") as file:
            projects = pickle.load(file)
    except FileNotFoundError:
        projects = []
    return projects


def save_projects(projects):
    with open("projects.dat", "wb") as file:
        pickle.dump(projects, file)


def display_projects(projects):
    unfinished = sorted([p for p in projects if p.completion < 100])
    finished = sorted([p for p in projects if p.completion == 100])

    print("Unfinished Projects:")
    if unfinished:
        for p in unfinished:
            print(p)
    else:
        print("No unfinished projects.")
    print()

    print("Finished Projects:")
    if finished:
        for p in finished:
            print(p)
    else:
        print("No finished projects.")
    print()

def filter_projects_by_date(projects):
    date_str = input("Enter start date (mm/dd/yyyy): ")
    try:
        date = datetime.strptime(date_str, "%m/%d/%Y")
    except ValueError:
        print("Invalid date format. Please use mm/dd/yyyy.")
        return

    filtered = sorted([p for p in projects if p.start_date >= date], key=lambda p: p.start_date)

    print("Filtered Projects:")
    if filtered:
        for p in filtered:
            print(p)
    else:
        print("No projects found for that date or later.")
    print()

def add_project(projects):
    name = input("Enter project name: ")
    priority = int(input("Enter project priority (1-5): "))
    date_str = input("Enter start date (mm/dd/yyyy): ")
    try:
        date = datetime.strptime(date_str, "%m/%d/%Y")
    except ValueError:
        print("Invalid date format. Please use mm/dd/yyyy.")
        return

    projects.append(projects(name, priority, date))
    print("Project added.")
    print()

def update_project(projects):
    print("Select a project to update:")
    for i, p in enumerate(projects):
        print(f"{i + 1}. {p}")
    try:
        selection = int(input("Enter project number: "))
        project = projects[selection - 1]
    except (ValueError, IndexError):
        print("Invalid selection.")
        return
    completion = input(f"Enter completion percentage ({project.completion}%): ")
    if completion:
        try:
            completion = int(completion)
            if completion < 0 or completion > 100:
                raise ValueError
        except ValueError:
            print("Invalid completion percentage.")
            return
        project.completion = completion

    priority = input(f"Enter priority ({project.priority}): ")
    if priority:
        try:
            priority = int(priority)
            if priority < 1 or priority > 5:
                raise ValueError
        except ValueError:
            print("Invalid completion percentage.")
            return
        project.priority = priority

        main()



