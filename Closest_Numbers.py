'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def pair(l):
    p = []
    mdiff = pow(10, 7)+1
    l.sort()
    for i in range(1, len(l)):
        d = abs(l[i-1]-l[i])
        if d < mdiff:
            mdiff = d
            p = [l[i-1], l[i]]
        elif d == mdiff:
            p.extend([l[i-1], l[i]])
    print(p)
    for i in range(1, len(p), 2):
        print(p[i-1], p[i])


l = [4, 2, 1, 3]
pair(l)
