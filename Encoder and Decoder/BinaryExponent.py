print('For A to the power of P')
A = int(input('A?\n>'))
P = int(input('P?\n>'))
binary = "{0:b}".format(P)
List = []
List += binary
while int(List[0]) == 0:
    List.pop(0)
N = A
List.pop(0)
for x in range(len(List)):
    if int(List[x]) == 1:
        N **= 2
        N *= A
    else:
        N **= 2
print(N)
