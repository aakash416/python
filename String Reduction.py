'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def subString(s, n):
    l = []
    count = 0
    for z in range(n-2):
        k = s[z:]
        for i in range(n):
            for j in range(i+1, n+1):
                l.append(k[i: j])
        if len(l) != len(set(l)):
            count += 1
            l.clear()
    return count


s = "abbabb"
print(subString(s, len(s)))
