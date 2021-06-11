'''
Proyecto 3
Taller de programacion
Grupo 05
Melany Salas Fernandez
2021121147
'''
#-----------------------------------Modulos---------------------------
import tkinter as tk
import random as ran
import time

#----------------------------------Funciones--------------------------

'''
Funcion para crear la ventana de juego
'''
def a_jugar():
    global numero
    global nivel_dificultad
    global lado_num
    global f0c0
    global f0c1
    global f0c2
    global f0c3
    global f0c4
    global f1c0
    global f1c1
    global f1c2
    global f1c3
    global f1c4
    global f2c0
    global f2c1
    global f2c2
    global f2c3
    global f2c4
    global f3c0
    global f3c1
    global f3c2
    global f3c3
    global f3c4
    global f4c0
    global f4c1
    global f4c2
    global f4c3
    global f4c4
    
    
    
    ventana_principal.state(newstate="withdraw")
    ventana_a_jugar= tk.Tk()
    ventana_a_jugar.geometry("600x600")
    ventana_a_jugar.title("FUTOSHIKI- A jugar")
    ventana_a_jugar.config(bg="#F4D6CC")
    numero= tk.IntVar

    if lado_num == 0: #Derecha
        b1= tk.Button(ventana_a_jugar, text= "1", width= 5, bg="#F4CFB1", command=lambda:asigna_value(1)).grid(row=2, column=0)

        b2= tk.Button(ventana_a_jugar, text= "2", width= 5, bg="#F4CFB1", command=lambda:asigna_value(2)).grid(row=4, column=0)

        b3= tk.Button(ventana_a_jugar, text= "3", width= 5, bg="#F4CFB1", command=lambda:asigna_value(3)).grid(row=6, column=0)

        b4= tk.Button(ventana_a_jugar, text= "4", width= 5, bg="#F4CFB1", command=lambda:asigna_value(4)).grid(row=8, column=0)

        b5= tk.Button(ventana_a_jugar, text= "5", width= 5, bg="#F4CFB1", command=lambda:asigna_value(5)).grid(row=10, column=0)
        
    else:
        b1= tk.Button(ventana_a_jugar, text= "1", width= 5, bg="#F4CFB1").grid(row=2, column=20)

        b2= tk.Button(ventana_a_jugar, text= "2", width= 5, bg="#F4CFB1").grid(row=4, column=20)

        b3= tk.Button(ventana_a_jugar, text= "3", width= 5, bg="#F4CFB1").grid(row=6, column=20)

        b4= tk.Button(ventana_a_jugar, text= "4", width= 5, bg="#F4CFB1").grid(row=8, column=20)

        b5= tk.Button(ventana_a_jugar, text= "5", width= 5, bg="#F4CFB1").grid(row=10, column=20)
        
    f0c0=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860", command=lambda:asigna_casilla(0)).grid(row=2, column=1)
    f0c1=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860", command=lambda:asigna_casilla(1)).grid(row=4, column=1)
    f0c2=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860", command=lambda:asigna_casilla(2)).grid(row=6, column=1)
    f0c3=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(3)).grid(row=8, column=1)
    f0c4=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(4)).grid(row=10, column=1)

    f1c0=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(5)).grid(row=2, column=3)
    f1c1=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(6)).grid(row=4, column=3)
    f1c2=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(7)).grid(row=6, column=3)
    f1c3=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(8)).grid(row=8, column=3)
    f1c4=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(9)).grid(row=10, column=3)

    f2c0=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(10)).grid(row=2, column=5)
    f2c1=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(11)).grid(row=4, column=5)
    f2c2=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(12)).grid(row=6, column=5)
    f2c3=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(13)).grid(row=8, column=5)
    f2c4=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(14)).grid(row=10, column=5)

    f3c0=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(15)).grid(row=2, column=7)
    f3c1=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(16)).grid(row=4, column=7)
    f3c2=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(17)).grid(row=6, column=7)
    f3c3=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(18)).grid(row=8, column=7)
    f3c4=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(19)).grid(row=10, column=7)

    f4c0=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(20)).grid(row=2, column=9)
    f4c1=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(21)).grid(row=4, column=9)
    f4c2=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(22)).grid(row=6, column=9)
    f4c3=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(23)).grid(row=8, column=9)
    f4c4=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(24)).grid(row=10, column=9)

    
        
        
    

   # name_label= tk.Label(ventana_a_jugar, text= "FUTOSHIKI", font= "Corbel 22 bold", height= 1, width= 15, bg= "#C83E4D")
   # name_label.place(relx = -2, rely = 0.5)

def asigna_value(boton):
    global numero
    if boton == 1:
        numero=1
        print(numero)
    elif boton == 2:
        numero=2
        print(numero)
    elif boton == 3:
        numero=3
        print(numero)
    elif boton == 4:
        numero=4
        print(numero)
    elif boton == 5:
        numero=5
        print(numero)
    return
def asigna_casilla(cod):
    global numero
    global f0c0
    global f0c1
    global f0c2
    global f0c3
    global f0c4
    
    global f1c0
    global f1c1
    global f1c2
    global f1c3
    global f1c4
    
    global f2c0
    global f2c1
    global f2c2
    global f2c3
    global f2c4
    
    global f3c0
    global f3c1
    global f3c2
    global f3c3
    global f3c4
    
    global f4c0
    global f4c1
    global f4c2
    global f4c3
    global f4c4
    if cod == 0:
        f0c0.config(text=numero)
        
    elif cod == 1:
        f0c1.config(text=numero)
        
    elif cod == 2:
        f0c2.config(text=numero)
        
    elif cod == 3:
        f0c3.config(text=numero)
    elif cod == 4:
        f0c4.config(text=numero)
        
    elif cod == 5:
        f1c0.config(text=numero)
        
    elif cod == 6:
        f1c1.config(text=numero)
        
    elif cod == 7:
        f1c2.config(text=numero)
        
    elif cod == 8:
        f1c3.config(text=numero)
        
    elif cod == 9:
        f1c4.config(text=numero)
        
    elif cod == 10:
        f2c0.config(text=numero)
    elif cod == 11:
        f2c1.config(text=numero)
    elif cod == 12:
        f2c2.config(text=numero)
    elif cod == 13:
        f2c3.config(text=numero)
    elif cod == 14:
        f2c4.config(text=numero)
        
    elif cod == 15:
        f3c0.config(text=numero)
    elif cod == 16:
        f3c1.config(text=numero)
    elif cod == 17:
        f3c2.config(text=numero)
    elif cod == 18:
        f3c3.config(text=numero)
    elif cod == 19:
        f3c4.config(text=numero)
        
    elif cod == 20:
        f4c0.config(text=numero)
    elif cod == 21:
        f4c1.config(text=numero)
    elif cod == 22:
        f4c2.config(text=numero)
    elif cod == 23:
        f4c3.config(text=numero)
    elif cod == 24:
        f4c0.config(text=numero)
    
def prueba():
    global nivel_dificultad
    s= nivel_dificultad.get()
    print(s)
'''
Funcion para crear la ventana de configuracion
'''
def configuracion():
    global nivel_dificultad
    ventana_principal.state(newstate="withdraw")
    ventana_configuracion= tk.Tk()
    ventana_configuracion.geometry("600x600")
    ventana_configuracion.title("FUTOSHIKI- A jugar")
    ventana_configuracion.config(bg="#F4D6CC")

    name_label= tk.Label(ventana_configuracion, text= "FUTOSHIKI", font= "Corbel 22 bold", height= 1, width= 15, bg= "#C83E4D")
    name_label.grid(row=0, column=1)

    nivel_label= tk.Label(ventana_configuracion, text= "1. Nivel", font= "Corbel 12 bold", width= 8, bg= "#F4D6CC")
    nivel_label.grid(row=2, column=0)


    #Radiosbutton
    nivel_dificultad= tk.IntVar()
    
    
    facil_rb= tk.Radiobutton(ventana_configuracion, text= "Facil",font= "Corbel 12", width= 8,\
                             bg= "#F4D6CC",variable= nivel_dificultad , value=1, command= prueba)
    facil_rb.grid(row=2, column=1)

    intermedio_rb= tk.Radiobutton(ventana_configuracion, text= "Intermedio",font= "Corbel 12", width= 8,\
                                  bg= "#F4D6CC",variable= nivel_dificultad ,value=2, command= prueba)
    intermedio_rb.grid(row=3, column=1)

    dificil_rb= tk.Radiobutton(ventana_configuracion, text= "Dificil",font= "Corbel 12", width= 8, \
                               bg= "#F4D6CC",variable= nivel_dificultad , value=3, command= prueba)
    dificil_rb.grid(row=4, column=1)


    #Botones
    regresar_b= tk.Button(ventana_configuracion, text= "Regresar",font= "Corbel 12", width= 12, bg="#F4CFB1", command= lambda:regresar(ventana_configuracion))
    regresar_b.grid(row=20, column=0)

    

'''
Funcion para acerda de
'''
def acerca_de():
    ventana_principal.state(newstate="withdraw")
    ventana_configuracion= tk.Tk()
    ventana_configuracion.geometry("300x300")
    ventana_configuracion.title("FUTOSHIKI- Acerca de")
    ventana_configuracion.config(bg="#F4D6CC")

    name_label= tk.Label(ventana_configuracion, text= "FUTOSHIKI", font= "Corbel 22 bold", height= 1, width= 15, bg= "#C83E4D")
    name_label.grid(row=0, column=0)

    titulo1_label= tk.Label(ventana_configuracion, text= "Informacion",font= "Corbel 14 bold", bg= "#F4CFB1")
    titulo1_label.grid(row=1, column=0)

    titulo2_label= tk.Label(ventana_configuracion, text= "Version 2.5.9",font= "Corbel 14 bold",  bg= "#F4CFB1")
    titulo2_label.grid(row=2, column=0)

    titulo3_label= tk.Label(ventana_configuracion, text= "Creador: Melany Salas Fernandez",font= "Corbel 14 bold",  bg= "#F4CFB1")
    titulo3_label.grid(row=2, column=0)

    titulo3_label= tk.Label(ventana_configuracion, text= "Fecha de creacion: Junio,2021",font= "Corbel 14 bold",  bg= "#F4CFB1")
    titulo3_label.grid(row=4, column=0)
    
    regresar_b= tk.Button(ventana_configuracion, text= "Regresar",font= "Corbel 12", width= 12, bg="#F4CFB1", command= lambda:regresar(ventana_configuracion))
    regresar_b.grid(row=10, column=0)
    
def regresar(ventana):
    ventana_principal.state(newstate= "normal")
    #ventana.state(newstate= "withdraw")
    ventana.destroy()
#-----------------------------Programa-Principal----------------------

#Golabls
global nivel_dificultad
global numero
global lado_num
lado_num= 0
nivel_dificultad= 1
'''
Ventana principal
'''

ventana_principal= tk.Tk()
ventana_principal.geometry("500x300")
ventana_principal.title("Ventana principal")
ventana_principal.config(bg="#F4D6CC")


#Labels
name_label= tk.Label(ventana_principal, text= "FUTOSHIKI", font= "Corbel 22 bold", height= 1, width= 15, bg= "#C83E4D")
name_label.grid(row=0, column=1)

name_label= tk.Label(ventana_principal, height= 11, width= 15, bg= "#F4D6CC")
name_label.grid(row=1, column=1)


#Botones
a_jugar_b= tk.Button(ventana_principal, text= "A jugar",font= "Corbel 12", width= 12, bg="#F4CFB1", command= a_jugar)
a_jugar_b.grid(row=10, column=0)

configura_b= tk.Button(ventana_principal, text= "Configuracion",font= "Corbel 12", width= 12, bg="#F4CFB1", command= configuracion)
configura_b.grid(row=11, column=0)

ayuda_b= tk.Button(ventana_principal, text= "Ayuda",font= "Corbel 12", width= 12, bg="#F4CFB1")
ayuda_b.grid(row=10, column=3)

ayuda_b= tk.Button(ventana_principal, text= "Acerca de",font= "Corbel 12", width= 12, bg="#F4CFB1", command= acerca_de)
ayuda_b.grid(row=11, column=3)

#ventana_principal= tk.toplevel()

ventana_principal.mainloop()
