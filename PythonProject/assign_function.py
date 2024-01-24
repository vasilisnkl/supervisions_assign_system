from dictionaries import dicts

from bonus_1 import bonus1

def assign(courses, supervisors):

    sups, num_lessons, restrictions_broken, lessons_in_sup, assigned = dicts(supervisors)

    supers = [s for s in num_lessons.keys()]
    #το supers είναι μία λίστα με αντικείμενα της τάξης Supervisor,
    #τα οποία βρίσκονται σε φθίνουσα σειρά με βάση τον αριθμό των μαθημάτων τα οποία μπορεί να εποπτεύσει ο κάθε επόπτης
    for course in courses:

        available_sups = [supervisor for supervisor in supers if str(course.id) not in supervisor.unavailabilities and sups[supervisor.name] < supervisor.supervisions]
        assigns = []
        #για κάθε μάθημα, η available_sups περιέχει τους επόπτες που είναι διαθέσιμοι: 
        #ελέγχεται αν ο κωδικός του μαθήματος βρίσκεται στους περιορισμούς του επόπτη,
        #καθώς και αν οι εποπτείες που έχει αναλάβει έως τώρα δεν ξεπερνούν τον μέγιστο αριθμό εποπτειών που μπορεί να αναλάβει

        for i in range(course.supervisors_needed):
            #όσο δεν έχει καλυφθεί ο απαραίτητος αριθμών εποπτών για το μάθημα, το πρόγραμμα κάνει αναθέσεις
            if len(available_sups) == 0:
                #αν δεν υπάρχουν διαθέσιμοι επόπτες τότε καλείται το bonus_1 ώστε να παραβιαστούν οι κατάλληλοι περιορισμοί
                assigns.extend(bonus1(sups, assigns, course, restrictions_broken))
                break
            
            #επιλέγεται ο επόπτης προς ανάθεση και τοποθετείται στη λίστα assigns
            assigned_sup = available_sups.pop(0)
            assigns.append(assigned_sup)
            sups[assigned_sup.name] += 1

        assigned[course.id] = assigns
        for x in assigns:
            lessons_in_sup[x].append(course.id)

    return assigned, lessons_in_sup