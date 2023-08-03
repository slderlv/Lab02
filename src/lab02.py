# Encontrar los primeros 100 números de la secuencia de Fibonacci
Fibonacci = [0,1]
for i in range(98): # 98 porque ya tenemos los dos primeros
  Fibonacci.append(Fibonacci[-1]+Fibonacci[-2])
print(Fibonacci)

textFile = open("src/Fibonacci.txt","w")
for number in Fibonacci:
  textFile.write(str(number)+"\n")