import matplotlib.pyplot as s
#  marks vs names

names=["shaurya","pranav","shriya"]
marks=[99.9,90,67]

s.xlabel('student name')
s.ylabel('marks')
s.title('student analysis')
s.bar(names,marks)
s.show()