space_academy = {
    "academy_name": "Galaxy Horizon Advanced Academy",
    "location": "Orbit of Mars, Sector 7-G",
    "established_year": 2142,
    "is_active": True,
    "administration": {
        "dean": "Dr. Elena Vance",
        "vice_dean": "Commander Rex Jarvis",
        "contacts": {"email": "admin@gha.edu", "subspace_freq": "884.2-A"},
    },
    "departments": {
        "astrophysics": {
            "head": "Prof. Liam Sterling",
            "budget_credits": 1500000.50,
            "labs": ["Deep Space Observatory", "Quantum Particle Accelerator"],
        },
        "xenobiology": {
            "head": "Dr. T'Miri (Vulcan)",
            "budget_credits": 2100000.00,
            "labs": ["Bio-Dome Alpha", "Exo-Pathogen Containment Unit"],
        },
        "starship_engineering": {
            "head": "Chief Engineer Montgomery",
            "budget_credits": 4500000.75,
            "labs": ["Warp Drive Assembly", "Hull Stress Testing Rig"],
        },
    },
    "students": [
        {
            "id": "S-001",
            "name": "Alex Mercer",
            "age": 21,
            "species": "Human",
            "department": "starship_engineering",
            "gpa": 3.85,
            "is_on_scholarship": True,
            "courses_enrolled": ["Warp Theory I", "Titanium Welding", "Orbital Mechanics"],
            "grades": {"Warp Theory I": 95, "Titanium Welding": 88},
            "emergency_contact": ("Sarah Mercer", "Mother", "+1-555-MARS-01"),
        },
        {
            "id": "S-002",
            "name": "Zorblax the Undying",
            "age": 142,
            "species": "Protonian",
            "department": "astrophysics",
            "gpa": 3.98,
            "is_on_scholarship": False,
            "courses_enrolled": ["Black Hole Topology", "Quantum Mechanics IV", "Orbital Mechanics"],
            "grades": {"Black Hole Topology": 100, "Quantum Mechanics IV": 97, "Orbital Mechanics": 99},
            "emergency_contact": ("Grand High Hive", "Government", "Subspace-Channel-9"),
        },
        {
            "id": "S-003",
            "name": "Kira Dax",
            "age": 19,
            "species": "Trill",
            "department": "xenobiology",
            "gpa": 3.42,
            "is_on_scholarship": True,
            "courses_enrolled": ["Exo-Flora Analysis", "Genetic Splicing", "Invertebrate Psychology"],
            "grades": {"Exo-Flora Analysis": 85, "Genetic Splicing": 78},
            "emergency_contact": ("Tobias Dax", "Father", "+3-222-TRIL-99"),
        },
        {
            "id": "S-004",
            "name": "John Doe",
            "age": 23,
            "species": "Human",
            "department": "starship_engineering",
            "gpa": 2.15,
            "is_on_scholarship": False,
            "courses_enrolled": ["Titanium Welding", "Basic Blueprint Reading"],
            "grades": {"Titanium Welding": 60, "Basic Blueprint Reading": 65},
            "emergency_contact": None,
        },
    ],
    "facilities_status": {
        "power_grid": "Stable (92%)",
        "life_support": "Optimal",
        "shields": "Offline for Maintenance",
    },
}


# Рівень "Новачок" (Доступ по ключах):

# 1). Вивести на екран ім'я декана академії.
print (f"Ім'я декана академії: {space_academy['administration']['dean']}")


# 2). Вивести назву другої лабораторії факультету ксенобіології (xenobiology).
print (f"Назва другої лабораторії факультету ксенобіології: {space_academy['departments']['xenobiology']['labs'][1]}")


# 3). Вивести телефон екстреного зв'язку (emergency_contact) першого студента в списку.
print (f"Телефон екстреного зв'язку першого студента в списку: {space_academy['students'][0]['emergency_contact'][2]}")


# Рівень "Мідл" (Цикли та фільтрація):

# 1). Написати цикл, який виведе імена всіх студентів та їхній середній бал (gpa).
for i in range(len(space_academy['students'])):
    print (f"Студент {space_academy['students'][i]['name']} та його середній бал {space_academy['students'][i]['gpa']}")


# 2). Порахувати загальний бюджет (budget_credits) всіх факультетів академії.
total_budget = 0
for value in space_academy['departments'].values():
    total_budget = total_budget + int(value['budget_credits'])
print(f"Загальний бюджет всіх факультетів академії: {total_budget}")


# 3). Знайти всіх студентів, які навчаються на стипендії (is_on_scholarship: True), і вивести їхні ID.
students_with_stipend = ''
for i in range(len(space_academy['students'])):
    if space_academy['students'][i]['is_on_scholarship'] == True:
        students_with_stipend += (f"Студент {space_academy['students'][i]['name']} (id: {space_academy['students'][i]['id']}) навчається на стипендії.\n")
print(students_with_stipend)
if len(students_with_stipend) == 0:
    print('Немає студентів, які навчаються на стипендії.')