import textwrap
def Rail_encrypt(pt,d):
    pt = "".join(pt.lower().strip().split(" "))
    
    while len(pt)%d != 0:
        pt+="x"
        
    pt_blocks = textwrap.wrap(pt,d)
    #print(pt_blocks)
    
    ct = ""
    for i in range(d):
        for j in pt_blocks:
            ct += j[i]

    return(ct)
    
    
    
def Rail_decrypt(ct, d):
    ct = "".join(ct.lower().strip().split(" "))
    ct_blocks = textwrap.wrap(ct,len(ct)//d)
    
    pt = ""
    for i in range(len(ct)//d):
        for j in ct_blocks:
            pt += j[i]
    
    if pt[-1] == "x":
        x_count = 0
        for i in range(len(pt)-1,0,-1):
            if pt[i] == "x":
                x_count+=1
        pt = pt[:-(x_count)]
                
    return(pt)
