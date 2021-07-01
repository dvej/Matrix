# Program creates a square matrix from numbers written down in spiral that starts from upper-left corner and ends in center of the matrix.

def spirala(n):
    a = [[0 for j in range(n)] for i in range(n)]
    if n % 2 != 0:
        poz = int((n-1)/2)
        a[poz][poz] = n**2
    br = 0
    for i in range(n//2):
        for j in range(i,n-1-i):
            br += 1
            a[i][j] = br
        for j in range(i,n-1-i):
            br += 1
            a[j][n-1-i] = br
        for j in reversed(range(i+1,n-i)):
            br += 1
            a[n-1-i][j] = br
        for j in reversed(range(i+1,n-i)):
            br += 1
            a[j][i] = br
    return a

m = int(input("Enter square matrix sides length: "))
for red in (spirala(m)):
    for element in red:
        print("{:3d}".format(element),end=" ")
    print()
