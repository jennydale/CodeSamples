def find_consecutive_runs(ints, runLength=3):
    """
    Given list of integers, find in that list all runs of runLength consecutive
    numbers that increase or decrease by 1. Return the indices of the first
    element of each run. If there are no consecutive runs, return None.
    """
    if len(ints) < runLength:
        return None
        
    runStartIndices = []
    possibleStartIndices = range(len(ints)-runLength+1)
    
    for i in possibleStartIndices:
        chunk = ints[i:i+runLength]
        upRun = range(ints[i], ints[i]+runLength)
        downRun = range(ints[i], ints[i]-runLength, -1)
        if (chunk == upRun or chunk == downRun):
            runStartIndices.append(i)
        
    return runStartIndices if runStartIndices else None
    
    

# TESTING
if __name__ == '__main__':
    
    # (runLength, inputList, expectedOutput)
    testCases = ((3, [1, 2], None),
                 (3, [1, 2, 'a'], None),
                 (3, [1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7, 8, 7], [0, 4, 6, 7]),
                 (3, [-1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7, 8, 7], [4, 6, 7]),
                 (3, [-1, 2, 3, 5, -10, -9, -8, 9, 10, 11, 9, 8, 7], [4, 7, 10]),
                 (3, [3, 2, 1, 5, 11, 10, 9, 8, 9, 10, 11, 7], [0, 4, 5, 7, 8]),
                 (3, [8, 9, 10, 11, 7, 12, 13, 15, 16, 17, 3, 2, 1], [0, 1, 7, 10]),
                 (4, [8, 9, 10, 11, 7, 12, 13, 15, 16, 17, 3, 2, 1], [0]),
                 (5, [8, 9, 10, 11, 7, 12, 13, 15, 16, 17, 3, 2, 1], None),
                 (2, [8, 9, 10, 11, 7, 12, 13, 15, 16, 17, 3, 2, 1], [0, 1, 2, 5, 7, 8, 10, 11])
                )
    
    for runLength, test, output in testCases:
        print("find_consecutive_runs(%r, runLength=%d) = %r" % (test, runLength, output))
        assert(find_consecutive_runs(test, runLength) == output)

