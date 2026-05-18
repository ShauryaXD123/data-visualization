import matplotlib.pyplot as s

# marks=[30,20,10,15,15]
# subjects=['Maths','Science','Hindi','Sanskrit','Economics']
# s.title('subject wise marks distribution')
# s.pie(marks,labels=subjects)
# s.show()

marks=[99,89,78,94,67]
name=['Shaurya','Pranav','Atharv','Soham','Bhavya']

s.title('percentage distribution of a class')
s.pie(marks,labels=name,autopct="%1.1f%%")
s.show()