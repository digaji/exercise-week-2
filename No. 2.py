student1 = 80.0
student2 = 90.0
student3 = 66.5

def average(score1, score2, score3):
    total_score = score1 + score2 + score3
    average = total_score / 3
    print("Student scores:")
    print(score1, score2, score3, sep='\n')
    print("Average " + str(average))

average(student1, student2, student3)