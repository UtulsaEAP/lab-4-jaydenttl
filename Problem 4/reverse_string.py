"""
Complete the following python code to reverse the string entered by the user.

Name: Jayden Ly
Lab Time: thursday 2:52
"""

def reverse_string():
    while True:
        og_string = input()
        if og_string.lower() in ['d','done']:
            break

        reversed_string = og_string[::-1]
        print(reversed_string)
    
    pass
if __name__ == "__main__":
    reverse_string()