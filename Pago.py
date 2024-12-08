from tkinter import *
ventana=Tk()
ventana.geometry("3000x3000")
ventana.configure(bg="#3f88c5")


"""

def pago():
    try:
        total_pago = float(cuadroNombre.get())


        if total_pago > 0:
           ventana_pago= Toplevel(ventana)
           ventana_pago.title("Pago realizado")
           ventana_pago.geometry("300x150")
           ventana_pago.configure(bg="#a1d6e3")


           mensaje= f"El pago de {total_pago:.2f} se ha realizado con exito"
           mensaje_label=Label(ventana_pago,text=mensaje,font=("arial",14),bg="#a1d6e3",fg="green")
           mensaje_label.place(y=30)

           boton_cerrar= Button(ventana_pago, text="Cerrar",font=("arial",12),command=ventana_pago.destroy)
           boton_cerrar.place()

        else:
            mensaje_label.config(text="Ingrese un monto valido", fg="red")

    except ValueError:
        mensaje_label.config(text="Ingrese un numero valido", fg="red")
"""


nombreLabel=Label(ventana,text="Total a pagar:", font=( 22))
nombreLabel.configure(bg="#3f88c5",fg="White")
nombreLabel.place(x=590,y=160)

cuadroNombre=Entry(ventana,width=10, font=("arial, 20"), justify="center")
cuadroNombre.place(x=500, y=195, width=300,height=50)


boton1 =Button(ventana, text="Confirmar pago",font=("Arial", 12), width=20, height=2)  #Es una boton, se debe agregar command
boton1.place(x=550,y=300,width=200, height=50) 


mensaje_label=Label(ventana,text="",font=("arial",14), bg="#3f88c5", fg="black")
mensaje_label.place(x=550,y=380,width=200, height=50)


ventana.mainloop()