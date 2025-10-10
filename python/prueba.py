import random
numero= random.randint(1,10)

print ("averigua cual es el numero secreto")


while True:

   prueba= int(input("esribe numero "))



   
   if prueba > numero:
    print ("numero escogido es mas elevado")

   elif prueba < numero:
     print ("el numero escogido es mas bajo")

   else:
     print("enhorabuena")
     break
   

   
