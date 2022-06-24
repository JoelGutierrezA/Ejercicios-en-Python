import numpy as np
import os

#Creación de la Matriz
fNormal=int(input('Ingrese numero de filas: '))
cNormal=int(input('Ingrese numero de columnas: '))
fVip=int(input('Ingrese numero de filas: '))
cVip=int(input('Ingrese numero de columnas: '))
aNormal=np.zeros(shape=(fNormal,cNormal), dytpe=int)
aVip=np.zeros(shape=(fVip,cVip), dtype=int)

#Precios pasajes
pAN=78900; pANdes=pAN*0.3; pAV=240000; pAVdes=pAV*0.3

#Almacenamiento de datos de clientes
nombreN=list(); rutN=list(); telefonoN=list(); bancoN=list()
pasajeroN=[nombreN, rutN, telefonoN, bancoN]
nombreV=list(); rutV=list(); telefonoV=list(); banco=list()
pasajeroV=[nombreV, rutV, telefonoV, bancoV]

#Creación del Menú