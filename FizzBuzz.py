Lista = []
for i in range((101)):
    Lista.append(i)

for i in range(len(Lista)):
    if i % 5 == 0 and i % 3 == 0:
        osztható = i
        helyzet = Lista.index(osztható)
        Lista[helyzet] = "Fizz"+"Buzz" 
    elif i % 3 == 0:
        osztható = i
        helyzet = Lista.index(osztható)
        Lista[helyzet] = "Fizz"
    elif i % 5 == 0:
        osztható = i
        helyzet = Lista.index(osztható)
        Lista[helyzet] = "Buzz"

Lista.remove(Lista[0])
print(Lista)