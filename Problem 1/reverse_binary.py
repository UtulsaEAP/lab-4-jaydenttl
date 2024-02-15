"""
Complete the following python code to print the reverse binary representation of positive integer number entered by the user.

Name: Jayden Ly
Lab Time: 2:19

Write a program that takes in a positive integer as input, and outputs a string of 1's and 0's representing the integer in reverse binary. For an integer x, the algorithm is:

    As long as x is greater than 0
    Output x modulo 2 (remainder is either 0 or 1)
    Assign x with x divided by 2

Note: The above algorithm outputs the 0's and 1's in reverse order.

Ex: If the input is:

    6

the output is:

    011

6 in binary is 110; the algorithm outputs the bits in reverse.

"""


def reverse_binary():
    user_num = int(input())
    new = ''
    x = user_num

    while x > 0:
        new += str(x % 2)
        x = x // 2
 

    print(new)
if __name__ == "__main__":
    reverse_binary()