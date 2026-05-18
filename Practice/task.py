import matplotlib.pyplot as s
import numpy as np

students=["aman","shaurya","pranav","neha","rohit"]
marks = [85, 92, 76, 88, 69]
s.bar(students,marks,color=["red","blue","green","yellow","orange"])
s.xlabel('student name')
s.ylabel('marks')
s.title('students vs marks')
s.show()

matches=[1,2,3,4,5]

virat=[45,80,60,100,75]

rohit=[30,70,90,85,65]
s.xlabel('matches')
s.ylabel('player scores')
s.title('Virat vs Rohit')
s.plot(matches,virat,color="red",label="virat")
s.plot(matches,rohit,color="blue",label="rohit")
s.legend()
s.grid()
s.show()

models=["Linear", "Decision Tree", "Random Forest", "SVM"]
accuracy=[78,85,92,88]
s.grid(axis="y")
s.title('models vs accuracy')
s.bar(models,accuracy,color=["red","black","green","purple"])
s.show()

months=["Jan","Feb","Mar","Apr","May"]
channel1=[1000,2000,3500,5000,7000]
channel2=[1500,2500,3000,4500,6000]
s.xlabel('months')
s.ylabel('channel growth')
s.title('channel1 vs channel2')
s.legend()
s.plot(months,channel1,color="green",label="channel1")
s.plot(months,channel2,color="pink",label="channel2")
linestyle="big"
marker="o"
fontsize=18
s.show()

hours = [6, 3, 8, 2]
activities = ["Study", "Gaming", "Sleep", "Exercise"]
s.pie(hours,labels=activities,autopct="%1.1f%%")
s.title('percentage ditribution of activities')
s.show()

players=["steve","alex","herobrine"]
diamonds=[25,40,15]

s.xlabel('players')
s.ylabel('diamonds')
s.bar(players,diamonds,color=["lightblue","yellow","red"])
s.title('players vs diamonds')
s.grid()
print("max diamond :",np.max(diamonds))
print("min diamond:",np.min(diamonds))
s.show()








