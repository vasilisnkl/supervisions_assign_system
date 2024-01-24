#η παρακάτω συνάρτηση για κάθε επόπτη προσπαθεί να ικανοποιήσει κάθε του επιθυμία
#για κάθε του προτίμηση, εφόσον δεν εποπτεύει ήδη σε αυτή, ψάχνει κάποιον επόπτη που να μπορεί να τον αντικαταστήσει
#για να το κάνει αυτό πάει σε κάθε μάθημα του αρχικού επόπτη, μέχρι να βρει αυτό στο οποίο ο επόπτης, με τον οποίο θα γίνει η ανταλλαγή, 
#δεν βρίσκεται ήδη αλλά ούτε το συγκεκριμένο είναι στους περιορισμούς τους   
def bonus2(supervisors, assigned, lessons_in_sup):
    for s in supervisors:
        #για κάθε επόπτη...
        for pr in s.preferences:
            #για κάθε του προτίμηση...
            #εφόσον δεν εποπτεύει ήδη
            if s not in assigned[int(pr)]:
                #για κάθε επόπτη του μαθήματος που είναι προτίμησή του...
                for x in assigned[int(pr)]:
                    #ψάχνει μάθημα όπου ο επόπτης ικανοποιεί τα κριτήρια που αναφέρθηκαν
                    for lesson in lessons_in_sup[s]:
                        if x in assigned[lesson] or str(lesson) in x.unavailabilities:
                            continue
                        else:
                            #γίνεται η ανταλλαγή
                            try:
                                assigned[lesson].append(x)
                                assigned[lesson].remove(s)
                                assigned[int(pr)].remove(x)
                                assigned[int(pr)].append(s)
                                lessons_in_sup[s].remove(lesson)
                                lessons_in_sup[s].append(int(pr))
                                lessons_in_sup[x].remove(int(pr))
                                lessons_in_sup[x].append(lesson)
                                break
                            except ValueError:
                                print(s.name)
                    break
    return assigned