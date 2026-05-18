import matplotlib.pyplot as s

pizza = [30, 20, 15, 25, 10]
ingredients = ['cheese', 'sauce', 'toppings', 'chicken', 'oregano']

s.title('pizza ingredients')
s.pie(pizza,labels=ingredients)
s.show()