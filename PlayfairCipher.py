def matrixgen(key):
    st = "abcdefghiklmnopqrstuvwxyz"
    key = "".join(set(key))
    for i in key:
        st = st.replace(i,"")
    matstr = key+st
    
    MAT = []
    k = 0
    for i in range(5): 
        col = [] 
        for j in range(5): 
            col.append(matstr[k]) 
            k+=1
        MAT.append(col) 

    return(MAT, matstr)

def mapper(matstr):
    mapp = {
        "0": [0,0],
        "1": [0,1],
        "2": [0,2],
        "3": [0,3],
        "4": [0,4],
        "5": [1,0],
        "6": [1,1],
        "7": [1,2],
        "8": [1,3],
        "9": [1,4],
        "10": [2,0],
        "11": [2,1],
        "12": [2,2],
        "13": [2,3],
        "14": [2,4],
        "15": [3,0],
        "16": [3,1],
        "17": [3,2],
        "18": [3,3],
        "19": [3,4],
        "20": [4,0],
        "21": [4,1],
        "22": [4,2],
        "23": [4,3],
        "24": [4,4]
    }
    
    for i in range(len(matstr)):
        mapp[matstr[i]] = mapp.pop(str(i))
        
    return(mapp)

def PThandler(pt):
    pt = "".join(pt.split(" "))
    PT = pt[0]
    for i in range(1,len(pt)):
        if PT[i-1] == pt[i]:
            PT += "x"+ pt[i]
        else:
            PT += pt[i]
    if( len(PT)%2 == 1):
        PT += "x"
    PT2 = textwrap.wrap(PT,2)
    return(PT)

def CThandler(ct):
    PT = ct[0]
    for i in range(1,len(ct)-1):
        print(ct[i])
        if ct[i-1] == ct[i+1]:
            #print(ct[i+1])
            PT += ct[i+1]
        else:
            #print(ct[i])
            PT += ct[i]
    PT += ct[-1]
    return(PT)
    
    
    
def PLAYFAIR_encrypt(key, pt):
    
    MAT, matstr = matrixgen(key)
    mapp = mapper(matstr)
    PT = PThandler(pt)
    print(PT)
    CT = ""
    for i in range(0,len(PT),2):
        X = mapp[str(PT[i])]
        Y = mapp[str(PT[i+1])]

        #SAME ROW
        if X[0] == Y[0]:
            CT += MAT[X[0]][(X[1]+1)%5]
            CT += MAT[Y[0]][(Y[1]+1)%5]
            
        #SAME COLUMN
        elif X[1] == Y[1]:
            CT += MAT[(X[0]+1)%5][X[1]]
            CT += MAT[(Y[0]+1)%5][Y[1]]
    
        #NONE
        else:
            CT += MAT[(X[0])%5][(Y[1])%5]
            CT += MAT[(Y[0])%5][(X[1])%5]

    return(CT)
    
    
def PLAYFAIR_decrypt(key,CT):
    
    MAT, matstr = matrixgen(key)
    mapp = mapper(matstr)
    
    PT = ""
    for i in range(0,len(CT),2):
        X = mapp[str(CT[i])]
        Y = mapp[str(CT[i+1])]

        #SAME ROW
        if X[0] == Y[0]:
            PT += MAT[X[0]][(X[1]-1)%5]
            PT += MAT[Y[0]][(Y[1]-1)%5]
            
        #SAME COLUMN
        elif X[1] == Y[1]:
            PT += MAT[(X[0]-1)%5][X[1]]
            PT += MAT[(Y[0]-1)%5][Y[1]]
    
        #NONE
        else:
            PT += MAT[(X[0])%5][(Y[1])%5]
            PT += MAT[(Y[0])%5][(X[1])%5]

    print(PT)
    PT = CThandler(PT)
    return(PT)
