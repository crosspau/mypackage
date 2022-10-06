def top_n (items, n):
    '''Return the top n items in an array in decending order

    Args:
        items(array): list or array -like object
        n (int): number of items to return
    Return:
        array: top n items, in desc order
        
    Egs:
        >>>top_n([8,3,2,7,4] ,3)
        [8,7,3]
        '''

    for i in range(n):
        for j in range(len(items)-i-1):
            if items[j]>[j+1]:
                items[j], items [j+1] = items [j+1], items[j]

    top_n = items[-n]

    return top_n [::-1]
