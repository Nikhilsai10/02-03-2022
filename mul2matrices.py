matOne = []
print("Enter 9 Elements for First Matrix: ")
for i in range(3):
    matOne.append([])
    for j in range(3):
        num = int(input())
        matOne[i].append(num)

matTwo = []
print("Enter 9 Elements for Second Matrix: ")
for i in range(3):
    matTwo.append([])
    for j in range(3):
        num = int(input())
        matTwo[i].append(num)

matThree = []
for i in range(3):
    matThree.append([])
    for j in range(3):
        mul = matOne[i][j] * matTwo[i][j]
        matThree[i].append(mul)

print("\nMultiplication Result of Two Given Matrices is:")
for i in range(3):
    for j in range(3):
        print(matThree[i][j], end=" ")
    print()
