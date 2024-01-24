class Course:
    #ορίζονται τα αντικείμενα της τάξης Course των οποίων τα στοιχεία είναι αντίστοιχα με τα πεδία του lessons.csv
    def __init__(self, id, date_time, exam_rooms, semester, professor, supervisors_needed):
        self.id = id
        self.date_time = date_time
        self.exam_rooms = exam_rooms
        self.semester = semester
        self.professor = professor
        self.supervisors_needed = supervisors_needed
        
class Supervisor:
    #ορίζονται τα αντικείμενα της τάξης Supervisor των οποίων τα στοιχεία είναι αντίστοιχα με τα πεδία του supervisors.csv
    #υπάρχει το προαιρετικό όρισμα preferences που καλύπτει το δεύτερο bonus της εργασίας
    def __init__(self, id, name, email, supervisions, unavailabilities, preferences=[]):
        self.id = id
        self.name = name
        self.email = email
        self.supervisions = supervisions
        self.unavailabilities = unavailabilities
        self.preferences = preferences