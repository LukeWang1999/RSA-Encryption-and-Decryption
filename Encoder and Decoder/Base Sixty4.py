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
def encode(L):
    List = []
    List += L
    IKYRL = ''
    for x in range(len(List)):
        for a in range(8-len("{0:b}".format(list_ASCII.index(List[x])))):
            IKYRL += '0'
        IKYRL += str("{0:b}".format(list_ASCII.index(List[x])))
    List = []
    for x in range(int((len(IKYRL)/6))):
        List.append(IKYRL[6*x:6*(x+1)])
    if len(IKYRL)%6 != 0:
        List.append(IKYRL[len(IKYRL)-(len(IKYRL)%6)::1])
    L = ''
    for x in range(len(List)):
        if len(List[x]) == 6:
            L += list_64[int(List[x], 2)]
        else:
            H = 6-len(List[x])
            for y in range(6-len(List[x])):
                List[x] += '0'
            L += list_64[int(List[x], 2)]
            if H == 2:
                L += '='
            elif H == 4:
                L += '=='
    print(L)
def decode(L):
    List = []
    List += L
    IKYRL = ''
    C = 0
    Hello = ''
    while List[-1] == '=':
        List.pop()
        C += 2
    for x in range(len(List)):
        for a in range(6-len("{0:b}".format(list_64.index(List[x])))):
            IKYRL += '0'
        IKYRL += str("{0:b}".format(list_64.index(List[x])))
    List = []
    List += IKYRL
    for a in range(C):
        List.pop()       
    for b in range(len(List)):
        Hello += List[b]
    List = []
    for c in range(int(len(Hello)/8)):
        List.append(Hello[8*c:8*(c+1)])
    L = ''
    for d in range(len(List)):
        L += list_ASCII[int(List[d], 2)]
    print(L)
while True:
    while True:
        try:
            code = int(input('Do you want to encode(1) or decode(0)?\n>'))
            break
        except:
            print('Please choose available option!')
    if code == 1:  
        L = input('What do you want to encode?\n>')
        encode(L)
    else:
        L = input('What do you want to decode?\n>')
        decode(L)
