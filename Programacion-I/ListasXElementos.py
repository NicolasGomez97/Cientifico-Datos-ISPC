#importo libreria de para la letras de la lista
import string
var=[]
#var2=[]
dic = dict()
#Ingresamos que el limite de la lista
l = int(input("ingrese el limite  de la lista: \n"))
# Uso el for para recorrer las catidad de lista de terminada por el usuario
for i in string.ascii_lowercase[:l]:
    dic[i]=var
    var.clear()
    for q in range(5):
        #For para recorrer los 10 elementos
        #var2.append(i)
        print("ingrese el",q,"° numero de la lista",i,":")
        var.insert(q, input("Ingrese:"))
        print(var)
    print(dic)
#print(var2)
#for i in string.ascii_lowercase[:l]:
    #for q in range(l*5):
        #dic[i]=var[q]
print(dic)
while True:
    v = int(input("Que numero vas a querer hacer la suma y sacar la media: \n"))
    print("tenes hasta el",i)
    res = 0
    for q in range(1,l+1):
        for i in string.ascii_lowercase[:l]:
            if q == v: 
                res += dic.get(i)
    print(float(res/l))
    print("Quiere continuar:")
    v = input("").upper()
    print(v)
    if v == 'SI':
        res =0
        continue       
    else:
        break