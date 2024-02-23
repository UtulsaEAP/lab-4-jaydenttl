"""
Complete the following python code to take in a list of values from the user and then normalize them

Name: Jayden Ly
Lab Time: thursday 6:13
"""


def norm():
    first_integer = int(input('integer amount of values:'))
    float_list = []
    for i in range(first_integer):
        float_inputs = float(input())
        float_list.append(float_inputs)             #appends(attach to end) the float inputs to blank list

    the_largest_val = max(float_list)

    for float_inputs in float_list:
        divided_list = float_inputs * (1 / the_largest_val)
        print(f'{divided_list:.2f}')

if __name__ == "__main__":
    norm()
