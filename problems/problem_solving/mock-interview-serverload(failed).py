"""
 Input = array of server loads for server i located at index i 
 
 Task = perform swaps at a cost of 1min in order to group 
 all servers with a state of 1 (under heavy load)

 Output = the minimum cost in mins for grouping these servers

"""


input = [1, 0, 1, 0, 1, 0, 1, 0 ]
def getMinimumMinutes(serverLoad):
    total_cost = 0
    left_point = 0
    right_point = len(serverLoad)-1
    left_fill = right_fill = 0
    while(left_point<=right_point):
        left = serverLoad[left_point]
        right = serverLoad[right_point]
        if left == 1:
            # check if left push < right push
            left_cost = left_point - left_fill
            right_cost = (len(serverLoad)-1)-left_point-right_fill
            if left_cost < right_cost:
                if left_cost == 0:
                    left_fill +=1
                else:
                    left_fill +=1
                    total_cost +=1
            else:
                if right_cost == 0:
                    right_fill +=1
                else:
                    right_fill +=1
                    total_cost +=1
            left_point +=1
        if right == 1:
            # check if left push < right push
            left_cost = right_point - left_fill
            right_cost = (len(serverLoad)-1)-right_point-right_fill
            if left_cost < right_cost:
                if left_cost == 0:
                    left_fill +=1
                else:
                    left_fill +=1
                    total_cost +=1
            else:
                if right_cost == 0:
                    right_fill +=1
                else:
                    right_fill +=1
                    total_cost +=1
        right_point -=1
            
       
    return total_cost

print(getMinimumMinutes(input))