"""
Complete the following python code to print all numbers between the two values incrementing by 5 from the initial value to the final value. The initial value and final value are entered by the user. If the final value is less than the initial value, print "Second integer can't be less than the first.

Name:
Lab Time:
"""

def inc_5():
    first = int(input())
    second = int(input())
    new = ''
    if first > second:
        print("Second integer can't be less than the first.")
    else:
        while first <= second:
            new = str(new)+' '+str(first)
            first = first + 5
            
        print(new)



if __name__ == '__main__':
    inc_5()