
def binData(arr, binSize):

    sample = []
    binnedData = []
    copyArr = [x for x in arr]

    while len(copyArr) > 0:

        for i in range(binSize):
            if len(copyArr) > 0:
                sample.append(copyArr.pop())

        avg = sum(sample)/len(sample)
        print(sample, avg)
        
        for i in range(len(sample)):
            binnedData.append(avg)

        sample = []
            
    return binnedData[::-1]

print(binData([1,2,3,5,5,5], 3))
        
