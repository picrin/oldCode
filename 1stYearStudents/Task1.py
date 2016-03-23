def get_resp():
    res = open("Responses.txt.txt","r")
    resp = res.read()
    respon = resp.split()
    respon = respon + [0,0,0]
    return respon

que = open("QuestionInfo.txt.txt","r")
ques = que.read()
questi = ques.split()

first = {}
second = {}
third = {}
i = 0
count1 = 0
count2 = 0
count3 = 0
ID1 = []
ID2 = []
ID3 = []

respon = get_resp()
first = {}
ID1 = []
count1 = 0
while i<len(respon)-3:
    if int(respon[i])==1:
        if int(respon[i+1]) not in ID1:
            count1+=1
            ID1 = ID1 + [int(respon[i+1])]
        if int(respon[i+1]) in ID1:
            j = int(respon[i+1])
            k = 0
            while k<len(ID1):
                if ID1[k]==j:
                    count1=len(ID1[0:k+1])
                    break
                k = k + 1
        first.update({count1:{"ID":int(respon[i+1]),"response":int(respon[i+2])}})        
    i = i + 3  





    
while i<len(respon)-3:
    if int(respon[i])==1:
        if int(respon[i+1]) not in ID1:
            count1+=1
            ID1 = ID1 + [int(respon[i+1])]
        if int(respon[i+1]) in ID1:
            j = int(respon[i+1])
            k = 0
            while k<len(ID1):
                if ID1[k]==j:
                    count1=len(ID1[0:k+1])
                    break
                k = k + 1
        first.update({count1:{"ID":int(respon[i+1]),"response":int(respon[i+2])}})
    if int(respon[i])==2:
        if int(respon[i+1]) not in ID2:
            count2+=1
            ID2 = ID2 + [int(respon[i+1])]        
        second.update({count2:{"ID":int(respon[i+1]),"response":int(respon[i+2])}})
    if int(respon[i])==3:
        if int(respon[i+1]) not in ID3:
            count3+=1
            ID3 = ID3 + [int(respon[i+1])]        
        third.update({count3:{"ID":int(respon[i+1]),"response":int(respon[i+2])}})
    i = i + 3

br1 = questi[0]
br2 = questi[2]
br3 = questi[4]

value1 = first.values()
value2 = second.values()
value3 = third.values()
resp1 = [[1,0],[2,0],[3,0],[4,0],[5,0]]
resp2 = [[1,0],[2,0],[3,0]]
resp3 = [[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[10,0]]
respon1 = []
respon2 = []
respon3 = []
i = 0
def response1(first):
    value1 = first.values()
    resp1 = [[1,0],[2,0],[3,0],[4,0],[5,0]]
    respon1 = []
    i = 0
    while i<len(value1):
        value = value1[i].values()
        respon1 = respon1 + [value[1]]
        i = i + 1   
    for item in respon1:
        if item == 1:
            resp1[0][1] = resp1[0][1] + 1
        if item == 2:
            resp1[1][1] = resp1[1][1] + 1
        if item == 3:
            resp1[2][1] = resp1[2][1] + 1
        if item == 4:
           resp1[3][1] = resp1[3][1] + 1
        if item == 5:
           resp1[4][1] = resp1[4][1] + 1
    print resp1       
    
i = 0
while i<len(value2):
    value = value2[i].values()
    respon2 = respon2 + [value[1]]
    for item in respon2:
        if item == 1:
            resp2[0][1] = resp2[0][1] + 1
        if item == 2:
            resp2[1][1] = resp2[1][1] + 1
        if item == 3:
            resp2[2][1] = resp2[2][1] + 1
    i = i + 1
i = 0    
while i<len(value3):
    value = value3[i].values()
    respon3 = respon3 + [value[1]]
    for item in respon3:
        if item == 1:
            resp3[0][1] = resp3[0][1] + 1
        if item == 2:
            resp3[1][1] = resp3[1][1] + 1
        if item == 3:
            resp3[2][1] = resp3[2][1] + 1
        if item == 4:
            resp3[3][1] = resp3[3][1] + 1
        if item == 5:
            resp3[4][1] = resp3[4][1] + 1
        if item == 6:
            resp3[5][1] = resp3[5][1] + 1
        if item == 7:
            resp3[6][1] = resp3[6][1] + 1
        if item == 8:
            resp3[7][1] = resp3[7][1] + 1
        if item == 9:
            resp3[8][1] = resp3[8][1] + 1
        if item == 10:
            resp3[9][1] = resp3[9][1] + 1            
    i = i + 1

response1(first)

