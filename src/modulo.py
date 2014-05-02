#!/src/bin/python
PI=3.1415926535897931159979634685441852

def aproximacion(nro_intervalo):
  n=int (nro_intervalo)
  if(n!=0):
   suma=0
   for i in range(1,nro_intervalo+1):
     x_i=(i-0.5)/float(nro_intervalo)
     fx_i=4/(1+x_i**2)
     b=i/float(nro_intervalo)
     a=b-(1/float(nro_intervalo))
     suma=suma+fx_i
   pi=suma/float(nro_intervalo)
   return pi
   
def error(nro_intervalo,nro_test,umbral):
  incorrectos=0
  for i in range(nro_test):
    valor_pi=aproximacion(nro_intervalo)
    valor=valor_pi-PI
    if(abs(valor)>umbral):
      incorrectos=incorrectos+1
  porcentaje=(incorrectos/float(nro_test))*100
  return porcentaje

