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
from tkinter import messagebox
from datetime import datetime

#----------------------------------Funciones--------------------------
#__________________________________________
'''
Entradas: Un string
Salidas: Muestra el mensaje con un message box
'''
def showMensaje(mensaje):
    messagebox.showinfo("Mensaje", mensaje)
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
Funcion para asina datos de un archivo
Entradas: nombre del archivo
Salidas: Hace print a los datos del archivo
'''
    
def asigna_datos(nombre_archivo):
    arc= open(nombre_archivo, "rb")
    while True:
        try:
            lectura=pickle.load(arc)
            #print(lectura)
            return lectura
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
    
    global ventana_a_jugar
    global matriz_juego
    global flag1

    global hora_actual
    global min_actual
    global seg_actual
    global reloj_o_time
    global hora_inicio

    global min_timer
    global hora_timer
    global seg_timer
    global ind_escoge_par

    global b1
    global b2
    global b3
    global b4
    global b5

    ind_escoge_par = 1

    flag1= 1
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
    nombre_jugador1= tk.Entry(ventana_a_jugar, font= "Corbel 12 ", bg="#F4CFB1")
    nombre_jugador1.place(x=150, y=60)
    
    
    if lado_num == 0: #Derecha
        b1= tk.Button(ventana_a_jugar, text= "1", width= 5, bg="#F4CFB1", command=lambda:asigna_value(1))
        b1.grid(row=4, column=1)

        b2= tk.Button(ventana_a_jugar, text= "2", width= 5, bg="#F4CFB1", command=lambda:asigna_value(2))
        b2.grid(row=6, column=1)

        b3= tk.Button(ventana_a_jugar, text= "3", width= 5, bg="#F4CFB1", command=lambda:asigna_value(3))
        b3.grid(row=8, column=1)

        b4= tk.Button(ventana_a_jugar, text= "4", width= 5, bg="#F4CFB1", command=lambda:asigna_value(4))
        b4.grid(row=10, column=1)

        b5= tk.Button(ventana_a_jugar, text= "5", width= 5, bg="#F4CFB1", command=lambda:asigna_value(5))
        b5.grid(row=12, column=1)
        
    else:
        b1= tk.Button(ventana_a_jugar, text= "1", width= 5, bg="#F4CFB1",  command=lambda:asigna_value(1))
        b1.grid(row=4, column=20)

        b2= tk.Button(ventana_a_jugar, text= "2", width= 5, bg="#F4CFB1", command=lambda:asigna_value(2))
        b2.grid(row=6, column=20)

        b3= tk.Button(ventana_a_jugar, text= "3", width= 5, bg="#F4CFB1", command=lambda:asigna_value(3))
        b3.grid(row=8, column=20)

        b4= tk.Button(ventana_a_jugar, text= "4", width= 5, bg="#F4CFB1", command=lambda:asigna_value(4))
        b4.grid(row=10, column=20)

        b5= tk.Button(ventana_a_jugar, text= "5", width= 5, bg="#F4CFB1", command=lambda:asigna_value(5))
        b5.grid(row=12, column=20)
        
    #asigna_value(0)
        
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
    
    #Espacios
    signo0=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=4, column=3)
    signo1=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=4, column=5)
    signo2=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=4, column=7)
    signo3=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=4, column=9)
    
    signo4=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=6, column=3)
    signo5=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=6, column=5)
    signo6=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=6, column=7)
    signo7=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=6, column=9)
 
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=8, column=3)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=8, column=5)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=8, column=7)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=8, column=9)
    
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=10, column=3)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=10, column=5)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=10, column=7)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=10, column=9)
    
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=5, column=2)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=5, column=4)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=5, column=6)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=5, column=8)

    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=7, column=2)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=7, column=4)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=7, column=6)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=7, column=8)
    
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=9, column=2)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=9, column=4)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=9, column=6)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=9, column=8)

    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=11, column=2)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=11, column=4)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=11, column=6)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=11, column=8)

    #Label
    #mayor=tk.Label(ventana_a_jugar, text= ">", bg="#F4D6CC").grid(row=4, column=7)

    #Botones
    #Boton Incia Juego
    inicia_juego_b= tk.Button(ventana_a_jugar, text= "Iniciar juego",font= "Corbel 12",width= 11, bg="#DB504A", command= lambda:carga_juego(nombre_jugador1.get())).place(x=20, y=400)
    #botona= tk.Button(ventana_entrada_v, text= "Aceptar", command= lambda: agrega_placa(fecha_hora_entrada, placa.get(),primer_esp, ventana_entrada_v))

    #Boton Borrar jugada
    borra_jugada_b= tk.Button(ventana_a_jugar, text= "Borrar jugada",font= "Corbel 12",width= 11, bg="#658E9C", command= desapila).place(x=150, y=400)

    #Boton Termina juego
    termina_juego_b= tk.Button(ventana_a_jugar, text= "Terminar juego",font= "Corbel 12",width= 11, bg="#6D8A96", command= termina_juego).place(x=290, y=400)

    #Boton Top 10
    top10_b= tk.Button(ventana_a_jugar, text= "Top 10",font= "Corbel 12",width= 11, bg="#DB504A").place(x=440, y=400)

    #Boton Guarda juego
    guarda_juego_b= tk.Button(ventana_a_jugar, text= "Guardar juego",font= "Corbel 12",width= 11, bg="#7A6174", command= guarda_juego).place(x=290, y=500)

    #Boton Carga juego
    cargar_juego_b= tk.Button(ventana_a_jugar, text= "Cargar juego",font= "Corbel 12",width= 11, bg="#7A6174", command=carga_partida).place(x=440, y=500)
    
    #borrar_juego()
    borra_juego_b= tk.Button(ventana_a_jugar, text= "Borrar juego",font= "Corbel 12",width= 11, bg="#6D8A96", command= lambda:borrar_juego(nombre_jugador1.get())).place(x=355, y=450)

    #Etiquetas reloj
    if reloj_o_time != 2:
        hora_label= tk.Label(ventana_a_jugar, text= "Hora",width= 9, font= "Corbel 12", bg="#DB504A").place(x=10, y=450)
        min_label= tk.Label(ventana_a_jugar, text= "Minutos",width= 9, font= "Corbel 12 ", bg="#7A6174").place(x=95, y=450)
        seg_label= tk.Label(ventana_a_jugar, text= "Segundos",width= 9, font= "Corbel 12 ", bg="#6D8A96").place(x=180, y=450)

        hora_actual= tk.Label(ventana_a_jugar, text= "0",width= 9,height= 2,font= "Corbel 12", bg="#F4C796").place(x=10, y=475)
        min_actual= tk.Label(ventana_a_jugar, text= "0",width= 9,height= 2,font= "Corbel 12", bg="#F4C796").place(x=95, y=475)
        seg_actual= tk.Label(ventana_a_jugar, text= "0",width= 9,height= 2,font= "Corbel 12", bg="#F4C796")
        seg_actual.place(x=180, y=475)
        
        if reloj_o_time == 3:
            ventana_pr=tk.Toplevel()
            ventana_pr.geometry("350x100")
            ventana_pr.title("FUTOSHIKI- Tiempo del cronometro")
            ventana_pr.config(bg="#F4D6CC")
            
            nombre= tk.Label(ventana_pr, text= "¿Desea cambien el tiempo del cronometro?", font= "Corbel 12 bold ", bg="#F4CFB1")
            nombre.place(x=5, y=5)

            regresar_b= tk.Button(ventana_pr, text= "No",font= "Corbel 12", bg="#F4CFB1", command= lambda:regresar_pr(ventana_pr,0))
            regresar_b.place(x=45, y=50)

            regresar_b= tk.Button(ventana_pr, text= "Sí",font= "Corbel 12", bg="#F4CFB1", command= lambda:regresar_pr(ventana_pr,1))
            regresar_b.place(x=85, y=50)
            
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
    global b1
    global b2
    global b3
    global b4
    global b5
    if boton == 1:
        numero=1
        b1.config(bg="#70b578")
        b2.config(bg="#F4CFB1")
        b3.config(bg="#F4CFB1")
        b4.config(bg="#F4CFB1")
        b5.config(bg="#F4CFB1")
        
    elif boton == 2:
        numero=2
        b1.config(bg="#F4CFB1")
        b2.config(bg="#70b578")
        b3.config(bg="#F4CFB1")
        b4.config(bg="#F4CFB1")
        b5.config(bg="#F4CFB1")
       
    elif boton == 3:
        numero=3
        b1.config(bg="#F4CFB1")
        b2.config(bg="#F4CFB1")
        b3.config(bg="#70b578")
        b4.config(bg="#F4CFB1")
        b5.config(bg="#F4CFB1")

    elif boton == 4:
        numero=4
        b1.config(bg="#F4CFB1")
        b2.config(bg="#F4CFB1")
        b3.config(bg="#F4CFB1")
        b4.config(bg="#70b578")
        b5.config(bg="#F4CFB1")
        
    elif boton == 5:
        numero=5
        b1.config(bg="#F4CFB1")
        b2.config(bg="#F4CFB1")
        b3.config(bg="#F4CFB1")
        b4.config(bg="#F4CFB1")
        b5.config(bg="#70b578")
    else:
        pass
        
    return
#__________________________________________
'''
Funcion asigna casilla
Entradas: codigo(cada boton tiene un codigo que es de 0 al 24)
Salidas: actualiza el valor de los botones segun la variable numero
'''
def asigna_casilla(cod):
    global numero

    global flag1
    
    global matriz_juego

    global ventana_a_jugar

    global matriz_0_1

    if numero != 1 and numero != 2 and numero != 3 and numero != 4 and numero != 5:
        showMensaje("No ha seleccionado un numero")
        return

    if cod == 0:
        f=False
        if isinstance(matriz_juego[0][0],str):
            showMensaje("JUGADA NO ES VÁLIDA PORQUE ESTE ES UN DÍGITO FIJO")
            return
        apila(matriz_juego[0][0], 0, 0,"#F4B860", 0, 4, 2)

        matriz_juego[0][0]= numero
        
        for i, num in enumerate(matriz_juego[0]):
            
            if numero == int(matriz_juego[1][0]) or numero == int(matriz_juego[2][0]) or numero == int(matriz_juego[3][0]) or numero == int(matriz_juego[4][0]):
                f0c0=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D", command=lambda:asigna_casilla(0)).grid(row=4, column=2)
                showMensaje("El numero " + str(numero) + " ya esta en la columna")
                matriz_0_1[0][0]=0
                f= False
                break
            
            elif int(num) == numero and i != 0:
                f0c0=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D", command=lambda:asigna_casilla(0)).grid(row=4, column=2)
                showMensaje("El numero " + str(numero)+ " ya esta en la fila")
                matriz_0_1[0][0]=0
                f= False
                break
            
            else:
                f0c0=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860", command=lambda:asigna_casilla(0)).grid(row=4, column=2)
                matriz_0_1[0][0]=1
                f=True
                pass
            
        if valida_mayor1(0, 0) == False and f != False:
            f0c0=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D", command=lambda:asigna_casilla(0)).grid(row=4, column=2)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[0][0]=0
            f= False
                  
        elif valida_mayor2(0, 0) == False and f != False:
            f0c0=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D", command=lambda:asigna_casilla(0)).grid(row=4, column=2)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[0][0]=0
            f= False

        if gane() == True:
            showMensaje("Ganó")

    elif cod == 1:
        if isinstance(matriz_juego[1][0],str):
            showMensaje("JUGADA NO ES VÁLIDA PORQUE ESTE ES UN DÍGITO FIJO")
            return
        apila(matriz_juego[1][0], 1, 0,"#F4B860", 1, 6, 2)
        matriz_juego[1][0]= numero
        
        for i,num in enumerate(matriz_juego[1]):
            #print(matriz_juego[1],num,1, numero)
            
            if numero == int(matriz_juego[0][0]) or numero == int(matriz_juego[2][0]) or numero == int(matriz_juego[3][0]) or numero == int(matriz_juego[4][0]):
                showMensaje("El numero " + str(numero) + " ya esta en la columna")
                f0c1=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D", command=lambda:asigna_casilla(1)).grid(row=6, column=2)
                matriz_0_1[1][0]=0
                f = False
                break
            
            elif int(num) == numero and i != 0:
                showMensaje("El numero " + str(numero)+ " ya esta en la fila")
                f0c1=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D", command=lambda:asigna_casilla(1)).grid(row=6, column=2)
                matriz_0_1[1][0]=0
                f = False
                break
       
            else:
                f0c1=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860", command=lambda:asigna_casilla(1)).grid(row=6, column=2)
                matriz_0_1[1][0]=1
                f = True
                pass
            
        if valida_mayor1(1, 0) == False and f != False:
            f0c1=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D", command=lambda:asigna_casilla(1)).grid(row=6, column=2)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[1][0]=0
            f = False
        
        elif valida_mayor2(1, 0) == False and f != False:
            f0c1=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D", command=lambda:asigna_casilla(1)).grid(row=6, column=2)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[1][0]=0
            f = False
            
        if gane() == True:
            #showMensaje("Ganó")
            mensaje_gane()
            
      
    elif cod == 2:
        if isinstance(matriz_juego[2][0],str):
            showMensaje("JUGADA NO ES VÁLIDA PORQUE ESTE ES UN DÍGITO FIJO")
            return
        apila(matriz_juego[2][0], 2, 0,"#F4B860", 2, 8, 2)
        
        matriz_juego[2][0]= numero
        for i,num in enumerate(matriz_juego[2]):
    
            if numero == int(matriz_juego[0][0]) or numero == int(matriz_juego[1][0]) or numero == int(matriz_juego[3][0]) or numero == int(matriz_juego[4][0]):
                showMensaje("El numero " + str(numero) + " ya esta en la columna")
                f0c2=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D", command=lambda:asigna_casilla(2)).grid(row=8, column=2)
                matriz_0_1[2][0]=0
                f= False
                break
            
            elif int(num) == numero and i != 0:
                f0c2=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D", command=lambda:asigna_casilla(2)).grid(row=8, column=2)
                showMensaje("El numero " + str(numero)+ " ya esta en la fila")
                matriz_0_1[2][0]=0
                f= False
                break
            
            else:
                f0c2=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860", command=lambda:asigna_casilla(2)).grid(row=8, column=2)
                matriz_0_1[2][0]=1
                f= True
                pass
            
        if valida_mayor1(2, 0) == False and f != False:
            f0c2=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D", command=lambda:asigna_casilla(2)).grid(row=8, column=2)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[2][0]=0
            f= False
            
        elif valida_mayor2(2, 0) == False and f != False:
            f0c2=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D", command=lambda:asigna_casilla(2)).grid(row=8, column=2)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[2][0]=0
            f= False
            
        if gane() == True:
            #showMensaje("Ganó")
            mensaje_gane()
   
    elif cod == 3:
        if isinstance(matriz_juego[3][0],str):
            showMensaje("JUGADA NO ES VÁLIDA PORQUE ESTE ES UN DÍGITO FIJO")
            return
        apila(matriz_juego[3][0], 3, 0,"#F4B860", 3, 10, 2)
        matriz_juego[3][0]= numero
        
        for i,num in enumerate(matriz_juego[3]):
            
            if numero == int(matriz_juego[0][0]) or numero == int(matriz_juego[1][0]) or numero == int(matriz_juego[2][0]) or numero == int(matriz_juego[4][0]):
                showMensaje("El numero " + str(numero) + " ya esta en la columna")
                f0c3=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(3)).grid(row=10, column=2)
                matriz_0_1[3][0]=0
                f= False
                break
            
            elif int(num) == numero and i != 0:
                f0c3=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(3)).grid(row=10, column=2)
                showMensaje("El numero " + str(numero)+ " ya esta en la fila")
                matriz_0_1[3][0]=0
                f= False
                break
            
            else:
                f0c3=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(3)).grid(row=10, column=2)
                matriz_0_1[3][0]=1
                f=True
                pass
        
        if valida_mayor1(3, 0) == False and f!= False:
            f0c3=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(3)).grid(row=10, column=2)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[3][0]=0
            f= False
        
        elif valida_mayor2(3, 0) == False and f!= False:
            f0c3=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(3)).grid(row=10, column=2)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[3][0]=0
            f=False
        
        if gane() == True:
            #showMensaje("Ganó")
            mensaje_gane()
        

    elif cod == 4:
        if isinstance(matriz_juego[4][0],str):
            showMensaje("JUGADA NO ES VÁLIDA PORQUE ESTE ES UN DÍGITO FIJO")
            return
        apila(matriz_juego[4][0], 4, 0,"#F4B860", 4, 12, 2)
        matriz_juego[4][0]= numero
        
        for i,num in enumerate(matriz_juego[4]):
            if numero == int(matriz_juego[0][0]) or numero == int(matriz_juego[1][0]) or numero == int(matriz_juego[2][0]) or numero == int(matriz_juego[3][0]):
                showMensaje("El numero " + str(numero) + " ya esta en la columna")
                f0c4=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(4)).grid(row=12, column=2)
                matriz_0_1[4][0]=0
                f= False
                break
            
            elif int(num) == numero and i != 0:
                f0c4=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(4)).grid(row=12, column=2)
                showMensaje("El numero " + str(numero)+ " ya esta en la fila")
                matriz_0_1[4][0]=0
                f= False
                break

            else:
                f0c4=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(4)).grid(row=12, column=2)
                matriz_0_1[4][0]=1
                f= True
                pass
            
        if valida_mayor1(4, 0) == False and f!= False:
            f0c4=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(4)).grid(row=12, column=2)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[4][0]=0
            f= False
        
        elif valida_mayor2(4, 0) == False and f!= False:
            f0c4=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(4)).grid(row=12, column=2)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[4][0]=0
            f=False
        
        if gane() == True:
            #showMensaje("Ganó")
            mensaje_gane()
          
#_________________________________________________________________________________________________________________________________________________
        
    elif cod == 5:
        if isinstance(matriz_juego[0][1],str):
            showMensaje("JUGADA NO ES VÁLIDA PORQUE ESTE ES UN DÍGITO FIJO")
            return
        apila(matriz_juego[0][1], 0, 1,"#F4B860", 5, 4, 4)
        matriz_juego[0][1]= numero
        
        for i,num in enumerate(matriz_juego[0]):
            if numero == int(matriz_juego[4][1]) or numero == int(matriz_juego[1][1]) or numero == int(matriz_juego[2][1]) or numero == int(matriz_juego[3][1]):
                showMensaje("El numero " + str(numero) + " ya esta en la columna")
                f1c0=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(5)).grid(row=4, column=4)
                matriz_0_1[0][1]=0
                f= False
                break
            
            elif int(num) == numero and i != 1:
                f1c0=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(5)).grid(row=4, column=4)
                showMensaje("El numero " + str(numero)+ " ya esta en la fila")
                matriz_0_1[0][1]=0
                f= False
                break

            else:
                f1c0=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(5)).grid(row=4, column=4)
                matriz_0_1[0][1]=1
                f= True
                pass
            
        if valida_mayor1(0, 1) == False and f!= False:
            f1c0=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(5)).grid(row=4, column=4)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[0][1]=0
            f= False
        
        elif valida_mayor2(0, 1) == False and f!= False:
            f1c0=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(5)).grid(row=4, column=4)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[0][1]=0
            f= False
            
        if gane() == True:
            #showMensaje("Ganó")
            mensaje_gane()

        
    elif cod == 6:
        if isinstance(matriz_juego[1][1],str):
            showMensaje("JUGADA NO ES VÁLIDA PORQUE ESTE ES UN DÍGITO FIJO")
            return
        apila(matriz_juego[1][1], 1, 1,"#F4B860", 6, 6, 4)
        matriz_juego[1][1]= numero
        
        for i,num in enumerate(matriz_juego[1]):
            if numero == int(matriz_juego[0][1]) or numero == int(matriz_juego[2][1]) or numero == int(matriz_juego[3][1]) or numero == int(matriz_juego[4][1]):
                showMensaje("El numero " + str(numero) + " ya esta en la columna")
                matriz_0_1[1][1]=0
                f= False
                break
            
            elif int(num) == numero and i != 1:
                f1c1=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(6)).grid(row=6, column=4)
                showMensaje("El numero " + str(numero)+ " ya esta en la fila")
                matriz_0_1[1][1]=0
                f= False
                break
            
            else:
                f1c1=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(6)).grid(row=6, column=4)
                matriz_0_1[1][1]=1
                f= True
                pass
            
        if valida_mayor1(1, 1) == False and f!= False:
            f1c1=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(6)).grid(row=6, column=4)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[1][1]=0
            f=False
        
        elif valida_mayor2(1, 1) == False and f!= False:
            f1c1=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(6)).grid(row=6, column=4)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[1][1]=0
            f= False

        if gane() == True:
            #showMensaje("Ganó")
            mensaje_gane()

    
    elif cod == 7:
        if isinstance(matriz_juego[2][1],str):
            showMensaje("JUGADA NO ES VÁLIDA PORQUE ESTE ES UN DÍGITO FIJO")
            return
        apila(matriz_juego[2][1], 2, 1,"#F4B860", 7, 8, 4)   
        matriz_juego[2][1]= numero
        for i,num in enumerate(matriz_juego[2]):
            if numero == int(matriz_juego[0][1]) or numero == int(matriz_juego[1][1]) or numero == int(matriz_juego[3][1]) or numero == int(matriz_juego[4][1]):
                f1c2=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(7)).grid(row=8, column=4)
                showMensaje("El numero " + str(numero) + " ya esta en la columna")
                matriz_0_1[2][1]=0
                f= False
                break
            
            elif int(num) == numero and i != 1:
                f1c2=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(7)).grid(row=8, column=4)
                showMensaje("El numero " + str(numero)+ " ya esta en la fila")
                matriz_0_1[2][1]=0
                f= False
                break
            
            else:
                f1c2=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(7)).grid(row=8, column=4)
                matriz_0_1[2][1]=1
                f= True
                pass
            
        if valida_mayor1(2, 1) == False and f!= False:
            f1c2=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(7)).grid(row=8, column=4)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[2][1]=0
            f=False
            
        
        elif valida_mayor2(2, 1) == False and f!= False:
            f1c2=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(7)).grid(row=8, column=4)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[2][1]=0
            f=False

        if gane() == True:
            #showMensaje("Ganó")
            mensaje_gane()
        

    
    elif cod == 8:
        if isinstance(matriz_juego[3][1],str):
            showMensaje("JUGADA NO ES VÁLIDA PORQUE ESTE ES UN DÍGITO FIJO")
            return
        apila(matriz_juego[3][1], 3, 1,"#F4B860", 8, 10, 4)     
        matriz_juego[3][1]= numero
        print(numero)
        
        for i,num in enumerate(matriz_juego[3]):
            if numero == int(matriz_juego[0][1]) or numero == int(matriz_juego[1][1]) or numero == int(matriz_juego[2][1]) or numero == int(matriz_juego[4][1]):
                f1c3=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(8)).grid(row=10, column=4)
                showMensaje("El numero " + str(numero) + " ya esta en la columna")
                matriz_0_1[3][1]=0
                f= False
                break
            
            elif int(num) == numero and i != 1:
                f1c3=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(8)).grid(row=10, column=4)
                showMensaje("El numero " + str(numero)+ " ya esta en la fila")
                matriz_0_1[3][1]=0
                f= False
                break
            
            else:
                f1c3=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(8)).grid(row=10, column=4)
                matriz_0_1[3][1]=1
                f= True
                pass
            
        if valida_mayor1(3, 1) == False and f!= False:
            f1c3=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(8)).grid(row=10, column=4)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[3][1]=0
            f=False
        
        elif valida_mayor2(3, 1) == False and f!= False:
            f1c3=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(8)).grid(row=10, column=4)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[3][1]=0
            f= False
            
        if gane() == True:
            #showMensaje("Ganó")
            mensaje_gane()

        
    elif cod == 9:
        if isinstance(matriz_juego[4][1],str):
            showMensaje("JUGADA NO ES VÁLIDA PORQUE ESTE ES UN DÍGITO FIJO")
            return
        apila(matriz_juego[4][1], 4, 1,"#F4B860", 9, 12, 4) 
        matriz_juego[4][1]= numero
        
        for i,num in enumerate(matriz_juego[4]):
            if numero == int(matriz_juego[0][1]) or numero == int(matriz_juego[1][1]) or numero == int(matriz_juego[2][1]) or numero == int(matriz_juego[3][1]):
                f1c4=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(9)).grid(row=12, column=4)
                showMensaje("El numero " + str(numero) + " ya esta en la columna")
                matriz_0_1[4][1]=0
                f= False
                break
            
            elif int(num) == numero and i != 1:
                f1c4=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(9)).grid(row=12, column=4)
                showMensaje("El numero " + str(numero)+ " ya esta en la fila")
                matriz_0_1[4][1]=0                
                f= False
                break
            
            else:
                f1c4=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(9)).grid(row=12, column=4)
                matriz_0_1[4][1]=1
                f=True
                pass
            
        if valida_mayor1(4, 1) == False and f!= False:
            f1c4=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(9)).grid(row=12, column=4)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[4][1]=0
            f=False
        
        elif valida_mayor2(4, 1) == False and f!= False:
            f1c4=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(9)).grid(row=12, column=4)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[4][1]=0
            f=False
        if gane() == True:
            #showMensaje("Ganó")
            mensaje_gane()

#_________________________________________________________________________________________________________________________________________________
        
    elif cod == 10:
        if isinstance(matriz_juego[0][2],str):
            showMensaje("JUGADA NO ES VÁLIDA PORQUE ESTE ES UN DÍGITO FIJO")
            return

        apila(matriz_juego[0][2], 0, 2,"#F4B860", 10, 4, 6) 
        matriz_juego[0][2]= numero
        for i,num in enumerate(matriz_juego[0]):
            if numero == int(matriz_juego[1][2]) or numero == int(matriz_juego[2][2]) or numero == int(matriz_juego[3][2]) or numero == int(matriz_juego[4][2]):
                f2c0=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(10)).grid(row=4, column=6)
                showMensaje("El numero " + str(numero) + " ya esta en la columna")
                matriz_0_1[0][2]=0
                f= False
                break
            
            elif int(num) == numero and i != 2:
                f2c0=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(10)).grid(row=4, column=6)
                showMensaje("El numero " + str(numero)+ " ya esta en la fila")
                matriz_0_1[0][2]=0
                f= False
                break
            
            else:
                f2c0=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(10)).grid(row=4, column=6)
                matriz_0_1[0][2]=1
                f=True
                pass
            
        if valida_mayor1(0, 2) == False and f!= False:
            f2c0=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(10)).grid(row=4, column=6)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[0][2]=0
            f= False
        
        elif valida_mayor2(0, 2) == False and f!= False:
            f2c0=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(10)).grid(row=4, column=6)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[0][2]=0
            f=False

        if gane() == True:
            #showMensaje("Ganó")
            mensaje_gane()
    
    elif cod == 11:
        if isinstance(matriz_juego[1][2],str):
            showMensaje("JUGADA NO ES VÁLIDA PORQUE ESTE ES UN DÍGITO FIJO")
            return
        
        apila(matriz_juego[1][2], 1, 2,"#F4B860", 11, 6, 6) 
        matriz_juego[1][2]= numero
        
        for i,num in enumerate(matriz_juego[1]):
            if numero == int(matriz_juego[0][2]) or numero == int(matriz_juego[2][2]) or numero == int(matriz_juego[3][2]) or numero == int(matriz_juego[4][2]):
                f2c1=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(11)).grid(row=6, column=6)
                showMensaje("El numero " + str(numero) + " ya esta en la columna")
                matriz_0_1[1][2]=0
                f= False
                break
            
            elif int(num) == numero and i != 2:
                showMensaje("El numero " + str(numero) + " ya esta en la fila")
                f2c1=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(11)).grid(row=6, column=6)
                matriz_0_1[1][2]=0
                f= False
                break
            
            else:
                f2c1=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(11)).grid(row=6, column=6)
                matriz_0_1[1][2]=1
                f= True
                pass

        if not valida_mayor1(1, 2) == True and f!= False:
            f2c1=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(11)).grid(row=6, column=6)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[1][2]=0
            f= False


        elif not valida_mayor2(1, 2) == True and f!= False:
            f2c1=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(11)).grid(row=6, column=6)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[1][2]=0
            f= False
            #print("es aqui 2")

        if gane() == True:
            #showMensaje("Ganó")
            mensaje_gane()
    
    elif cod == 12:
        if isinstance(matriz_juego[2][2],str):
            showMensaje("JUGADA NO ES VÁLIDA PORQUE ESTE ES UN DÍGITO FIJO")
            return
        
        apila(matriz_juego[2][2], 2, 2,"#F4B860", 12, 8, 6)
        matriz_juego[2][2]= numero

        for i,num in enumerate(matriz_juego[2]):
            if numero == int(matriz_juego[0][2]) or numero == int(matriz_juego[1][2]) or numero == int(matriz_juego[3][2]) or numero == int(matriz_juego[4][2]):
                f2c2=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(12)).grid(row=8, column=6)
                showMensaje("El numero " + str(numero) + " ya esta en la columna")
                matriz_0_1[2][2]=0
                f= False
                break
            
            elif int(num) == numero and i != 2:
                f2c2=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(12)).grid(row=8, column=6)
                showMensaje("El numero " + str(numero)+ " ya esta en la fila")
                matriz_0_1[2][2]=0
                f= False
                break
            
            else:
                f2c2=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(12)).grid(row=8, column=6)
                matriz_0_1[2][2]=1
                f= True
                pass
            
        if valida_mayor1(2, 2) == False and f!= False:
            f2c2=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(12)).grid(row=8, column=6)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[2][2]=0
            f= False
        
        elif valida_mayor2(2, 2) == False and f!= False:
            f2c2=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(12)).grid(row=8, column=6)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[2][2]=0
            f= False
            
        if gane() == True:
            #showMensaje("Ganó")
            mensaje_gane()

            
    elif cod == 13:
        if isinstance(matriz_juego[3][2],str):
            showMensaje("JUGADA NO ES VÁLIDA PORQUE ESTE ES UN DÍGITO FIJO")
            return
        
        apila(matriz_juego[3][2], 3, 2,"#F4B860", 13, 10, 6)
        matriz_juego[3][2]= numero
        
        for i,num in enumerate(matriz_juego[3]):
            if numero == int(matriz_juego[0][2]) or numero == int(matriz_juego[1][2]) or numero == int(matriz_juego[2][2]) or numero == int(matriz_juego[4][2]):
                f2c3=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(13)).grid(row=10, column=6)
                showMensaje("El numero " + str(numero) + " ya esta en la columna")
                matriz_0_1[3][2]=0
                f= False
                break
            
            elif int(num) == numero and i != 2:
                f2c3=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(13)).grid(row=10, column=6)
                showMensaje("El numero " + str(numero)+ " ya esta en la fila")
                matriz_0_1[3][2]=0
                f= False
                break

            else:
                f2c3=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(13)).grid(row=10, column=6)
                matriz_0_1[3][2]=1
                f= True
                pass
            
        if valida_mayor1(3, 2) == False and f!= False:
            f2c3=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(13)).grid(row=10, column=6)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[3][2]=0
            f=False

        elif valida_mayor2(3, 2) == False and f!= False:
            f2c3=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(13)).grid(row=10, column=6)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[3][2]=0
            f=False

        if gane() == True:
            #showMensaje("Ganó")
            mensaje_gane()
    
    elif cod == 14:
        if isinstance(matriz_juego[4][2],str):
            showMensaje("JUGADA NO ES VÁLIDA PORQUE ESTE ES UN DÍGITO FIJO")
            return
        apila(matriz_juego[4][2], 4, 2,"#F4B860", 14, 12, 6)
        matriz_juego[4][2]= numero

        for i,num in enumerate(matriz_juego[4]):
            if numero == int(matriz_juego[0][2]) or numero == int(matriz_juego[1][2]) or numero == int(matriz_juego[2][2]) or numero == int(matriz_juego[3][2]):
                f2c4=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(14)).grid(row=12, column=6)
                showMensaje("El numero " + str(numero) + " ya esta en la columna")
                matriz_0_1[4][2]=0
                f= False
                break
            
            elif int(num) == numero and i != 2:
                f2c4=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(14)).grid(row=12, column=6)
                showMensaje("El numero " + str(numero)+ " ya esta en la fila")
                matriz_0_1[4][2]=0
                f= False
                break
            
            else:
                f2c4=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(14)).grid(row=12, column=6)
                matriz_0_1[4][2]=1
                f=True
                pass
            
        if valida_mayor1(4, 2) == False and f!= False:
            f2c4=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(14)).grid(row=12, column=6)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[4][2]=0
            f=False

        elif valida_mayor2(4, 2) == False and f!= False:
            f2c4=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(14)).grid(row=12, column=6)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[4][2]=0
            f=False

        if gane() == True:
            #showMensaje("Ganó")
            mensaje_gane()

#_________________________________________________________________________________________________________________________________________________

    elif cod == 15:
        if isinstance(matriz_juego[0][3],str):
            showMensaje("JUGADA NO ES VÁLIDA PORQUE ESTE ES UN DÍGITO FIJO")
            return
        apila(matriz_juego[0][3], 0, 3,"#F4B860", 15, 4, 8)
        matriz_juego[0][3]= numero
        for i,num in enumerate(matriz_juego[0]):
            if numero == int(matriz_juego[1][3]) or numero == int(matriz_juego[2][3]) or numero == int(matriz_juego[3][3]) or numero == int(matriz_juego[4][3]):
                f3c0=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(15)).grid(row=4, column=8)
                showMensaje("El numero " + str(numero) + " ya esta en la columna")
                matriz_0_1[0][3]=0
                f= False
                break
            
            elif int(num) == numero and i != 3:
                f3c0=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(15)).grid(row=4, column=8)
                showMensaje("El numero " + str(numero)+ " ya esta en la fila")
                matriz_0_1[0][3]=0
                f= False
                break
            
            else:
                f3c0=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(15)).grid(row=4, column=8)
                matriz_0_1[0][3]=1
                f=True
                pass
            
        if valida_mayor1(0, 3) == False and f!= False:
            f3c0=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(15)).grid(row=4, column=8)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[0][3]=0
            f=False
        
        elif valida_mayor2(0, 3) == False and f!= False:
            f3c0=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(15)).grid(row=4, column=8)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[0][3]=0
            f=False

        if gane() == True:
            #showMensaje("Ganó")
            mensaje_gane()

        
    elif cod == 16:
        if isinstance(matriz_juego[1][3],str):
            showMensaje("JUGADA NO ES VÁLIDA PORQUE ESTE ES UN DÍGITO FIJO")
            return
        apila(matriz_juego[1][3], 1, 3,"#F4B860", 16, 6, 8)
        matriz_juego[1][3]= numero
        for i,num in enumerate(matriz_juego[1]):
            if numero == int(matriz_juego[0][3]) or numero == int(matriz_juego[2][3]) or numero == int(matriz_juego[3][3]) or numero == int(matriz_juego[4][3]):
                f3c1=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(16)).grid(row=6, column=8)
                showMensaje("El numero " + str(numero) + " ya esta en la columna")
                matriz_0_1[1][3]=0
                f= False
                break
            
            elif int(num) == numero and i != 3:
                f3c1=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(16)).grid(row=6, column=8)
                showMensaje("El numero " + str(numero)+ " ya esta en la fila")
                matriz_0_1[1][3]=0
                f= False
                break

            else:
                f3c1=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(16)).grid(row=6, column=8)
                matriz_0_1[1][3]=1
                f=True
                pass
            
        if valida_mayor1(1, 3) == False and f!= False:
            f3c1=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(16)).grid(row=6, column=8)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[1][3]=0
            f=False
        
        elif valida_mayor2(1, 3) == False and f!= False:
            f3c1=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(16)).grid(row=6, column=8)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[1][3]=0
            f=False

        if gane() == True:
            #showMensaje("Ganó")
            mensaje_gane()
            
    
    elif cod == 17:
        if isinstance(matriz_juego[2][3],str):
            showMensaje("JUGADA NO ES VÁLIDA PORQUE ESTE ES UN DÍGITO FIJO")
            return
        apila(matriz_juego[2][3], 2, 3,"#F4B860", 17, 8, 8)
        matriz_juego[2][3]= numero
        for i,num in enumerate(matriz_juego[2]):
            if numero == int(matriz_juego[0][3]) or numero == int(matriz_juego[1][3]) or numero == int(matriz_juego[3][3]) or numero == int(matriz_juego[4][3]):
                f3c2=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(17)).grid(row=8, column=8)
                showMensaje("El numero " + str(numero) + " ya esta en la columna")
                matriz_0_1[2][3]=0
                f= False
                break
            
            elif int(num) == numero and i != 3:
                f3c2=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(17)).grid(row=8, column=8)
                showMensaje("El numero " + str(numero)+ " ya esta en la fila")
                matriz_0_1[2][3]=0
                f=True
                return

            else:
                f3c2=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(17)).grid(row=8, column=8)
                matriz_0_1[2][3]=1
                f= False
                break
            
        if valida_mayor1(2, 3) == False and f!= False:
            f3c2=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(17)).grid(row=8, column=8)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[2][3]=0
            f=False
        
        elif valida_mayor2(2, 3) == False and f!= False:
            f3c2=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(17)).grid(row=8, column=8)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[2][3]=0
            f=False

        if gane() == True:
            #showMensaje("Ganó")
            mensaje_gane()

    
    elif cod == 18:
        if isinstance(matriz_juego[2][4],str):
            showMensaje("JUGADA NO ES VÁLIDA PORQUE ESTE ES UN DÍGITO FIJO")
            return
        apila(matriz_juego[3][3], 3, 3,"#F4B860", 18, 10, 8)
        matriz_juego[3][3]= numero
        for i,num in enumerate(matriz_juego[3]):
            if numero == int(matriz_juego[0][3]) or numero == int(matriz_juego[1][3]) or numero == int(matriz_juego[2][3]) or numero == int(matriz_juego[4][3]):
                f3c3=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(18)).grid(row=10, column=8)
                showMensaje("El numero " + str(numero) + " ya esta en la columna")
                matriz_0_1[3][3]=0
                f= False
                break
            
            elif int(num) == numero and i != 3:
                f3c3=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(18)).grid(row=10, column=8)
                showMensaje("El numero " + str(numero)+ " ya esta en la fila")
                matriz_0_1[3][3]=0
                f= False
                break

            else:
                f3c3=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(18)).grid(row=10, column=8)
                matriz_0_1[3][3]=1
                f=True
                pass
            
        if valida_mayor1(3, 3) == False and f!= False:
            f3c3=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(18)).grid(row=10, column=8)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[3][3]=0
            f=False

        elif valida_mayor2(3, 3) == False and f!= False:
            f3c3=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(18)).grid(row=10, column=8)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[3][3]=0
            f=False 

        if gane() == True:
            #showMensaje("Ganó")
            mensaje_gane()

    
    elif cod == 19:
        if isinstance(matriz_juego[4][3],str):
            showMensaje("JUGADA NO ES VÁLIDA PORQUE ESTE ES UN DÍGITO FIJO")
            return
        apila(matriz_juego[4][3], 4, 3,"#F4B860", 19, 12, 8)
        matriz_juego[4][3]= numero
        for i,num in enumerate(matriz_juego[4]):
            if numero == int(matriz_juego[0][3]) or numero == int(matriz_juego[1][3]) or numero == int(matriz_juego[2][3]) or numero == int(matriz_juego[3][3]):
                f3c4=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(19)).grid(row=12, column=8)
                showMensaje("El numero " + str(numero) + " ya esta en la columna")
                matriz_0_1[4][3]=0
                f= False
                break
            
            elif int(num) == numero and i != 3:
                f3c4=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(19)).grid(row=12, column=8)
                showMensaje("El numero " + str(numero)+ " ya esta en la fila")
                matriz_0_1[4][3]=0
                f= False
                break

            else:
                f3c4=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(19)).grid(row=12, column=8)
                matriz_0_1[4][3]=1
                f=True
                pass
            
        if valida_mayor1(4, 3) == False and f!= False:
            f3c4=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(19)).grid(row=12, column=8)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[4][3]=0
            f=False

        elif valida_mayor2(4, 3) == False and f!= False:
            f3c4=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(19)).grid(row=12, column=8)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[4][3]=0
            f=False

        if gane() == True:
            #showMensaje("Ganó")
            mensaje_gane()

#________________________________________________________________________________________________________________________________________________
        
    elif cod == 20:
        if isinstance(matriz_juego[0][4],str):
            showMensaje("JUGADA NO ES VÁLIDA PORQUE ESTE ES UN DÍGITO FIJO")
            return
        apila(matriz_juego[0][4], 0, 4,"#F4B860", 20, 4, 10)
        matriz_juego[0][4]= numero
        for i,num in enumerate(matriz_juego[0]):
            if numero == int(matriz_juego[1][4]) or numero == int(matriz_juego[2][4]) or numero == int(matriz_juego[3][4]) or numero == int(matriz_juego[4][4]):
                f4c0=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(20)).grid(row=4, column=10)
                showMensaje("El numero " + str(numero) + " ya esta en la columna")
                matriz_0_1[0][4]=0
                f= False
                break
            
            elif int(num) == numero and i != 4:
                f4c0=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(20)).grid(row=4, column=10)
                showMensaje("El numero " + str(numero)+ " ya esta en la fila")
                matriz_0_1[0][4]=0
                f= False
                break
            
            else:
                f4c0=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(20)).grid(row=4, column=10)
                matriz_0_1[0][4]=1
                f=True
                pass
            
        if valida_mayor1(0, 4) == False and f!= False:
            f4c0=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(20)).grid(row=4, column=10)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[0][4]=0
            f=False
        
        elif valida_mayor2(0, 4) == False and f!= False:
            f4c0=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(20)).grid(row=4, column=10)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[0][4]=0
            f=False

        if gane() == True:
            #showMensaje("Ganó")
            mensaje_gane()


    
    elif cod == 21:
        if isinstance(matriz_juego[1][4],str):
            showMensaje("JUGADA NO ES VÁLIDA PORQUE ESTE ES UN DÍGITO FIJO")
            return
        apila(matriz_juego[1][4], 1, 4,"#F4B860", 21, 6, 10)
        matriz_juego[1][4]= numero
        for i,num in enumerate(matriz_juego[1]):
            if numero == int(matriz_juego[0][4]) or numero == int(matriz_juego[2][4]) or numero == int(matriz_juego[3][4]) or numero == int(matriz_juego[4][4]):
                f4c1=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(21)).grid(row=6, column=10)
                showMensaje("El numero " + str(numero) + " ya esta en la columna")
                matriz_0_1[1][4]=0
                f= False
                break
            
            elif int(num) == numero and i != 4:
                f4c1=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(21)).grid(row=6, column=10)
                showMensaje("El numero " + str(numero)+ " ya esta en la fila")
                matriz_0_1[1][4]=0
                f= False
                break
            
            else:
                f4c1=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(21)).grid(row=6, column=10)
                matriz_0_1[1][4]=1
                f=True
                pass
            
        if valida_mayor1(1, 4) == False and f!= False:
            f4c1=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(21)).grid(row=6, column=10)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[1][4]=0
            f=False
        
        elif valida_mayor2(1, 4) == False and f!= False:
            f4c1=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(21)).grid(row=6, column=10)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[1][4]=0
            f=False

        if gane() == True:
            #showMensaje("Ganó")
            mensaje_gane()


    elif cod == 22:
        if isinstance(matriz_juego[2][4],str):
            showMensaje("JUGADA NO ES VÁLIDA PORQUE ESTE ES UN DÍGITO FIJO")
            return
        apila(matriz_juego[2][4], 2, 4,"#F4B860", 22, 8, 10)
        matriz_juego[2][4]= numero
        for i,num in enumerate(matriz_juego[2]):
            if numero == int(matriz_juego[0][4]) or int(numero == matriz_juego[1][4]) or numero == int(matriz_juego[3][4]) or numero == int(matriz_juego[4][4]):
                f4c2=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(22)).grid(row=8, column=10)
                showMensaje("El numero " + str(numero) + " ya esta en la columna")
                matriz_0_1[2][4]=0
                f= False
                break
            
            elif int(num) == numero and i != 4:
                f4c2=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(22)).grid(row=8, column=10)
                showMensaje("El numero " + str(numero)+ " ya esta en la fila")
                matriz_0_1[2][4]=0
                f= False
                break
            
            else:
                f4c2=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(22)).grid(row=8, column=10)
                matriz_0_1[2][4]=1
                f=True
                pass
            
        if valida_mayor1(2, 4) == False and f!= False:
            f4c2=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(22)).grid(row=8, column=10)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[2][4]=0
            f=False

        elif valida_mayor2(2, 4) == False and f!= False:
            f4c2=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(22)).grid(row=8, column=10)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[2][4]=0
            f=False

        if gane() == True:
            #showMensaje("Ganó")
            mensaje_gane()


    
    elif cod == 23:
        if isinstance(matriz_juego[3][4],str):
            showMensaje("JUGADA NO ES VÁLIDA PORQUE ESTE ES UN DÍGITO FIJO")
            return
        apila(matriz_juego[3][4], 3, 4,"#F4B860", 23, 10, 10)
        matriz_juego[3][4]= numero
        for i,num in enumerate(matriz_juego[3]):
            if numero == int(matriz_juego[0][4]) or numero == int(matriz_juego[1][4]) or numero == int(matriz_juego[2][4]) or numero == int(matriz_juego[4][4]):
                f4c3=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(23)).grid(row=10, column=10)
                showMensaje("El numero " + str(numero) + " ya esta en la columna")
                matriz_0_1[3][4]=0
                f= False
                break
            
            elif int(num) == numero and i != 4:
                f4c3=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(23)).grid(row=10, column=10)
                showMensaje("El numero " + str(numero)+ " ya esta en la fila")
                matriz_0_1[3][4]=0
                f= False
                break
            
            else:
                f4c3=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(23)).grid(row=10, column=10)
                matriz_0_1[3][4]=1
                f=True
                pass
            
        if valida_mayor1(3, 4) == False and f!= False:
            f4c3=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(23)).grid(row=10, column=10)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[3][4]=0
            f=False
        
        elif valida_mayor2(3, 4) == False and f!= False:
            f4c3=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(23)).grid(row=10, column=10)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[3][4]=0
            f=False

        if gane() == True:
            #showMensaje("Ganó")
            mensaje_gane()

   
    elif cod == 24:
        if isinstance(matriz_juego[4][4],str):
            showMensaje("JUGADA NO ES VÁLIDA PORQUE ESTE ES UN DÍGITO FIJO")
            return
        apila(matriz_juego[4][4], 4, 4,"#F4B860", 24, 12, 10)
        matriz_juego[4][4]= numero
        for i,num in enumerate(matriz_juego[4]):
            if numero == int(matriz_juego[0][4]) or numero == int(matriz_juego[1][4]) or numero == int(matriz_juego[2][4]) or numero == int(matriz_juego[3][4]):
                f4c4=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(24)).grid(row=12, column=10)
                matriz_0_1[4][4]=0
                f= False
                break
            
            elif int(num) == numero and i != 4:
                f4c4=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(24)).grid(row=12, column=10)
                showMensaje("El numero " + str(numero)+ " ya esta en la fila")
                matriz_0_1[4][4]=0
                f= False
                break
            
            else:
                f4c4=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(24)).grid(row=12, column=10)
                matriz_0_1[4][4]=1
                f=True
                pass
            
        if valida_mayor1(4, 4) == False and f!= False:
            f4c4=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(24)).grid(row=12, column=10)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[4][4]=0
            f=False
        
        elif valida_mayor2(4, 4) == False and f!= False:
            f4c4=tk.Button(ventana_a_jugar, text= numero, width= 5, height= 1, bg="#C83E4D",command=lambda:asigna_casilla(24)).grid(row=12, column=10)
            showMensaje("El numero " + str(numero)+ " no cumple con la restriccion")
            matriz_0_1[4][4]=0
            f=False

        if gane() == True:
            #showMensaje("Ganó")
            mensaje_gane()

def regresar_pr(ventana, cod):
    ventana.destroy()
    if cod==0:
        pass
    else:
        cambio_valor_cr()
#Funcion para preguntar si desea terminar el juego
def termina_juego():
    ventana_tj=tk.Toplevel()
    ventana_tj.geometry("350x100")
    ventana_tj.title("FUTOSHIKI- Terminar el juego")
    ventana_tj.config(bg="#F4D6CC")
    
    nombre= tk.Label(ventana_tj, text= "¿Esta seguro de que desea terminar el juego?", font= "Corbel 12 bold ", bg="#F4CFB1")
    nombre.place(x=5, y=5)

    regresar_b= tk.Button(ventana_tj, text= "No",font= "Corbel 12", bg="#F4CFB1", command= lambda:regresar_tj(ventana_tj, 0))
    regresar_b.place(x=45, y=50)

    regresar_b= tk.Button(ventana_tj, text= "Sí",font= "Corbel 12", bg="#F4CFB1", command= lambda:regresar_tj(ventana_tj, 1))
    regresar_b.place(x=85, y=50)

def regresar_tj(ventana, cod):
    global ventana_a_jugar
    if cod == 0:
        pass
    elif cod == 1:
        ventana_a_jugar.destroy()
        a_jugar()
    ventana.destroy()
    
#Funcion para borrar el juego actual
def borrar_juego(nombre_jugador):
    ventana_bj=tk.Toplevel()
    ventana_bj.geometry("350x100")
    ventana_bj.title("FUTOSHIKI- Terminar el juego")
    ventana_bj.config(bg="#F4D6CC")
    
    nombre= tk.Label(ventana_bj, text= "¿Esta seguro de que desa borrar el juego?", font= "Corbel 12 bold ", bg="#F4CFB1")
    nombre.place(x=5, y=5)

    regresar_b= tk.Button(ventana_bj, text= "No",font= "Corbel 12", bg="#F4CFB1", command= lambda:regresar_bj(ventana_bj,0, nombre_jugador))
    regresar_b.place(x=45, y=50)

    regresar_b= tk.Button(ventana_bj, text= "Sí",font= "Corbel 12", bg="#F4CFB1", command= lambda:regresar_bj(ventana_bj,1, nombre_jugador))
    regresar_b.place(x=85, y=50)
    
def regresar_bj(ventana, cod, nombre_jugador):
    global ind_escoge_par
    global ventana_a_jugar
    if cod == 0:
        pass
    elif cod == 1:
        ind_escoge_par=0
        carga_juego(nombre_jugador)
    ventana.destroy()

def carga_juego(nombre_jugador):
    global flag_cargar_juego
    global arc_jugadas
    global matriz_juego
    global numero
    global partida
    global num
    global hora_inicio
    global reloj_o_time
    global nombre_j
    global flag_cargar_juego
    global lista_pila
    global nivel_dificultad
    global ind_escoge_par

    global min_timer
    global hora_timer
    global seg_timer

    lista_pila= []
    arc_jugadas=asigna_datos("futoshiki2021partidas.dat")
    #print(arc_jugadas)

    if flag_cargar_juego == False:
        nombre_jugador=str(nombre_jugador)
        largo = len(nombre_jugador)
        num=escoge_partida()
        
        if len(nombre_jugador) < 1 or len(nombre_jugador) > 20:
            showMensaje("Nombre no es valido")
            return
        
        nombre_j=nombre_jugador
       # partida1=arc_jugadas[num]
        
        if nivel_dificultad == 1 and ind_escoge_par == 1:
            partida= arc_jugadas[0][num]
            
        if nivel_dificultad == 2 and ind_escoge_par == 1:
            partida= arc_jugadas[1][num]
            
        if nivel_dificultad == 3 and ind_escoge_par == 1:
            partida = arc_jugadas[2][num]
            
        crea_matriz()
        if ind_escoge_par == 1:
            hora_inicio= obtener_hora()
        print(hora_inicio)
    
    if reloj_o_time == 1:
        seg_actual.after(1000, lambda:funcion_time())
    elif reloj_o_time == 3:
        seg_actual.after(1000, lambda:timer_reloj())
    
    signo0=tk.Label(ventana_a_jugar,text="   ",bg="#F4D6CC").grid(row=4, column=3)
    signo1=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC").grid(row=4, column=5)
    signo2=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=4, column=7)
    signo3=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=4, column=9)
    
    signo4=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=6, column=3)
    signo5=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=6, column=5)
    signo6=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=6, column=7)
    signo7=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=6, column=9)
 
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=8, column=3)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=8, column=5)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=8, column=7)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=8, column=9)
    
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=10, column=3)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=10, column=5)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=10, column=7)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=10, column=9)
    
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=5, column=2)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=5, column=4)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=5, column=6)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=5, column=8)

    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=7, column=2)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=7, column=4)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=7, column=6)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=7, column=8)
    
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=9, column=2)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=9, column=4)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=9, column=6)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=9, column=8)

    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=11, column=2)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=11, column=4)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=11, column=6)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=11, column=8)

    

    for validacion in partida:
        if validacion[0] not in "1 2 3 4 5":
            #print(validacion)
            validacion1=validacion[1]
            validacion2=validacion[2]
            
            if validacion[0] == "˄" or validacion[0] == "˅":
                if validacion1 == 0:
                    validacion1=5
                elif validacion1==1:
                    validacion1=7
                elif validacion1==2:
                    validacion1=9
                elif validacion1==3:
                    validacion1=11

                if validacion2 == 0:
                    validacion2= 2
                elif validacion2==1:
                    validacion2=4
                elif validacion2==2:
                    validacion2=6
                elif validacion2==3:
                    validacion2=8
                elif validacion2==4:
                    validacion2=10

                signo=tk.Label(ventana_a_jugar, text= validacion[0],font= "bold", bg="#F4D6CC",).grid(row=validacion1, column=validacion2)
                #print("Val1", validacion1,validacion2)
    
            if validacion[0] == ">" or validacion[0] == "<":
                if validacion2 == 0:
                    validacion2=3
                elif validacion2==1:
                    validacion2=5
                elif validacion2==2:
                    validacion2=7
                elif validacion2==3:
                    validacion2=9
                    
                if validacion1 == 0:
                    validacion1=4
                elif validacion1==1:
                    validacion1=6
                elif validacion1==2:
                    validacion1=8
                elif validacion1==3:
                    validacion1=10
                elif validacion1==4:
                    validacion1=12
                
                
                signo=tk.Label(ventana_a_jugar, text= validacion[0],font="Corbel 13 bold", bg="#F4D6CC",).grid(row=validacion1, column=validacion2)

        else:
            matriz_juego[validacion[1]][validacion[2]]=str(validacion[0])
            matriz_0_1[validacion[1]][validacion[2]]=1
            
    #print(matriz_juego)

    if matriz_juego[0][0] !=0:
        f0c0=tk.Button(ventana_a_jugar, text= matriz_juego[0][0], width= 5, height= 1, bg="#F4B860", command=lambda:asigna_casilla(0)).grid(row=4, column=2)
    else:
        f0c0=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860", command=lambda:asigna_casilla(0)).grid(row=4, column=2)

    if matriz_juego[1][0] !=0:
        f0c1=tk.Button(ventana_a_jugar, text= matriz_juego[1][0], width= 5, height= 1, bg="#F4B860", command=lambda:asigna_casilla(1)).grid(row=6, column=2)
    else:
        f0c1=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860", command=lambda:asigna_casilla(1)).grid(row=6, column=2)

    if matriz_juego[2][0] !=0:
        f0c2=tk.Button(ventana_a_jugar, text= matriz_juego[2][0], width= 5, height= 1, bg="#F4B860", command=lambda:asigna_casilla(2)).grid(row=8, column=2)
    else:
        f0c2=tk.Button(ventana_a_jugar, text="", width= 5, height= 1, bg="#F4B860", command=lambda:asigna_casilla(2)).grid(row=8, column=2)

    if matriz_juego[3][0] !=0:
        f0c3=tk.Button(ventana_a_jugar, text= matriz_juego[3][0], width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(3)).grid(row=10, column=2)
    else:
        f0c3=tk.Button(ventana_a_jugar, text= "" , width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(3)).grid(row=10, column=2)
        
        
    if matriz_juego[4][0] !=0:
        f0c4=tk.Button(ventana_a_jugar, text= matriz_juego[4][0], width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(4)).grid(row=12, column=2)
    else:
        f0c4=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(4)).grid(row=12, column=2)
        
    #1_______________________________________________________________________________________________________________________________________________________
                
    if matriz_juego[0][1] !=0:
        f1c0=tk.Button(ventana_a_jugar, text= matriz_juego[0][1], width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(5)).grid(row=4, column=4)
    else:
        f1c0=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(5)).grid(row=4, column=4)

    if matriz_juego[1][1] !=0:
        f1c1=tk.Button(ventana_a_jugar, text= matriz_juego[1][1], width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(6)).grid(row=6, column=4)
    else:
        f1c1=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(6)).grid(row=6, column=4)
        

    if matriz_juego[2][1] !=0:
        f1c2=tk.Button(ventana_a_jugar, text= matriz_juego[2][1], width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(7)).grid(row=8, column=4)
    else:
        f1c2=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(7)).grid(row=8, column=4)
        

    if matriz_juego[3][1] !=0:
        f1c3=tk.Button(ventana_a_jugar, text= matriz_juego[3][1], width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(8)).grid(row=10, column=4)
    else:
        f1c3=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(8)).grid(row=10, column=4)

    if matriz_juego[4][1] !=0:
        f1c4=tk.Button(ventana_a_jugar, text= matriz_juego[4][1], width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(9)).grid(row=12, column=4)
    else:
        f1c4=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(9)).grid(row=12, column=4)
        
    #1_______________________________________________________________________________________________________________________________________________________
                
    if matriz_juego[0][2] !=0:
        f2c0=tk.Button(ventana_a_jugar, text= matriz_juego[0][2], width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(10)).grid(row=4, column=6)
    else:
        f2c0=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(10)).grid(row=4, column=6)
        

    if matriz_juego[1][2] !=0:
        f2c1=tk.Button(ventana_a_jugar, text= matriz_juego[1][2], width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(11)).grid(row=6, column=6)
    else:
        f2c1=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(11)).grid(row=6, column=6)
        

    if matriz_juego[2][2] !=0:
        f2c2=tk.Button(ventana_a_jugar, text= matriz_juego[2][2], width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(12)).grid(row=8, column=6)
    else:
        f2c2=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(12)).grid(row=8, column=6)
        
    if matriz_juego[3][2] !=0:
        f2c3=tk.Button(ventana_a_jugar, text= matriz_juego[3][2], width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(13)).grid(row=10, column=6)
    else:
        f2c3=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(13)).grid(row=10, column=6)

    if matriz_juego[4][2] !=0:
        f2c4=tk.Button(ventana_a_jugar, text= matriz_juego[4][2], width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(14)).grid(row=12, column=6)
    else:
        f2c4=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(14)).grid(row=12, column=6) 
    #3_______________________________________________________________________________________________________________________________________________________
                
    if matriz_juego[0][3] !=0:
        f3c0=tk.Button(ventana_a_jugar, text= matriz_juego[0][3], width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(15)).grid(row=4, column=8)
    else:
        f3c0=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(15)).grid(row=4, column=8)

    if matriz_juego[1][3] !=0:
        f3c1=tk.Button(ventana_a_jugar, text=matriz_juego[1][3], width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(16)).grid(row=6, column=8)
    else:
        f3c1=tk.Button(ventana_a_jugar, text="", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(16)).grid(row=6, column=8)

    if matriz_juego[2][3] !=0:
        f3c2=tk.Button(ventana_a_jugar, text= matriz_juego[2][3],width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(17)).grid(row=8, column=8)
    else:
        f3c2=tk.Button(ventana_a_jugar, text= "",width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(17)).grid(row=8, column=8)
        

    if matriz_juego[3][3] !=0:
        f3c3=tk.Button(ventana_a_jugar, text= matriz_juego[3][3], width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(18)).grid(row=10, column=8)
    else:
        f3c3=tk.Button(ventana_a_jugar, text="", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(18)).grid(row=10, column=8)

    if matriz_juego[4][3] !=0:
        f3c4=tk.Button(ventana_a_jugar, text= matriz_juego[4][3], width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(19)).grid(row=12, column=8)
    else:
        f3c4=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(19)).grid(row=12, column=8)
        
    #4_______________________________________________________________________________________________________________________________________________________
                
    if matriz_juego[0][4] !=0:
        f4c0=tk.Button(ventana_a_jugar, text= matriz_juego[0][4], width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(20)).grid(row=4, column=10)
    else:
        f4c0=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(20)).grid(row=4, column=10)

    if matriz_juego[1][4] !=0:
        f4c1=tk.Button(ventana_a_jugar, text=matriz_juego[1][4], width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(21)).grid(row=6, column=10)
    else:
        f4c1=tk.Button(ventana_a_jugar, text="", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(21)).grid(row=6, column=10)

    if matriz_juego[2][4] !=0:
        f4c2=tk.Button(ventana_a_jugar, text= matriz_juego[2][4], width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(22)).grid(row=8, column=10)
    else:
        f4c2=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(22)).grid(row=8, column=10)

    if matriz_juego[3][4] !=0:
        f4c3=tk.Button(ventana_a_jugar, text= matriz_juego[3][4], width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(23)).grid(row=10, column=10)
    else:
        f4c3=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(23)).grid(row=10, column=10)

    if matriz_juego[4][4] !=0:
        f4c4=tk.Button(ventana_a_jugar, text= matriz_juego[4][4], width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(24)).grid(row=12, column=10)
    else:
        f4c4=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(24)).grid(row=12, column=10)
    
    return partida

    

#___________________________________________________________VENTANA_CONFIGURACION________________________________________________________________________
'''
Funcion para crear la ventana de configuracion
'''
def configuracion():
    global nivel_dificultad
    global reloj_o_time
    global lado_num
    
    ventana_principal.state(newstate="withdraw")
    ventana_configuracion= tk.Tk()
    ventana_configuracion.geometry("600x600")
    ventana_configuracion.title("FUTOSHIKI- A jugar")
    ventana_configuracion.config(bg="#F4D6CC")

    name_label= tk.Label(ventana_configuracion, text= "FUTOSHIKI", font= "Corbel 22 bold", height= 1, width= 15, bg= "#C83E4D")
    name_label.grid(row=0, column=1)

    nivel_label= tk.Label(ventana_configuracion, text= "1. Nivel", font= "Corbel 12 bold", width= 8, bg= "#F4D6CC")
    nivel_label.grid(row=2, column=0)

    reloj_label= tk.Label(ventana_configuracion, text= "2. Reloj", font= "Corbel 12 bold", width= 8, bg= "#F4D6CC")
    reloj_label.grid(row=5, column=0)

    lado_label= tk.Label(ventana_configuracion, text= "3. Pocision de panel de digitos", font= "Corbel 12 bold", bg= "#F4D6CC")
    lado_label.place(x=0, y=250)


    #Radiosbutton
    nivel_dificultad= tk.IntVar()
    nivel_dificultad.set(asigna_nivel(1))
    
    facil_rb= tk.Radiobutton(ventana_configuracion, text= "Facil",font= "Corbel 12", width= 8,\
                             bg= "#F4D6CC",variable= nivel_dificultad , value=1, command= lambda:asigna_nivel(1))
    facil_rb.grid(row=2, column=1)

    intermedio_rb= tk.Radiobutton(ventana_configuracion, text= "Intermedio",font= "Corbel 12", width= 8,\
                                  bg= "#F4D6CC",variable= nivel_dificultad ,value=2, command= lambda:asigna_nivel(2))
    intermedio_rb.grid(row=3, column=1)

    dificil_rb= tk.Radiobutton(ventana_configuracion, text= "Dificil",font= "Corbel 12", width= 8,\
                               bg= "#F4D6CC",variable= nivel_dificultad , value=3, command= lambda:asigna_nivel(3))
    dificil_rb.grid(row=4, column=1)
    

    reloj_o_time= tk.IntVar()
    reloj_o_time.set(cambia_op_time(1))
    
    s_reloj_rb= tk.Radiobutton(ventana_configuracion, text= "Sí",font= "Corbel 12", width= 8,\
                             bg= "#F4D6CC",variable= reloj_o_time , value=1, command= lambda:cambia_op_time(1)).grid(row=5, column=1)

    n_reloj_rb= tk.Radiobutton(ventana_configuracion, text= "No",font= "Corbel 12", width= 8,\
                                  bg= "#F4D6CC",variable= reloj_o_time ,value=2, command= lambda:cambia_op_time(2)).grid(row=6, column=1)

    timer_rb= tk.Radiobutton(ventana_configuracion, text= "Timer",font= "Corbel 12", width= 8,\
                               bg= "#F4D6CC",variable= reloj_o_time , value=3, command= lambda:cambia_op_time(3)).grid(row=7, column=1)

    reloj_o_time= tk.IntVar()
    
    s_reloj_rb= tk.Radiobutton(ventana_configuracion, text= "Sí",font= "Corbel 12", width= 8,\
                             bg= "#F4D6CC",variable= reloj_o_time , value=1, command= lambda:cambia_op_time(1)).grid(row=5, column=1)

    n_reloj_rb= tk.Radiobutton(ventana_configuracion, text= "No",font= "Corbel 12", width= 8,\
                                  bg= "#F4D6CC",variable= reloj_o_time ,value=2, command= lambda:cambia_op_time(2)).grid(row=6, column=1)

    timer_rb= tk.Radiobutton(ventana_configuracion, text= "Timer",font= "Corbel 12", width= 8,\
                               bg= "#F4D6CC",variable= reloj_o_time , value=3, command= lambda:cambia_op_time(3)).grid(row=7, column=1)

    lado_num= tk.IntVar()
    lado_num.set(cambia_lado_num(1))
    
    derecha_rb= tk.Radiobutton(ventana_configuracion, text= "Derecha",font= "Corbel 12", width= 8,\
                             bg= "#F4D6CC",variable= lado_num , value=1, command= lambda:cambia_lado_num(1)).place(x=250, y=250)

    izquierda_rb= tk.Radiobutton(ventana_configuracion, text= "Izquierta",font= "Corbel 12", width= 8,\
                                  bg= "#F4D6CC",variable= lado_num ,value=2, command= lambda:cambia_lado_num(0)).place(x=250, y=275)


    #Botones
    regresar_b= tk.Button(ventana_configuracion, text= "Regresar",font= "Corbel 12", width= 12, bg="#F4CFB1", command= lambda:regresar(ventana_configuracion))
    regresar_b.place(x=250, y=350)

def funcion_time():
    global reloj_o_time
    
    global hora_actual
    global min_actual
    global seg_actual
    global hora_inicio
    
    hora= time.strftime("%H")
    minutos= time.strftime("%M")
    seg= time.strftime("%S")
    hora_actual= tk.Label(ventana_a_jugar, text= hora,width= 9,height= 2,font= "Corbel 12", bg="#F4C796").place(x=10, y=475)
    min_actual= tk.Label(ventana_a_jugar, text= minutos,width= 9,height= 2,font= "Corbel 12", bg="#F4C796").place(x=95, y=475)
    seg_actual= tk.Label(ventana_a_jugar, text= seg,width= 9,height= 2,font= "Corbel 12", bg="#F4C796")
    seg_actual.place(x=180, y=475)
    seg_actual.after(1000, lambda:funcion_time())

def timer_reloj():
    global reloj_o_time
    global min_timer
    global hora_timer
    global seg_timer
    #print(min_timer,hora_timer, seg_timer)

    while seg_timer != 0 or min_timer !=0 or hora_timer != 0:
        if seg_timer == 0 and min_timer != 0:
            min_timer-=1
            seg_timer+=60
        elif min_timer == 0 and hora_timer !=0:
            hora_timer-=1
            min_timer+=59
        seg_timer-=1

        break
    hora_actual= tk.Label(ventana_a_jugar, text= hora_timer,width= 9,height= 2,font= "Corbel 12", bg="#F4C796").place(x=10, y=475)
    min_actual= tk.Label(ventana_a_jugar, text= min_timer,width= 9,height= 2,font= "Corbel 12", bg="#F4C796").place(x=95, y=475)
    seg_actual= tk.Label(ventana_a_jugar, text= seg_timer,width= 9,height= 2,font= "Corbel 12", bg="#F4C796")
    seg_actual.place(x=180, y=475)
    
    if seg_timer == 0 and min_timer == 0 and hora_timer == 0:
        fin_time()
        return
    else:
        seg_actual.after(1000, lambda:timer_reloj())
        
def fin_time():
    global ventana_a_jugar
    
    ventana_q=tk.Tk()
    ventana_q.geometry("400x200")
    ventana_q.title("FUTOSHIKI- Tiempo del cronometro")
    
    ventana_q.config(bg="#F4D6CC")

    nombre= tk.Label(ventana_q, text= "El tiempo se ha acabadabo, ¿Desea continuar?", font= "Corbel 12 bold ", bg="#F4CFB1")
    nombre.place(x=5, y=5)

    regresar_b= tk.Button(ventana_q, text= "No",font= "Corbel 12", bg="#F4CFB1", command= lambda:regresar_3(ventana_q, 0))
    regresar_b.place(x=45, y=50)

    regresar_b= tk.Button(ventana_q, text= "Sí",font= "Corbel 12", bg="#F4CFB1", command= lambda:regresar_3(ventana_q, 1))
    regresar_b.place(x=85, y=50)
    

def regresar_3(ventana, cod):
    global ventana_a_jugar
    
    if cod == 0:
        regresar(ventana_a_jugar)

    asigna_timer_o()
    ventana.destroy()
        
def asigna_timer_o():
    global min_timer_o
    global hora_timer_o
    global seg_timer_o
    global min_timer
    global hora_timer
    global seg_timer
    
    min_timer= min_timer_o
    seg_timer= seg_timer_o
    hora_timer= hora_timer_o

  
def guarda_juego():
    global matriz_juego
    global partida
    global nivel_dificultad
    global reloj_o_time
    global lado_num
    global num
    global hora_inicio
    global min_timer
    global hora_timer
    global seg_timer
    global flag_cargar_juego
    global matriz_0_1
    global nombre_j

    #juego_guardado= {m_juego:matriz_juego,par:partida, niv_dificultad: nivel_dificultad,reloj: reloj_o_time, l_num: lado_num}
    juego_guardado= [matriz_juego, matriz_0_1 ,nivel_dificultad, reloj_o_time, lado_num, hora_inicio, partida, nombre_j]
    if reloj_o_time==3:
        juego_guardado.append([hora_timer, min_timer,seg_timer])
        
    print(juego_guardado)
    

    arc= open("futoshiki2021juegoactual.dat" , "wb")
    pickle.dump(juego_guardado, arc)
    arc.close
    showMensaje("Ha sido guardado con exito")

def carga_partida():
    global matriz_juego
    global partida
    global nivel_dificultad
    global reloj_o_time
    global lado_num
    global num
    global hora_inicio
    global min_timer
    global hora_timer
    global seg_timer
    global matriz_0_1
    global nombre_j
    
    arc= open("futoshiki2021juegoactual.dat", "rb")
    flag_cargar_juego=True
    ventana_a_jugar.destroy()
    juego_guardado=pickle.load(arc)
    arc.close

    print(juego_guardado)
    matriz_juego= juego_guardado[0]
    matriz_0_1= juego_guardado[1]
    nivel_dificultad= juego_guardado[2]
    reloj_o_time= juego_guardado[3]
    lado_num= juego_guardado[4]
    hora_inicio=juego_guardado[5]
    nombre_j= juego_guardado[7]

    a_jugar()
    nombre_jugador1= tk.Label(ventana_a_jugar,text= nombre_j, width= 25, font= "Corbel 12 ", bg="#F4CFB1")
    nombre_jugador1.place(x=150, y=60)

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
    
    if matriz_juego[0][0] == 0:   
        f0c0=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860", command=lambda:asigna_casilla(0)).grid(row=4, column=2)
    else:
        f0c0=tk.Button(ventana_a_jugar, text= matriz_juego[0][0], width= 5, height= 1, bg="#F4B860", command=lambda:asigna_casilla(0)).grid(row=4, column=2)
        
    if matriz_juego[1][0] == 0:
        f0c1=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860", command=lambda:asigna_casilla(1)).grid(row=6, column=2)
    else:
        f0c1=tk.Button(ventana_a_jugar, text= matriz_juego[1][0], width= 5, height= 1, bg="#F4B860", command=lambda:asigna_casilla(1)).grid(row=6, column=2)

    if matriz_juego[2][0] == 0:
        f0c2=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860", command=lambda:asigna_casilla(2)).grid(row=8, column=2)
    else:
        f0c2=tk.Button(ventana_a_jugar, text= matriz_juego[2][0], width= 5, height= 1, bg="#F4B860", command=lambda:asigna_casilla(2)).grid(row=8, column=2)

    if matriz_juego[3][0] == 0:
        f0c3=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(3)).grid(row=10, column=2)
    else:
        f0c3=tk.Button(ventana_a_jugar, text= matriz_juego[3][0], width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(3)).grid(row=10, column=2)

    if matriz_juego[4][0] == 0:
        f0c4=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(4)).grid(row=12, column=2)
    else:
        f0c4=tk.Button(ventana_a_jugar, text= matriz_juego[4][0], width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(4)).grid(row=12, column=2)

    #----------------------------------------------------------------------------------------------------
    if matriz_juego[0][1] == 0:   
        f1c0=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(5)).grid(row=4, column=4)
    else:
        f1c0=tk.Button(ventana_a_jugar, text= matriz_juego[0][1], width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(5)).grid(row=4, column=4)
        
    if matriz_juego[1][1] == 0:   
        f1c1=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(6)).grid(row=6, column=4)
    else:
        f1c1=tk.Button(ventana_a_jugar, text= matriz_juego[1][1], width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(6)).grid(row=6, column=4)

    if matriz_juego[2][1] == 0:   
        f1c2=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(7)).grid(row=8, column=4)
    else:
        f1c2=tk.Button(ventana_a_jugar, text= matriz_juego[2][1], width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(7)).grid(row=8, column=4)

    if matriz_juego[3][1] == 0:   
        f1c3=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(8)).grid(row=10, column=4)
    else:
        f1c3=tk.Button(ventana_a_jugar, text= matriz_juego[3][1], width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(8)).grid(row=10, column=4)

    if matriz_juego[4][1] == 0:   
        f1c4=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(9)).grid(row=12, column=4)
    else:
        f1c4=tk.Button(ventana_a_jugar, text= matriz_juego[4][1], width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(9)).grid(row=12, column=4)
        
    #-----------------------------------------------------------------------------------------------------------------------------------
    if matriz_juego[0][2] == 0:   
        f2c0=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(10)).grid(row=4, column=6)
    else:
        f2c0=tk.Button(ventana_a_jugar, text= matriz_juego[0][2], width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(10)).grid(row=4, column=6)
        
    if matriz_juego[1][2] == 0:   
        f2c1=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(11)).grid(row=6, column=6)
    else:
        f2c1=tk.Button(ventana_a_jugar, text= matriz_juego[1][2], width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(11)).grid(row=6, column=6)

    if matriz_juego[2][2] == 0:   
        f2c2=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(12)).grid(row=8, column=6)
    else:
        f2c2=tk.Button(ventana_a_jugar, text= matriz_juego[2][2], width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(12)).grid(row=8, column=6)

    if matriz_juego[3][2] == 0:   
        f2c3=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(13)).grid(row=10, column=6)
    else:
        f2c3=tk.Button(ventana_a_jugar, text= matriz_juego[3][2], width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(13)).grid(row=10, column=6)

    if matriz_juego[4][2] == 0:   
        f2c4=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(14)).grid(row=12, column=6)
    else:
        f2c4=tk.Button(ventana_a_jugar, text= matriz_juego[4][2], width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(14)).grid(row=12, column=6)

    #-----------------------------------------------------------------------------------------------------------------------------------
    if matriz_juego[0][3] == 0:   
        f3c0=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(15)).grid(row=4, column=8)
    else:
        f3c0=tk.Button(ventana_a_jugar, text= matriz_juego[0][3], width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(15)).grid(row=4, column=8)
        
    if matriz_juego[1][3] == 0:   
        f3c1=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(16)).grid(row=6, column=8)
    else:
        f3c1=tk.Button(ventana_a_jugar, text= matriz_juego[1][3], width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(16)).grid(row=6, column=8)

    if matriz_juego[2][3] == 0:   
        f3c2=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(17)).grid(row=8, column=8)
    else:
        f3c2=tk.Button(ventana_a_jugar, text= matriz_juego[2][3], width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(17)).grid(row=8, column=8)

    if matriz_juego[3][3] == 0:   
        f3c3=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(18)).grid(row=10, column=8)
    else:
        f3c3=tk.Button(ventana_a_jugar, text= matriz_juego[3][3], width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(18)).grid(row=10, column=8)
        
    if matriz_juego[4][3] == 0:   
        f3c4=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(19)).grid(row=12, column=8)
    else:
        f3c4=tk.Button(ventana_a_jugar, text= matriz_juego[4][3], width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(19)).grid(row=12, column=8)            

#-----------------------------------------------------------------------------------------------------------------------------------
    if matriz_juego[0][4] == 0:   
        f4c0=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(20)).grid(row=4, column=10)
    else:
        f4c0=tk.Button(ventana_a_jugar, text= matriz_juego[0][4], width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(20)).grid(row=4, column=10)
        
    if matriz_juego[1][4] == 0:   
        f4c1=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(21)).grid(row=6, column=10)
    else:
        f4c1=tk.Button(ventana_a_jugar, text= matriz_juego[1][4], width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(21)).grid(row=6, column=10)

    if matriz_juego[2][4] == 0:   
        f4c2=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(22)).grid(row=8, column=10)
    else:
        f4c2=tk.Button(ventana_a_jugar, text= matriz_juego[2][4], width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(22)).grid(row=8, column=10)

    if matriz_juego[3][4] == 0:   
        f4c3=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(23)).grid(row=10, column=10)
    else:
        f4c3=tk.Button(ventana_a_jugar, text= matriz_juego[3][4], width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(23)).grid(row=10, column=10)
        
    if matriz_juego[4][4] == 0:   
        f4c4=tk.Button(ventana_a_jugar, text= "", width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(24)).grid(row=12, column=10)
    else:
        f4c4=tk.Button(ventana_a_jugar, text= matriz_juego[4][4], width= 5, height= 1, bg="#F4B860",command=lambda:asigna_casilla(24)).grid(row=12, column=10)
        

    signo0=tk.Label(ventana_a_jugar,text="   ",bg="#F4D6CC").grid(row=4, column=3)
    signo1=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC").grid(row=4, column=5)
    signo2=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=4, column=7)
    signo3=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=4, column=9)
    
    signo4=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=6, column=3)
    signo5=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=6, column=5)
    signo6=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=6, column=7)
    signo7=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=6, column=9)
 
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=8, column=3)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=8, column=5)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=8, column=7)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=8, column=9)
    
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=10, column=3)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=10, column=5)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=10, column=7)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=10, column=9)
    
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=5, column=2)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=5, column=4)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=5, column=6)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=5, column=8)

    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=7, column=2)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=7, column=4)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=7, column=6)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=7, column=8)
    
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=9, column=2)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=9, column=4)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=9, column=6)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=9, column=8)

    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=11, column=2)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=11, column=4)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=11, column=6)
    signo9=tk.Label(ventana_a_jugar,text="   ", bg="#F4D6CC",).grid(row=11, column=8)

    partida= juego_guardado[6]
    
    for validacion in partida:
        if validacion[0] not in "1 2 3 4 5":
            print(validacion)
            validacion1=validacion[1]
            validacion2=validacion[2]
            
            if validacion[0] == "˄" or validacion[0] == "˅":
                if validacion1 == 0:
                    validacion1=5
                elif validacion1==1:
                    validacion1=7
                elif validacion1==2:
                    validacion1=9
                elif validacion1==3:
                    validacion1=11

                if validacion2 == 0:
                    validacion2= 2
                elif validacion2==1:
                    validacion2=4
                elif validacion2==2:
                    validacion2=6
                elif validacion2==3:
                    validacion2=8
                elif validacion2==4:
                    validacion2=10

                signo=tk.Label(ventana_a_jugar, text= validacion[0],font= "bold", bg="#F4D6CC",).grid(row=validacion1, column=validacion2)
                #print("Val1", validacion1,validacion2)
    
            if validacion[0] == ">" or validacion[0] == "<":
                if validacion2 == 0:
                    validacion2=3
                elif validacion2==1:
                    validacion2=5
                elif validacion2==2:
                    validacion2=7
                elif validacion2==3:
                    validacion2=9
                    
                if validacion1 == 0:
                    validacion1=4
                elif validacion1==1:
                    validacion1=6
                elif validacion1==2:
                    validacion1=8
                elif validacion1==3:
                    validacion1=10
                elif validacion1==4:
                    validacion1=12
                
                
                signo=tk.Label(ventana_a_jugar, text= validacion[0],font="Corbel 13 bold", bg="#F4D6CC",).grid(row=validacion1, column=validacion2)
        if reloj_o_time != 2:
            hora_label= tk.Label(ventana_a_jugar, text= "Hora",width= 9, font= "Corbel 12", bg="#DB504A").place(x=10, y=450)
            min_label= tk.Label(ventana_a_jugar, text= "Minutos",width= 9, font= "Corbel 12 ", bg="#7A6174").place(x=95, y=450)
            seg_label= tk.Label(ventana_a_jugar, text= "Segundos",width= 9, font= "Corbel 12 ", bg="#6D8A96").place(x=180, y=450)

            hora_actual= tk.Label(ventana_a_jugar, text= "0",width= 9,height= 2,font= "Corbel 12", bg="#F4C796").place(x=10, y=475)
            min_actual= tk.Label(ventana_a_jugar, text= "0",width= 9,height= 2,font= "Corbel 12", bg="#F4C796").place(x=95, y=475)
            seg_actual= tk.Label(ventana_a_jugar, text= "0",width= 9,height= 2,font= "Corbel 12", bg="#F4C796")
            seg_actual.place(x=180, y=475)
            if reloj_o_time == 1:
                seg_actual.after(1000, lambda:funcion_time())
            elif reloj_o_time == 3:
                min_timer= juego_guardado[8][0]
                hora_timer= juego_guardado[8][1]
                seg_timer= juego_guardado[8][2]
                seg_actual.after(1000, lambda:timer_reloj())
                
        else:
            hora_label= tk.Label(ventana_a_jugar, text= "",width= 9, font= "Corbel 12", bg="#F4D6CC").place(x=10, y=450)
            min_label= tk.Label(ventana_a_jugar, text= "",width= 9, font= "Corbel 12 ", bg="#F4D6CC").place(x=95, y=450)
            seg_label= tk.Label(ventana_a_jugar, text= "",width= 9, font= "Corbel 12 ", bg="#F4D6CC").place(x=180, y=450)

            hora_actual= tk.Label(ventana_a_jugar, text= "",width= 9,height= 2,font= "Corbel 12", bg="#F4D6CC").place(x=10, y=475)
            min_actual= tk.Label(ventana_a_jugar, text= " ",width= 9,height= 2,font= "Corbel 12", bg="#F4D6CC").place(x=95, y=475)
            seg_actual= tk.Label(ventana_a_jugar, text= " ",width= 9,height= 2,font= "Corbel 12", bg="#F4D6CC")
            seg_actual.place(x=180, y=475)

   
 
def escoge_partida():
    global num
    num= ran.randint(0,2)
    return num        
            
        
#Funcion para obttener la hora actual
'''
  Entradas: NE
  Salidas: Retorna la hora actual
  Restricciones: NE
'''
def obtener_hora():
    #global hora_inicio

    #global hora_fin
    hora= time.strftime("%H")
    minutos= time.strftime("%M")
    seg= time.strftime("%S")
    hora_actual=(hora+ ":" + minutos + ":" + seg)
    return hora_actual


#________________________________
'''
Funcion qque verifica restricciones de mayor y menor que
Entradas:indices en la matriz
Salidas: retorna False si no cumple con la restriccion y True si sí la cumple
'''

def valida_mayor2(ind_fila, ind_columna):
    global partida
    global matriz_juego
    global numero
    for validacion in partida:
        if validacion[1] == ind_fila:
            if validacion[2]+1 == ind_columna:
                try:
                    if matriz_juego[ind_fila][ind_columna] == 0 or int(matriz_juego[ind_fila][ind_columna-1])== 0:
                        return True
                        
                    else:
                        if validacion[0] == ">":
                            if int(matriz_juego[ind_fila][ind_columna]) > int(matriz_juego[ind_fila][ind_columna-1]):
                                return False
                        elif validacion[0] == "<":
                            if int(matriz_juego[ind_fila][ind_columna]) < int(matriz_juego[ind_fila][ind_columna-1]):
                                return False
                except:
                    pass
                
        elif validacion[1]+1 == ind_fila:
            if validacion[2] == ind_columna:
                try:
                    #print(matriz_juego[ind_fila][ind_columna])
                    if matriz_juego[ind_fila][ind_columna] == 0 or int(matriz_juego[ind_fila-1][ind_columna]) == 0:
                        return True
                    
                    else:
                        if validacion[0] == "˄":
                            if int(matriz_juego[ind_fila][ind_columna]) < int(matriz_juego[ind_fila-1][ind_columna]):
                                return False
                        elif validacion[0] == "˅":
                            if int(matriz_juego[ind_fila][ind_columna]) > int(matriz_juego[ind_fila-1][ind_columna]):
                                return False
                except:
                    pass
                
    return True


def valida_mayor1(ind_fila, ind_columna):
    global partida
    global matriz_juego
    global numero
    for validacion in partida:
        if validacion[1] == ind_fila:
            if validacion[2] == ind_columna:
                #print("1", validacion)
                #print(matriz_juego)
                #print(matriz_juego[ind_fila][ind_columna], matriz_juego[ind_fila][ind_columna+1])
                try:
                    if matriz_juego[ind_fila][ind_columna] == 0:
                        break
                    
                    
                    else:
                        if validacion[0] == ">":
                            if int(matriz_juego[ind_fila][ind_columna+1]) ==0:
                                break
                            if int(matriz_juego[ind_fila][ind_columna]) < int(matriz_juego[ind_fila][ind_columna+1]):
                                return False
                        elif validacion[0] == "˄":
                            if matriz_juego[ind_fila+1][ind_columna] == 0:
                                break
                            if int(matriz_juego[ind_fila][ind_columna]) > int(matriz_juego[ind_fila+1][ind_columna]):
                                return False
                            
                        elif validacion[0] == "<":
                            if int(matriz_juego[ind_fila][ind_columna+1]) ==0:
                                break
                            if int(matriz_juego[ind_fila][ind_columna]) < int(matriz_juego[ind_fila][ind_columna+1]):
                                return False
                            
                        elif validacion[0] == "˅":
                            if matriz_juego[ind_fila+1][ind_columna] == 0:
                                break
                            if int(matriz_juego[ind_fila][ind_columna]) < int(matriz_juego[ind_fila+1][ind_columna]):
                                return False
                except:
                    print("Error 3")
                    break
    return True    

def asigna_nivel(num):
    global nivel_dificultad
    if num== 1:
        nivel_dificultad=1
    elif num == 2:
        nivel_dificultad=2
    elif num == 3:
        nivel_dificultad=3

    print(nivel_dificultad)

def cambia_op_time(num):
    global reloj_o_time
    if num == 1:
        reloj_o_time= 1
    elif num == 2:
        reloj_o_time= 2
    elif num == 3:
        reloj_o_time= 3
        cambio_valor_cr()
    print(reloj_o_time)


def cambio_valor_cr():
    global ventana_cr
    ventana_cr=tk.Tk()
    ventana_cr.geometry("400x200")
    ventana_cr.title("FUTOSHIKI- Tiempo del cronometro")
    ventana_cr.config(bg="#F4D6CC")

    nombre= tk.Label(ventana_cr, text= "Tiempo del cronometro", font= "Corbel 12 bold ", bg="#F4CFB1")
    nombre.place(x=110, y=5)
    
    nombre= tk.Label(ventana_cr, text= "Horas: ", font= "Corbel 12 ", bg="#F4CFB1")
    nombre.place(x=10, y=40)

    nombre= tk.Label(ventana_cr, text= "Minutos: ", font= "Corbel 12 ", bg="#F4CFB1")
    nombre.place(x=10, y=70)

    nombre= tk.Label(ventana_cr, text= "Segundos: ", font= "Corbel 12 ", bg="#F4CFB1")
    nombre.place(x=10, y=100)

    horas=tk.Entry(ventana_cr, font= "12 ", bg="#F4CFB1")
    horas.place(x=100, y=40)

    minutos=tk.Entry(ventana_cr, font= "12 ", bg="#F4CFB1")
    minutos.place(x=100, y=70)

    seg=tk.Entry(ventana_cr, font= "12 ", bg="#F4CFB1")
    seg.place(x=100, y=100)

    regresar_b= tk.Button(ventana_cr, text= "Ok",font= "Corbel 12", width= 12, bg="#F4CFB1", command= lambda:valor_cr(horas.get(), minutos.get(), seg.get()))
    regresar_b.place(x=75, y=130)
    
def valor_cr(horas, minutos, segundos):
    global min_timer
    global hora_timer
    global seg_timer

    global min_timer_o
    global hora_timer_o
    global seg_timer_o
    
    global ventana_cr

    if int(horas) < 0 or int(horas) > 2:
        showMensaje("El valor en las horas no es valido")
        return
    else:
        hora_timer=int(horas)
        hora_timer_o=int(horas)
        
    if int(minutos) < 0 or int(minutos) > 59:
        showMensaje("El valor en los minutos no es valido")
        return
    else:
        min_timer= int(minutos)
        min_timer_o= int(minutos)

    if int(segundos) < 0 or int(segundos) > 59:
        showMensaje("El valor en los segundos no es valido")
        return
    else:
        seg_timer= int(segundos)
        seg_timer_o= int(segundos)

    if hora_timer==0 and min_timer==0 and seg_timer==0:
        showMensaje("Al menor 1 de los valores debe ser != 0")
        return
    else:
        pass

    ventana_cr.destroy()
    

    
def cambia_lado_num(num):
    global lado_num
    if num== 1:
        lado_num=1
    else:
        lado_num=0
    print(lado_num)

#Funcion para saber si se gana o no
def gane():
    global matriz_0_1
    global hora_fin
    for fila in matriz_0_1:
        for columna in fila:
            if columna == 0:
                return
    hora_fin= obtener_hora()
    diferencia= diferencia_horas()
    
    return True

#Calculo de diferencia entre hora de entrdada y hora de salida
'''
  Entradas: Recibe la fecha y hora actual
  Salidas: Calcula es costo total y saca horas y minutos diferencia
  Restricciones: NE
'''
def diferencia_horas():
    global hora_fin
    global hora_inicio
    
    format_hora= "%H:%M:%S"
    hora_i= datetime.strptime(hora_inicio, format_hora) #tipo date time, tipo time
    hora_f= datetime.strptime(hora_fin, format_hora)

    
    total_horas= hora_f - hora_i
    l_total_horas=str(total_horas).split(":")
    
    total_hora= l_total_horas[0]
    total_min= l_total_horas[1]
    total_seg=l_total_horas[2]
    return total_hora, total_min, total_seg


def mensaje_gane():
    ventana_gane=tk.Tk()
    ventana_gane.geometry("400x200")
    ventana_gane.title("FUTOSHIKI- Felicidades")
    ventana_gane.config(bg="#F4D6CC")

    nombre= tk.Label(ventana_gane, text= "Ha completado la partida exitosamente", font= "Corbel 14 bold ", bg="#F4CFB1")
    nombre.place(x=5, y=5)
    
    regresar_b= tk.Button(ventana_gane, text= "Regresar al menu principal",font= "Corbel 12", bg="#F4CFB1", command= lambda:regresar_4(ventana_gane, 0))
    regresar_b.place(x=75, y=130)

def regresar_4(ventana, cod):
    global ventana_a_jugar
    
    if cod == 0:
        regresar(ventana_a_jugar)

    ventana.destroy()

#Funciones que trabajan con la pila de operaciones-----------------------------
'''
APPEND
Funcion para apilar
Entradas: Numero
Salidas: lista con los valores apilados
'''
def apila(numero, indice_fila, indice_columna,color, codigo, p_row, p_column):
    global matriz_juego
    global lista_pila
    global matriz_0_1
    
    valor10 = matriz_0_1[indice_fila][indice_columna]
    lista_pila.append((numero, indice_fila, indice_columna,color,codigo,valor10,p_row, p_column))
    return


    
'''
POP
Funcion para desapilar
Entradas: Numero
Salidas: lista con los valores apilados
'''
def desapila():
    global matriz_juego
    global lista_pila
    global matriz_0_1
    if lista_pila == []:
        showMensaje("No hay mas jugadas para borrar")
        return

    #elemento2=lista_pila[-1]
    elemento2= lista_pila.pop()
    if elemento2[0] == 0:
        boton= tk.Button(ventana_a_jugar, text= "  ", width= 5, \
                     height= 1, bg=elemento2[3],command=lambda:asigna_casilla(elemento2[4]))
    else:
        boton= tk.Button(ventana_a_jugar, text= elemento2[0], width= 5, \
                         height= 1, bg=elemento2[3],command=lambda:asigna_casilla(elemento2[4]))
    boton.grid(row=elemento2[6], column=elemento2[7])
    try:
        matriz_juego[elemento2[1]][elemento2[2]]=int(elemento2[0])
        matriz_0_1[elemento2[1]][elemento2[2]]=int(elemento2[elemento2[5]])
    except:
        matriz_juego[elemento2[1]][elemento2[2]]=int(0)
        
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
    ventana.destroy()

#Funcion que crea la matriz con listas en 0
def crea_matriz():
    global matriz_juego
    global matriz_0_1
    matriz_juego=[]
    matriz_0_1=[]
    cont_l=0
    #cont0=0
    while cont_l < 5:
        matriz_juego.append([0,0,0,0,0])
        matriz_0_1.append([0,0,0,0,0])
        cont_l+=1
    #print(juego_lista)
    

#-----------------------------Programa-Principal----------------------

#Golabls
global nivel_dificultad
global numero
global lado_num
global matriz_juego
global arc_jugadas
global reloj_o_time

global min_timer
global hora_timer
global seg_timer

global flag_cargar_juego
global ind_escoge_par

global lista_pila
min_timer=0
hora_timer=0
seg_timer=10
flag_cargar_juego=False
lista_pila=[]
ind_escoge_par=1


matriz_juego=[]
lado_num= 1
nivel_dificultad= 1
numero=0
crea_matriz()
reloj_o_time=1



#print(arc_jugadas)
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
