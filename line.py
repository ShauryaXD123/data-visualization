import matplotlib.pyplot as s
# Day vs temperature line graph

# X-axis (Days)
day = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# Y-axis (Temperature in °C for Bhopal)
temperature = [39,41,42,40,38,37,39,43,44,42,40,39,41,43,42]

s.xlabel('Day')
s.ylabel('Temp in *C')
s.title('Day vs temperature')
s.plot(day,temperature)
s.show()