def bonus1(sups, assigns, course, restrictions_broken):
    ls = list()
    for i in range(course.supervisors_needed - len(assigns)):
        #κάνει αναθέσεις για τον αριθμό των εποπτών που χρειάζονται ακόμα
        for j in restrictions_broken.keys():
            #για κάθε επόπτη παραβιάζει κάποιον περιορισμό του σε περίπτωση που είναι ελεύθερος
            if sups[j.name] != j.supervisions and j not in assigns:
                ls.append(j)
                sups[j.name] += 1
                restrictions_broken[j] += 1
                #κάθε φορά το restrictions_broken ταξινομείται κατά αύξουσα σειρά με βάση τον αριθμό των παραβιάσεων
                #εξασφαλίζοντας την δίκαιη παραβίαση των περιορισμών
                restrictions_broken = dict(sorted(restrictions_broken.items(), key=lambda item: item[1]))
                break
    return ls