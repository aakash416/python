'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def disk(my_list, max_split):
    final_list = max([min(my_list[i:i + max_split])
                     for i in range(0, len(my_list)-1)])
    return final_list


my_list = [2, 5, 6, 7, 8, 15, 34, 56, 78]
max_split = 2
print(disk(my_list, max_split))
