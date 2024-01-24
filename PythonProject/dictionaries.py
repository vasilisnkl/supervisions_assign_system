def dicts(supervisors):
    #αρχικοποιεί τα λεξικά που χρησιμοποιεί το πρόγραμμα
    sups = {}
    for s in supervisors:
        sups[s.name] = 0
        #κρατά για κάθε όνομα επόπτη τον αριθμό των επιτηρήσεων που του έχουν ανατεθεί 
    
    num_lessons = {}
    for s in supervisors:
        num_lessons[s] = s.supervisions
    num_lessons = dict(sorted(num_lessons.items(), key=lambda item: item[1], reverse=True))
    #κρατά τον αριθμό των επιτηρήσεων που μπορεί να αναλάβει κάθε επόπτης και ταξινομείται κατά φθίνουσα σειρά με βάση τον αριθμό αυτό

    restrictions_broken = {}
    for s in supervisors:
        restrictions_broken[s] = 0
    #κρατά για κάθε επόπτη τον αριθμό των περιορισμών που το πρόγραμμα έχει αγνοήσει
    
    lessons_in_sup = {}
    for s in supervisors:
        lessons_in_sup[s] = list()
    #κρατά για κάθε επόπτη μια λίστα που περιέχει τους κωδικούς των μαθημάτων τα οποία του έχουν ανατεθεί
    
    assigned = dict()
    #κρατά για κάθε κωδικό μαθήματος τους επόπτες που έχουν ανατεθεί σε αυτό το μάθημα

    return sups, num_lessons, restrictions_broken, lessons_in_sup, assigned