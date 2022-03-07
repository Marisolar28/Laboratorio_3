#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Problema 1
numero= int(input("Ingrese el numero:  ")) #ingrese el numero que quiere convertir a binario
print(format(numero, "0b"))

        


# In[22]:


#*Problema 2*
#crear una funcion para comprobar si un numero dado es primo
def es_primo(numero):
    if numero == 1:
        return False
    elif numero == 2:
        return True
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return False
        return True
numero=int(input("Ingresa un numero: "))
primo=es_primo(numero)
print("¿El numero ingresado es numero primo?", primo)


# In[4]:


#Problema 3
import math
question=int(input("Escribe la cantidad de numeros que introduciras:"))
funcion=[]
for i in range(question):
     funcion.append(int(input("Escribe los numeros a introducir:")))
var=0
for i in funcion:
    mean=sum(funcion)/len(funcion)
    var +=((i-mean)**2)/len(funcion)
stdeV= math.sqrt(var)
print("\nLa media de los datos es:",mean)
print("\nLa varianza:",var)
print("\nLa desviacion estandar de los datos es:",stdeV)
#print(mean)
#print(var)
             


# In[ ]:


#Problema 4
def ordenamiento_burbuja(lista): #Funcion ordenamiento burbuja
    for y in range (len(lista) -1,0,-1):
        for i in range(y):
            if lista [i] > lista[i +1]:
                temp= lista[i]
                lista[i]= lista[i+1]
                lista[i+1]= temp
    return(lista)

def main (): #Funcion Main
    size=int(input("Digite el tamaño de la lista:"))
    x=0
    values=[]
    while x < size:
        lista=int(input("Ingrese los numeros de la lista: "))
        values.append(lista)
        x= x + 1
    return values
ordenamiento_burbuja(main()) #Comprobacion de ordenamiento burbuja

            
        


# In[ ]:


#Problema #5
tupla = (10,20,40,5,70)
string_concat= ""
for i in tupla:
    string_concat= string_concat+str(i)
print (string_concat)


# In[ ]:


#Problema #6
tupla= [(), (), ('X',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
tupla= [t for t in tupla if t]
print (tupla)


# In[19]:


#problema 7
def mean_tupla (tupla_mean):
    e = 0
    mean = []
    while e < len(tupla_mean):
        mean.append(sum(tupla_mean[e]) / len(tupla_mean[e]))
        resultado = tuple(mean)
        e = e + 1
    return resultado


# In[20]:


tuplas_7= ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32))
mean_tupla(tuplas_7)


# In[ ]:




