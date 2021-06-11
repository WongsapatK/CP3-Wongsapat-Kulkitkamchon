userInput = int(input("Number of layers of pyramid: "))
for i in range(userInput):
    print(" "*(userInput-i-1)+("*"*(2*i+1)))