pyramidLayer = int(input("Number of layers of pyramid: "))
for i in range(pyramidLayer):
    print(" "*(pyramidLayer-i-1)+("*"*(2*i+1)))