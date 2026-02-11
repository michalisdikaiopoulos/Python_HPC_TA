def coursesstudents(students, course):
    return [s.name for s in students if s.attends(course)]