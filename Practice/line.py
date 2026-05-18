import matplotlib.pyplot as s

# cylinderPrices=[600,750,900,750,700,800,1100,1050]
# year=[2019,2020,2021,2022,2023,2024,2025,2026]

# s.xlabel('Cyclinder prices')
# s.ylabel('Year')
# s.title('Cylinder prices vs Year')
# s.plot(year,cylinderPrices)
# s.show()


# 2 lines graph for minecraft PVP
# Match=[1,2,3,4,5]
# Pranav=[78,46,67,90,45]
# Shaurya=[90,95,85,98,69]
# s.xlabel('Matches')
# s.ylabel('Player scores')
# s.title('Shaurya vs Pranav')
# s.plot(Match,Shaurya,color="blue",label="Shaurya")
# s.plot(Match,Pranav,color="yellow", label="Pranav")
# s.legend()
# s.grid()
# s.show()


Time=[1,2,3,4,5,6,7,8,9,10]

Bugatti_Chiron=[0,42,87,132,178,224,268,312,378,420]

Koenigsegg_Jesko=[0,45,92,140,188,238,289,338,392,450]
s.xlabel('Time in seconds')
s.ylabel('Car speed')
s.title('Car speed per second')
s.plot(Time,Bugatti_Chiron,color="Blue",label="Bugatti_Chiron")
s.plot(Time,Koenigsegg_Jesko,color="red",label="koenigsegg_Jesko")
s.legend()
s.grid()
s.show()