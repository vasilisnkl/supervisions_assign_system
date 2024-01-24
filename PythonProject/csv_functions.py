from classes import Course, Supervisor

def get_courses_from_csv(lessons):
    #μετατρέπει κάθε σειρά του lessons.csv σε αντικείμενο και τα τοποθετεί στην λίστα courses
    courses = list()
    lessons.readline()
    for line in lessons:
        line = line.strip()
        ls = line.split(',')
        exam = Course(int(ls[0]), ls[1], ls[2], ls[3], ls[4], int(ls[5]))
        courses.append(exam)
    return courses

def get_supervisors_from_csv(supervisors):
    #μετατρέπει κάθε σειρά του supervisors.csv σε αντικείμενο και τα τοποθετεί στην λίστα supervisors
    visors = list()
    supervisors.readline()
    for line in supervisors:
        line = line.strip()
        ls = line.split(',')
        if len(ls) < 6:
            supervisor = Supervisor(int(ls[0]), ls[1], ls[2], int(ls[3]), ls[4])
        else:
            #κατασκευάζει τα αντικείμενα σε περίπτωση που έχουν δωθεί προτιμήσεις (bonus 2)
            #τα preferences μετατρέπονται σε λίστα μέσω της εντολής ls[5][1:-1].split(' ') 
            supervisor = Supervisor(int(ls[0]), ls[1], ls[2], int(ls[3]), ls[4], ls[5][1:-1].split(' '))
        visors.append(supervisor)    
    return visors
