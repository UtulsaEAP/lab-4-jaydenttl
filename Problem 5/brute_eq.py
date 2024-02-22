"""
Complete the python code to find the solution to the system of linear equations entered by the user. 
The equations are of the form ax + by = c and dx + ey = f. The solution should be printed in the form x = # and y = #. 
If there is no solution, print "There is no solution".

Name:Jayden Ly
Lab Time: thurs 4:50
"""

def brute_eq():
    #Read in first equation, ax + by = c 
    a = int(input())
    b = int(input())
    c = int(input())

    #Read in second equation, dx + ey = f
    d = int(input())
    e = int(input())
    f = int(input())

    solution = False
    
    for i in range (-10,10):
        for j in range (-10, 10):
            if (a * i + b * j == c) and (d * i + e * j == f):
                solution = True
                first = i
                second = j
                
    if solution == False:
        print('There is no solution')
    elif solution == True:
        print('x = ' + str(first) + ' , y = '+str(second))

                #if solution == True:
                #    print('x = ' + str(i) + ' , y = '+str(j))
                #elif solution == False:
                #    print('There is no solution')
    

    

    
if __name__ == "__main__":
    brute_eq()