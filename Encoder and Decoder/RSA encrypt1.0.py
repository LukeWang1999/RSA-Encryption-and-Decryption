

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
def encrypt(L):
    List = []
    Message = ''
    List += L
    for x in range(len(List)):
        Message += str(list_ASCII.index(List[x]) ** UPK % SPK)
        Message += ' '
    List2=[]
    List2 += Message
    IKYRL = ''
    for x in range(len(List2)):
        for a in range(8-len("{0:b}".format(list_ASCII.index(List2[x])))):
            IKYRL += '0'
        IKYRL += str("{0:b}".format(list_ASCII.index(List2[x])))
    List2 = []
    for x in range(int((len(IKYRL)/6))):
        List2.append(IKYRL[6*x:6*(x+1)])
    if len(IKYRL)%6 != 0:
        List2.append(IKYRL[len(IKYRL)-(len(IKYRL)%6)::1])
    L = ''
    for x in range(len(List2)):
        if len(List2[x]) == 6:
            L += list_64[int(List2[x], 2)]
        else:
            H = 6-len(List2[x])
            for y in range(6-len(List2[x])):
                List2[x] += '0'
            L += list_64[int(List2[x], 2)]
            if H == 2:
                L += '='
            elif H == 4:
                L += '=='
    print(L)

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
##    for x in range(len(List2)):
##        List2.pop(List2.index(''))
    L = ''
    for x in range(len(List2)):
        L += list_ASCII[int(List2[x]) ** PK % SPK]
    print(L)

while True:
    while True:
        try:
            code = int(input('Do you want to encrypt(1) or decypt(0)?\n>'))
            break
        except:
            print('Please choose available option!')                
    if code == 1:
        while True:
            try:
                SPK = int(input('What is shared public key?\n>'))
                UPK = int(input('What is unshared public key?\n>'))
                break
            except:
                print('Please type integers!')
                
        L = input('What do you want to encrypt?\n>')
        encrypt(L)
    else:
        while True:
            try:
                PK = int(input('What is private key?\n>'))
                SPK = int(input('What is shared public key?\n>'))
                break
            except:
                print('Please type integers!')

        L = input('What do you want to decrypt?\n>')
        decrypt(L)
