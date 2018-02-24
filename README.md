# RSA-Encryption-and-Decryption
#Uses the RSA algorithm to encrypt text strings.

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
        A = list_ASCII.index(List[x])      
        Message += str(pow(A,UPK,SPK))
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
    f= open("EncryptedMessage.txt","w+")
    f.write(L)
    f.close()
path = 'C:/your_dir_path/text.txt'
path2 = 'C:/your_dir_path/text.txt'
D = open(path,"r")
S = open(path2,"r")
L = S.read()
keylist = []
F = D.read()
keylist = F.split('\n')
UPK = int(keylist[1])
SPK = int(keylist[0])
encrypt(L)
quit()
