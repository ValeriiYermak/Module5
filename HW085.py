grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
def formatted_grades(students):
    count = 0
    fin_table = []
    for std, grd in students.items():
        count += 1
        row = ('{num:>4d}|{name:10s}|{mark:^5s}|{grade_num:^5d}'.format(num=count, name=std, mark=grd, grade_num=grades.get(grd)))
        print (row)
        fin_table.append(row)
    return fin_table