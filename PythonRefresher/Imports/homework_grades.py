"""
- Modules get used all the times throughout programming
- It helps with creating new files, with unique purposes, to help with clean maintainable code
"""

import grade_average_service as grade_service

homework_assignment_grades = {
    'homework_1': 85,
    'homework_2': 100,
    'homework_3': 81,
}

grade_service.calculate_homework(homework_assignment_grades)