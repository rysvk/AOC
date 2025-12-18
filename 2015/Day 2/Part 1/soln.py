with open('input.txt', 'r') as file:
    data = file.readlines() 
lines = [line.split("x") for line in data] 
sides = [sorted([int(num) for num in line]) for line in lines]
print(sum(3*sides[i][0]*sides[i][1] + 2*sides[i][0]*sides[i][2] + 2*sides[i][1]*sides[i][2] for i in range(len(sides))))

