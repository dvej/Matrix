# Program creates a N*M matrix in form of an one-dimensional array from numbers of rows and columns that user defines.
# Than it makes a matrix transposition without using any additional memory (without additional matrix or array).

def transponovanje(niz,red,kol):
     n = len(niz)
     if red*kol != n:
          return False
     for i in range(1,red):
          for j in range(kol-1):
               for k in range(i*(kol-1-j)):
                    p = i*kol-k+j
                    niz[p],niz[p-1] = niz[p-1],niz[p]
     return niz

n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))
import string
a = []
for i in range(n):
    for j in range(1,m+1):
        a.append(string.ascii_letters[i] + str(j))
print(f"Matrix {n}x{m} in array form:",a)
mat = transponovanje(a,n,m)

if not mat:
     print("Wrong entry, not a matrix format")
else:
     print(f"Transposed Matrix {m}x{n}:",mat)
     for i in range(m):
         for j in range(n):
             print(mat[j+n*i],end=" ")
         print()
