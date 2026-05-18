import matplotlib.pyplot as s

marks = [45, 50, 60, 62, 65, 70, 72, 75, 80, 82, 85, 90, 95]
s.xlabel(marks)
s.title('marks distribution')
s.grid()
s.hist(marks,color="Blue")
s.show()

hours = [1,2,2,3,3,3,4,4,5,5,6,7,8]
s.hist(hours,color="lightblue")
s.grid()
s.title('hours')
fontsize=18
s.show()

hours = [1,2,3,4,5,6,7]
marks = [35,40,50,60,72,80,92]
s.scatter(hours,marks)
s.title('hours vs marks')
s.xlabel('hours')
s.ylabel('marks')
s.show()

training_hours = [1,2,3,4,5,6]
accuracy = [50,55,65,72,85,93]
s.scatter(training_hours,accuracy,marker="o",color="orange")
s.show()

resources = ["Diamond", "Iron", "Gold", "Coal"]
count = [25, 40, 15, 60]
s.bar(resources,count)

