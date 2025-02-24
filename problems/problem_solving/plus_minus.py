def plusMinus(arr):
    pos,neg,neut = 0.0,0.0,0.0

    for item in arr:
        if item > 0:
            pos+=1
        elif item < 0:
            neg+=1
        elif item == 0:
            neut+=1
    pos = pos / len(arr)
    neg = neg / len(arr)
    neut = neut / len(arr)
    for item in [pos,neg,neut]:
        print('{:.4f}'.format(item))
   

plusMinus([0,1,2,-3,2,-3])