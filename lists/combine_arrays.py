'''
    Write a function named combine_lists that takes two lists of strings and
    combines them into a single list.

    Example:
        Input: ["a", "b"], ["c", "d"]
        Output: ["a", "b", "c", "d"]
'''

def main():
    list1 = ["a", "b"]
    list2 = ["c", "d"]
    print(combine_lists(list1,list2))

def combine_lists(list1, list2):
    # return list1 + list2  # -> doesn't change the list1
    # or
    list1.extend(list2)     # -> changes the list1
    return list1



if __name__ == '__main__':
    main()
