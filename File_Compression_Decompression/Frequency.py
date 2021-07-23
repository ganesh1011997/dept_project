def frequencyTable(fname):
    fp=open(fname,'r')
    rec=fp.read()
    freq={}
    for i in rec:
        if i not in freq.keys():
            freq[i]=0
        freq[i]+=1
    return freq
