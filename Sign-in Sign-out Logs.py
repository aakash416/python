'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
logs = ["99 1 sign-in", "100 10 sign-in", "50 20 sign-in",
        "100 15 sign-out", "50 26 sign-out", "99 2 sign-out"]
Max = 5
for i in range(len(logs)):
    logs[i] = logs[i].split()
r = []
for i in range(len(logs)):
    for j in range(1, len(logs)):
        if logs[i][0] == logs[j][0]:
            if int(logs[j][1])-int(logs[i][1]) > 0:
                r.append(logs[i][0])
                r.append(int(logs[j][1])-int(logs[i][1]))
for i in range(1, len(r), 2):
    if r[i] <= 5:
        print(r[i-1])
    else:
        r.pop(i)
        r.pop(i-1)
