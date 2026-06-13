# Task_1

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self,name, salary)
        self.department = department

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size

team_lead = TeamLead("John Lennon", 20000, "QA Automation", programming_language = 'Python', team_size = 3)


assert hasattr(team_lead, "name")
print("The team lead has 'name' attribute.")
assert hasattr(team_lead, "salary")
print("The team lead has 'salary' attribute.")
assert hasattr(team_lead, "department")
print("The team lead has 'department' attribute.")
assert hasattr(team_lead, "programming_language")
print("The team lead has 'programming_language' attribute.")

