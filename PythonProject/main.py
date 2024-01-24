lessons_csv = open('lessons.csv', 'r', encoding='utf8')
supervisors_csv = open('supervisors.csv', 'r', encoding='utf8')
sol = open('solution.txt', 'w', encoding='utf8')

from csv_functions import get_courses_from_csv, get_supervisors_from_csv

from assign_function import assign

from bonus_2 import bonus2

courses = get_courses_from_csv(lessons_csv)
supervisors = get_supervisors_from_csv(supervisors_csv)
assigned, lessons_in_sup = assign(courses, supervisors)

assigned = bonus2(supervisors, assigned, lessons_in_sup)

#επεξεργασία του αρχείου εξόδου
crs = []            
for x in courses:
    #η λίστα crs περιέχει τους κωδικούς κάθε μαθήματος
    crs.append(x.id)
x = 0
for i in assigned.values():
    #για κάθε λίστα εποπτών που έχει ανατεθεί σε κάθε μάθημα...
    sol.write('Exam ' + str(crs[x]) + ' with supervisors:\n')
    for j in range(courses[x].supervisors_needed):
        #κάθε επόπτη που χρειάζεται σε κάθε μάθημα τον παίρνει από τη λίστα i...
        try:
            sol.write(str(i[j].name) + ' ( ' + i[j].email + ' ) \n')
        except IndexError:
            sol.write('Δεν συμπληρώθηκαν οι επιτηρητές\n')
            break
    sol.write('\n')
    x += 1

lessons_csv.close()
supervisors_csv.close()
sol.close()