import os
list_64 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
           'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           '0','1','2','3','4','5','6','7','8','9',
           '+','/'
          ]
list_ASCII = [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
             ' ','!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/',
             '0','1','2','3','4','5','6','7','8','9',
             ':',';','<','=','>','?',"@",
             'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
             '[',None,     #backslash giving problems... '\\' may work.?
             ']','^','_','`',
             'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
             '{','|','}','~',None
             ]

def decrypt(L):
    List = []
    List += L
    IKYRL = ''
    C = 0
    while List[-1] == '=':
        List.pop()
        C += 2
    for x in range(len(List)):
        for a in range(6-len("{0:b}".format(list_64.index(List[x])))):
            IKYRL += '0'
        IKYRL += str("{0:b}".format(list_64.index(List[x])))
    List = []
    List += IKYRL
    IKYRL = ''
    for a in range(C):
        List.pop()       
    for b in range(len(List)):
        IKYRL += List[b]

    List = []
    for c in range(int(len(IKYRL)/8)):
        List.append(IKYRL[8*c:8*(c+1)])
    L = ''
    for d in range(len(List)):
        L += list_ASCII[int(List[d], 2)]
    List = []
    List += L
    while List[-1] == ' ':
        List.pop()
        C += 2
    L = ''
    for x in range(len(List)):
        L += List[x]
    List2= []
    List2 = L.split(' ')
    L = ''
    for x in range(len(List2)):
        L += list_ASCII[pow(int(List2[x]),PK,SPK)]

    f= open("C:/Users/IN3LABS/Desktop/Lessons and Curriculum/Python.luke/CRYP/DecryptedMessage.txt","w+")
    f.write(L)
    f.close()

path = 'C:/Users/IN3LABS/Desktop/Lessons and Curriculum/Python.luke/Encoder and Decoder/Key Generator/EncryptKey.txt'
D = open(path,"r")
keylist = []
F = D.read()
keylist = F.split('\n')

SPK = int(keylist[0])
PK = int(keylist[2])
path2 = 'C:/Users/IN3LABS/Desktop/Lessons and Curriculum/Python.luke/CRYP/Paste encryted text file here/EncryptedMessage.txt'
G = open(path2,"r")
L = G.read()
decrypt(L)

os.remove("C:/Users/IN3LABS/Desktop/Lessons and Curriculum/Python.luke/CRYP/Paste encryted text file here/EncryptedMessage.txt")
quit()
