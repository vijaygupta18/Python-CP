def subsequence(str1):
        if (len(str1)==0):
            return [""]
        small = subsequence(str1[1:len(str1)])
        result = [" "]* (2* len(small))
        k=0
        for i in range(len(small)):
            result[k]=small[i]
            k=k+1
        for i in range(len(small)):
            result[k]=str1[0]+small[i]
            k=k+1
        return result
