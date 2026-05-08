def sumList(arr): #given a list, caculates the sum of the nums in the list 
    sum = 0
    for i in arr:
        sum += i
    return sum

if __name__ == "__main__":
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    randlist = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if sumList((i,j,k))!= n]

    print(randlist)
