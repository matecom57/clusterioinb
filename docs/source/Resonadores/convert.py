import sys
print (sys.argv)

def Busca_Izquiera(ss='', car='', pos=0):
  i = pos
  i1 = -1
  while  i > 0:
    if ss[i] == car:
      i1 = i+1
      i = -1
    else:
      i = i-1
  return i1

def Encuentra_http(ss=''):
  i = ss.find('http:')
  i2 = ss.find(')', i+1)
  i1 = Busca_Izquiera(ss, '(', i-1)
  print(i1, i2)
  http = ss[i1:i2]
  print(http)
  k2 = Busca_Izquiera(ss, ']', i1)-1
  k1 = Busca_Izquiera(ss, '[', k2)
  titulo = ss[k1:k2]
  print(titulo)  
  ssN = ss[:k1-1]+'`'+titulo+'<'+http+'>`_' + ss[i2+1:]
  print(ssN)  
  
 
nombre = sys.argv[1]

filin = open(nombre+'.md', 'r')
datos = filin.readlines()
filin.close

#filon = open(nombre+'.rst', 'w')

i = 0
for ss in datos:
  print(ss)
  if 'http:' in ss:
    print(str(i)+ ' - '+ss)
    Encuentra_http(ss)



