'''
Write a function named append_pos_sum that processes a list of integers.

Requirements:
1. Parameters: Takes one parameter: a list of integers.
2. Logic:
    Create a new list.
    Add only the positive integers from the input list to the new list.
    Calculate the sum of these positive integers.
    Append this sum as the last element of the new list.
3. Constraint: The original list must remain unchanged.

Example:
    Input: [4, -6, 3, -8, 0, 4, 3]
    Output: [4, 3, 4, 3, 14] (where 14 is the sum of 4+3+4+3)
'''

def main():
    input_list = [4, -6, 3, -7, 6, -8, 0, 4, 3]
    print(append_pos_sum(input_list))


def append_pos_sum(input_list):
    # 1st way:
    new_list = [i for i in input_list if i > 0]
    new_list.append(sum(new_list))
    return new_list

    # 2nd way:
    # sum = 0
    # output = []
    # for i in input_list:
    #     if i > 0:
    #        output.append(i)
    #        sum += i
    #
    # output.append(sum)
    # return output


if __name__ == '__main__':
    main()
