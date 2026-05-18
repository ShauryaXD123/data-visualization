import matplotlib.pyplot as s

players = [
    "Cristiano Ronaldo",
    "Lionel Messi",
    "Kylian Mbappe",
    "Erling Haaland",
    "Kevin De Bruyne",
    "Mohamed Salah",
    "Harry Kane",
    "Vinicius Jr"
]

scores = [35, 28, 30, 32, 18, 24, 27, 21] 
s.xlabel('player name')
s.ylabel('scores')
ax=s.axes() 
ax.set_facecolor("black")
s.title('players vs scores') 
s.bar(players,scores,color=["red","lightblue","blue","red","red","white","white","yellow"])
s.show()