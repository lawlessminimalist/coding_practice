"""
Description:
Bigger is greater

string input
task: return a bigger string

returned word must be larger than the original
must be smallest word that meets the first condition

conditons/operations allowed?


Input: 
abcd
bb
hefg
dhck
abcdd
abcdd

Output:
abdc
None
hegf
dhkc
abdcd
abddc

"""


def biggerIsGreater(w):
    swapChar1:str = input[len(input)-1]

    min_value = 100000000000000000
    min_string = None
    
    for idx in range(len(input)-1,0,-1):
        if input[idx-1] == swapChar1:
            continue

        swapped_string =  input[0:idx-1] + swapChar1 + input[idx:len(input)-1] + input[idx-1]
        value = calcValueString(swapped_string)

        if value < min_value:
            min_value = value
            min_string = swapped_string
    
    return min_string
        

def calcValueString(input:str):
    base = ord("a") - 1
    int_string = ''
    for char in input:
        int_string += str(ord(char)-base)
    return int(int_string)


print(biggerIsGreater('abdc'))

1,2,4,3
1,2,3,4

1,3,2,4
abcd
# acbd