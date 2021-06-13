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
import pickle

#----------------------------------Funciones--------------------------
#__________________________________________
'''
Funcion para grabar datos
Entradas: Datod y nombre del archivo
Salidas: Agrega los datos al archivo
'''
def graba_datos(datos, nombre_archivo):
    arc= open(nombre_archivo, "ab")
    pickle.dump(datos, arc)
    arc.close
    print("Se grabo el archivo")
#__________________________________________
'''
Funcion para leer datos de un archivo
Entradas: nombre del archivo
Salidas: Hace print a los datos del archivo
'''
    
def lee_datos(nombre_archivo):
    arc= open(nombre_archivo, "rb")
    while True:
        try:
            lectura=pickle.load(arc)
            print(lectura)
        except:
            break
    arc.close
   
#__________________________________________
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
    global ventana_a_jugar
    global matriz_juego
    
    ventana_principal.state(newstate="withdraw")
    ventana_a_jugar= tk.Tk()
    ventana_a_jugar.geometry("800x800")
    ventana_a_jugar.title("FUTOSHIKI- A jugar")
    ventana_a_jugar.config(bg="#F4D6CC")
    numero= tk.IntVar

    #Titulo
    name_label= tk.Label(ventana_a_jugar, text= "FUTOSHIKI", font= "Corbel 22 bold", height= 1, width= 15, bg= "#C83E4D").place(x=150, y=0)
    n_label= tk.Label(ventana_a_jugar, height= 1, width= 15, bg= "#F4D6CC").grid(row=0, column=0)
    
    #Nivel
    if nivel_dificultad==1:
        nivelsms="Facil"
    elif nivel_dificultad==2:
        nivelsms="Intermedio"
    elif nivel_dificultad==3:
        nivelsms="Dificil"
    nivel_label= tk.Label(ventana_a_jugar, text= "Nivel: " + nivelsms, font= "Corbel 12 ", bg="#F4D6CC").grid(row=1, column=0)
    
    #Nombre
    #Label
    namej_label= tk.Label(ventana_a_jugar, text= "Nombre del jugador: ", font= "Corbel 12 ", bg="#F4D6CC").grid(row=2, column=0)
    #Entry
    namej_entry= tk.Entry(ventana_a_jugar, font= "Corbel 12 ", bg="#F4CFB1").place(x=150, y=60)
    

    if lado_num == 0: #Derecha
        b1= tk.Button(ventana_a_jugar, text= "1", width= 5, bg="#F4CFB1", command=lambda:asigna_value(1)).grid(row=4, column=1)

        b2= tk.Button(ventana_a_jugar, text= "2", width= 5, bg="#F4CFB1", command=lambda:asigna_value(2)).grid(row=6, column=1)

        b3= tk.Button(ventana_a_jugar, text= "3", width= 5, bg="#F4CFB1", command=lambda:asigna_value(3)).grid(row=8, column=1)

        b4= tk.Button(ventana_a_jugar, text= "4", width= 5, bg="#F4CFB1", command=lambda:asigna_value(4)).grid(row=10, column=1)

        b5= tk.Button(ventana_a_jugar, text= "5", width= 5, bg="#F4CFB1", command=lambda:asigna_value(5)).grid(row=12, column=1)
        
    else:
        b1= tk.Button(ventana_a_jugar, text= "1", width= 5, bg="#F4CFB1",  command=lambda:asigna_value(1)).grid(row=4, column=20)

        b2= tk.Button(ventana_a_jugar, text= "2", width= 5, bg="#F4CFB1", command=lambda:asigna_value(2)).grid(row=6, column=20)

        b3= tk.Button(ventana_a_jugar, text= "3", width= 5, bg="#F4CFB1", command=lambda:asigna_value(3)).grid(row=8, column=20)

        b4= tk.Button(ventana_a_jugar, text= "4", width= 5, bg="#F4CFB1", command=lambda:asigna_value(4)).grid(row=10, column=20)

        b5= tk.Button(ventana_a_jugar, text= "5", width= 5, bg="#F4CFB1", command=lambda:asigna_value(5)).grid(row=12, column=20)
        
    f0c0=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860", command=lambda:asigna_casilla(0)).grid(row=4, column=2)
    f0c1=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860", command=lambda:asigna_casilla(1)).grid(row=6, column=2)
    f0c2=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860", command=lambda:asigna_casilla(2)).grid(row=8, column=2)
    f0c3=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(3)).grid(row=10, column=2)
    f0c4=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(4)).grid(row=12, column=2)

    f1c0=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(5)).grid(row=4, column=4)
    f1c1=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(6)).grid(row=6, column=4)
    f1c2=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(7)).grid(row=8, column=4)
    f1c3=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(8)).grid(row=10, column=4)
    f1c4=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(9)).grid(row=12, column=4)

    f2c0=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(10)).grid(row=4, column=6)
    f2c1=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(11)).grid(row=6, column=6)
    f2c2=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(12)).grid(row=8, column=6)
    f2c3=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(13)).grid(row=10, column=6)
    f2c4=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(14)).grid(row=12, column=6)

    f3c0=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(15)).grid(row=4, column=8)
    f3c1=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(16)).grid(row=6, column=8)
    f3c2=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(17)).grid(row=8, column=8)
    f3c3=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(18)).grid(row=10, column=8)
    f3c4=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(19)).grid(row=12, column=8)

    f4c0=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(20)).grid(row=4, column=10)
    f4c1=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(21)).grid(row=6, column=10)
    f4c2=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(22)).grid(row=8, column=10)
    f4c3=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(23)).grid(row=10, column=10)
    f4c4=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(24)).grid(row=12, column=10)

    #Label
    #mayor=tk.Label(ventana_a_jugar, text= ">", bg="#F4D6CC").grid(row=4, column=7)

    #Botones
    #Boton Incia Juego
    inicia_juego_b= tk.Button(ventana_a_jugar, text= "Iniciar juego",font= "Corbel 12",width= 11, bg="#DB504A").place(x=20, y=300)

    #Boton Borrar jugada
    borra_jugada_b= tk.Button(ventana_a_jugar, text= "Borrar jugada",font= "Corbel 12",width= 11, bg="#658E9C").place(x=150, y=300)

    #Boton Termina juego
    termina_juego_b= tk.Button(ventana_a_jugar, text= "Terminar juego",font= "Corbel 12",width= 11, bg="#6D8A96").place(x=290, y=300)

    #Boton Top 10
    top10_b= tk.Button(ventana_a_jugar, text= "Top 10",font= "Corbel 12",width= 11, bg="#DB504A").place(x=440, y=300)

    #Boton Guarda juego
    guarda_juego_b= tk.Button(ventana_a_jugar, text= "Guardar juego",font= "Corbel 12",width= 11, bg="#7A6174").place(x=290, y=400)

    #Boton Carga juego
    cargar_juego_b= tk.Button(ventana_a_jugar, text= "Cargar juego",font= "Corbel 12",width= 11, bg="#7A6174").place(x=440, y=400)

    #Etiquetas reloj
    hora_label= tk.Label(ventana_a_jugar, text= "Hora",width= 9, font= "Corbel 12", bg="#DB504A").place(x=10, y=350)
    min_label= tk.Label(ventana_a_jugar, text= "Minutos",width= 9, font= "Corbel 12 ", bg="#7A6174").place(x=95, y=350)
    seg_label= tk.Label(ventana_a_jugar, text= "Segundos",width= 9, font= "Corbel 12 ", bg="#6D8A96").place(x=180, y=350)

    hora_label= tk.Label(ventana_a_jugar, text= "0",width= 9,height= 2,font= "Corbel 12", bg="#F4C796").place(x=10, y=375)
    min_label= tk.Label(ventana_a_jugar, text= "0",width= 9,height= 2,font= "Corbel 12", bg="#F4C796").place(x=95, y=375)
    seg_label= tk.Label(ventana_a_jugar, text= "0",width= 9,height= 2,font= "Corbel 12", bg="#F4C796").place(x=180, y=375)


    
    #Regresar
    regresar_b= tk.Button(ventana_a_jugar, text= "X",font= "Corbel 12 bold", bg="#6D8A96", command= lambda:regresar(ventana_a_jugar)).grid(row=0, column=25)
#__________________________________________
'''
Funcion asigna valor
Entradas: boton(cada boton tiene un codigo que es de 1 al 5)
Salidas: actualiza el valor de la variable numero
'''
def asigna_value(boton):
    global numero
    if boton == 1:
        numero=1
        #pass
        #print(numero)
    elif boton == 2:
        numero=2
        #print(numero)
    elif boton == 3:
        numero=3
        #print(numero)
    elif boton == 4:
        numero=4
        #print(numero)
    elif boton == 5:
        numero=5
        #print(numero)
    #boton.config(bg="green")
    return
#__________________________________________
'''
Funcion asigna casilla
Entradas: codigo(cada boton tiene un codigo que es de 0 al 24)
Salidas: actualiza el valor de los botones segun la variable numero
'''
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

    global matriz_juego


    global ventana_a_jugar
    if cod == 0:
        for i, num in enumerate(matriz_juego[0]):
            if numero == matriz_juego[1][0] or numero == matriz_juego[2][0] or numero == matriz_juego[3][0] or numero == matriz_juego[4][0]:
                f0c0=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D", command=lambda:asigna_casilla(0)).grid(row=4, column=2)
                break
            
            elif num == numero and i != 0:
                f0c0=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D", command=lambda:asigna_casilla(0)).grid(row=4, column=2)
                break
            
            else:
                f0c0=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860", command=lambda:asigna_casilla(0)).grid(row=4, column=2)
            matriz_juego[0][0]= numero
        
    elif cod == 1:
        for i,num in enumerate(matriz_juego[1]):
            if numero == matriz_juego[0][0] or numero == matriz_juego[2][0] or numero == matriz_juego[3][0] or numero == matriz_juego[4][0]:
                f0c1=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D", command=lambda:asigna_casilla(1)).grid(row=6, column=2)
                break
            
            elif num == numero and i != 0:
                f0c1=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D", command=lambda:asigna_casilla(1)).grid(row=6, column=2)
                break
            
            else:
                f0c1=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860", command=lambda:asigna_casilla(1)).grid(row=6, column=2)
            matriz_juego[1][0]= numero
        
    elif cod == 2:
        for i,num in enumerate(matriz_juego[2]):
            if numero == matriz_juego[0][0] or numero == matriz_juego[1][0] or numero == matriz_juego[3][0] or numero == matriz_juego[4][0]:
                f0c2=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D", command=lambda:asigna_casilla(2)).grid(row=8, column=2)
                break
            
            elif num == numero and i != 0:
                f0c2=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D", command=lambda:asigna_casilla(2)).grid(row=8, column=2)
                break
            
            else:
                f0c2=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860", command=lambda:asigna_casilla(2)).grid(row=8, column=2)
            matriz_juego[2][0]= numero
        
    elif cod == 3:
        for i,num in enumerate(matriz_juego[3]):
            if numero == matriz_juego[0][0] or numero == matriz_juego[1][0] or numero == matriz_juego[2][0] or numero == matriz_juego[4][0]:
                f0c3=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(3)).grid(row=10, column=2)
                break
            
            elif num == numero and i != 0:
                f0c3=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(3)).grid(row=10, column=2)
                break
            
            else:
                f0c3=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(3)).grid(row=10, column=2)
            matriz_juego[3][0]= numero
        #print(matriz_juego)
    
    elif cod == 4:
        for i,num in enumerate(matriz_juego[4]):
            if numero == matriz_juego[0][0] or numero == matriz_juego[1][0] or numero == matriz_juego[2][0] or numero == matriz_juego[3][0]:
                f0c4=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(4)).grid(row=12, column=2)
                break
            
            elif num == numero and i != 0:
                f0c4=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(4)).grid(row=12, column=2)
                break
            
            else:
                f0c4=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(4)).grid(row=12, column=2)
            matriz_juego[4][0]= numero
        #print(matriz_juego)
#_________________________________________________________________________________________________________________________________________________
        
    elif cod == 5:
        for i,num in enumerate(matriz_juego[0]):
            if numero == matriz_juego[4][1] or numero == matriz_juego[1][1] or numero == matriz_juego[2][1] or numero == matriz_juego[3][1]:
                f1c0=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(5)).grid(row=4, column=4)
                break
            
            elif num == numero and i != 1:
                f1c0=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(5)).grid(row=4, column=4)
                break
            
            else:
                f1c0=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(5)).grid(row=4, column=4)
            matriz_juego[0][1]= numero
        #print(matriz_juego)
        
    elif cod == 6:
        for i,num in enumerate(matriz_juego[1]):
            if numero == matriz_juego[0][1] or numero == matriz_juego[2][1] or numero == matriz_juego[3][1] or numero == matriz_juego[4][1]:
                f1c1=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(6)).grid(row=6, column=4)
                break
            
            elif num == numero and i != 1:
                f1c1=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(6)).grid(row=6, column=4)
                break
            
            else:
                f1c1=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(6)).grid(row=6, column=4)
                matriz_juego[1][1]= numero
        #print(matriz_juego)
    
    elif cod == 7:
        for i,num in enumerate(matriz_juego[2]):
            if numero == matriz_juego[0][1] or numero == matriz_juego[1][1] or numero == matriz_juego[3][1] or numero == matriz_juego[4][1]:
                f1c2=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(7)).grid(row=8, column=4)
                break
            
            elif num == numero and i != 1:
                f1c2=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(7)).grid(row=8, column=4)
                break
            
            else:
                f1c2=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(7)).grid(row=8, column=4)
            matriz_juego[2][1]= numero
        #print(matriz_juego)
    
    elif cod == 8:
        for i,num in enumerate(matriz_juego[3]):
            if numero == matriz_juego[0][1] or numero == matriz_juego[1][1] or numero == matriz_juego[2][1] or numero == matriz_juego[4][1]:
                f1c3=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(8)).grid(row=10, column=4)
                break
            
            elif num == numero and i != 1:
                f1c3=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(8)).grid(row=10, column=4)
                break
            
            else:
                f1c3=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(8)).grid(row=10, column=4)
            matriz_juego[3][1]= numero
        #print(matriz_juego)
        
    elif cod == 9:
        for i,num in enumerate(matriz_juego[4]):
            if numero == matriz_juego[0][1] or numero == matriz_juego[1][1] or numero == matriz_juego[2][1] or numero == matriz_juego[3][1]:
                f1c4=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(9)).grid(row=12, column=4)
                break
            
            elif num == numero and i != 1:
                f1c4=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(9)).grid(row=12, column=4)
                break
            
            else:
                f1c4=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(9)).grid(row=12, column=4)
            matriz_juego[4][1]= numero
        #print(matriz_juego)
#_________________________________________________________________________________________________________________________________________________
        
    elif cod == 10:
        for i,num in enumerate(matriz_juego[0]):
            if numero == matriz_juego[1][2] or numero == matriz_juego[2][2] or numero == matriz_juego[3][2] or numero == matriz_juego[4][2]:
                f2c0=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(10)).grid(row=4, column=6)
                break
            
            elif num == numero and i != 2:
                f2c0=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(10)).grid(row=4, column=6)
                break
            
            else:
                f2c0=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(10)).grid(row=4, column=6)
            matriz_juego[0][2]= numero
        #print(matriz_juego)
    
    elif cod == 11:
         for i,num in enumerate(matriz_juego[1]):
            if numero == matriz_juego[0][2] or numero == matriz_juego[2][2] or numero == matriz_juego[3][2] or numero == matriz_juego[4][2]:
                f2c1=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(11)).grid(row=6, column=6)
                break
            
            elif num == numero and i != 2:
                f2c1=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(11)).grid(row=6, column=6)
                break
            
            else:
                f2c1=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(11)).grid(row=6, column=6)
                matriz_juego[1][2]= numero
       # print(matriz_juego)
    
    elif cod == 12:
        for i,num in enumerate(matriz_juego[2]):
            if numero == matriz_juego[0][2] or numero == matriz_juego[1][2] or numero == matriz_juego[3][2] or numero == matriz_juego[4][2]:
                f2c2=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(12)).grid(row=8, column=6)
                break
            
            elif num == numero and i != 2:
                f2c2=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(12)).grid(row=8, column=6)
                break
            
            else:
                f2c2=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(12)).grid(row=8, column=6)
            matriz_juego[2][2]= numero
        #print(matriz_juego)
    
    elif cod == 13:
         for i,num in enumerate(matriz_juego[3]):
            if numero == matriz_juego[0][2] or numero == matriz_juego[1][2] or numero == matriz_juego[2][2] or numero == matriz_juego[4][2]:
                f2c3=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(13)).grid(row=10, column=6)
                break
            
            elif num == numero and i != 2:
                f2c3=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(13)).grid(row=10, column=6)
                break
            
            else:
                f2c3=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(13)).grid(row=10, column=6)
            matriz_juego[3][2]= numero
        #print(matriz_juego)
    
    elif cod == 14:
        for i,num in enumerate(matriz_juego[4]):
            if numero == matriz_juego[0][2] or numero == matriz_juego[1][2] or numero == matriz_juego[2][2] or numero == matriz_juego[3][2]:
                f2c4=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(14)).grid(row=12, column=6)
                break
            
            elif num == numero and i != 2:
                f2c4=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(14)).grid(row=12, column=6)
                break
            
            else:
                f2c4=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(14)).grid(row=12, column=6)
            matriz_juego[4][2]= numero
       # print(matriz_juego)
#_________________________________________________________________________________________________________________________________________________

    elif cod == 15:
        for i,num in enumerate(matriz_juego[0]):
            if numero == matriz_juego[1][3] or numero == matriz_juego[2][3] or numero == matriz_juego[3][3] or numero == matriz_juego[4][3]:
                f3c0=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(15)).grid(row=4, column=8)
                break
            
            elif num == numero and i != 3:
                f3c0=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(15)).grid(row=4, column=8)
                break
            
            else:
                f3c0=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(15)).grid(row=4, column=8)
            matriz_juego[0][3]= numero
        #print(matriz_juego)
        
    elif cod == 16:
        for i,num in enumerate(matriz_juego[1]):
            if numero == matriz_juego[0][3] or numero == matriz_juego[2][3] or numero == matriz_juego[3][3] or numero == matriz_juego[4][3]:
                f3c1=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(16)).grid(row=6, column=8)
                break
            
            elif num == numero and i != 3:
                f3c1=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(16)).grid(row=6, column=8)
                break
            
            else:
                f3c1=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(16)).grid(row=6, column=8)
            matriz_juego[1][3]= numero
        #print(matriz_juego)
    
    elif cod == 17:
        for i,num in enumerate(matriz_juego[2]):
            if numero == matriz_juego[0][3] or numero == matriz_juego[1][3] or numero == matriz_juego[3][3] or numero == matriz_juego[4][3]:
                f3c2=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(17)).grid(row=8, column=8)
                break
            
            elif num == numero and i != 3:
                f3c2=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(17)).grid(row=8, column=8)
                break
            
            else:
                f3c2=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(17)).grid(row=8, column=8)
            matriz_juego[2][3]= numero
        #print(matriz_juego)
    
    elif cod == 18:
        for i,num in enumerate(matriz_juego[3]):
            if numero == matriz_juego[0][3] or numero == matriz_juego[1][3] or numero == matriz_juego[2][3] or numero == matriz_juego[4][3]:
                f3c3=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(18)).grid(row=10, column=8)
                break
            
            elif num == numero and i != 3:
                f3c3=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(18)).grid(row=10, column=8)
                break
            
            else:
                f3c3=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(18)).grid(row=10, column=8)
            matriz_juego[3][3]= numero
        #print(matriz_juego)
    
    elif cod == 19:
        for i,num in enumerate(matriz_juego[4]):
            if numero == matriz_juego[0][3] or numero == matriz_juego[1][3] or numero == matriz_juego[2][3] or numero == matriz_juego[3][3]:
                f3c4=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(19)).grid(row=12, column=8)
                break
            
            elif num == numero and i != 3:
                f3c4=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(19)).grid(row=12, column=8)
                break
            
            else:
                f3c4=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(19)).grid(row=12, column=8)
            matriz_juego[4][3]= numero
       # print(matriz_juego)
#________________________________________________________________________________________________________________________________________________
        
    elif cod == 20:
        for i,num in enumerate(matriz_juego[0]):
            if numero == matriz_juego[1][4] or numero == matriz_juego[2][4] or numero == matriz_juego[3][4] or numero == matriz_juego[4][4]:
                f4c0=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(20)).grid(row=4, column=10)
                break
            
            elif num == numero and i != 4:
                f4c0=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(20)).grid(row=4, column=10)
                break
            
            else:
                f4c0=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(20)).grid(row=4, column=10)
            matriz_juego[0][4]= numero
        #print(matriz_juego)
    
    elif cod == 21:
        for i,num in enumerate(matriz_juego[1]):
            if numero == matriz_juego[0][4] or numero == matriz_juego[2][4] or numero == matriz_juego[3][4] or numero == matriz_juego[4][4]:
                f4c1=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(21)).grid(row=6, column=10)
                break
            
            elif num == numero and i != 4:
                f4c1=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(21)).grid(row=6, column=10)
                break
            
            else:
                f4c1=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(21)).grid(row=6, column=10)
            matriz_juego[1][4]= numero
                #print(matriz_juego)
    
    elif cod == 22:
        for i,num in enumerate(matriz_juego[2]):
            if numero == matriz_juego[0][4] or numero == matriz_juego[1][4] or numero == matriz_juego[2][4] or numero == matriz_juego[4][4]:
                f4c2=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(22)).grid(row=8, column=10)
                break
            
            elif num == numero and i != 4:
                f4c2=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(22)).grid(row=8, column=10)
                break
            
            else:
                f4c2=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(22)).grid(row=8, column=10)
            matriz_juego[2][4]= numero
        #print(matriz_juego)
    
    elif cod == 23:
        for i,num in enumerate(matriz_juego[3]):
            if numero == matriz_juego[0][4] or numero == matriz_juego[1][4] or numero == matriz_juego[2][4] or numero == matriz_juego[4][4]:
                f4c3=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(23)).grid(row=10, column=10)
                break
            
            elif num == numero and i != 4:
                f4c3=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(23)).grid(row=10, column=10)
                break
            
            else:
                f4c3=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(23)).grid(row=10, column=10)
            matriz_juego[3][4]= numero
        #print(matriz_juego)
   
    elif cod == 24:
        for i,num in enumerate(matriz_juego[4]):
            if numero == matriz_juego[0][4] or numero == matriz_juego[1][4] or numero == matriz_juego[2][4] or numero == matriz_juego[3][4]:
                f4c4=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(24)).grid(row=12, column=10)
                break
            
            elif num == numero and i != 4:
                f4c4=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(24)).grid(row=12, column=10)
                break
            
            else:
                f4c4=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(24)).grid(row=12, column=10)
            matriz_juego[4][4]= numero
        #print(matriz_juego)

    
def prueba():
    global nivel_dificultad
    s= nivel_dificultad.get()
    print(s)
#___________________________________________________________VENTANA_CONFIGURACION________________________________________________________________________
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

#___________________________________________________________VENTANA_ACERCA_DE________________________________________________________________________
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

#Funcion que crea la matriz con listas en 0
def crea_matriz():
    global matriz_juego
    
    cont_l=0
    #cont0=0
    while cont_l < 5:
        matriz_juego.append([0,0,0,0,0])
        cont_l+=1
    #print(juego_lista)
    

#-----------------------------Programa-Principal----------------------

#Golabls
global nivel_dificultad
global numero
global lado_num
global matriz_juego
matriz_juego=[]
lado_num= 0
nivel_dificultad= 3
numero=0
crea_matriz()
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
