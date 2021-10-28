from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
from ttkthemes import themed_tk
from PIL import ImageTk,Image
import basegastos

class Presupuesto:
    
    def __init__(self):
        
        self.gasto1=basegastos.gastos()
        self.win = themed_tk.ThemedTk(theme="itft1")
        self.win.title("Control de Gastos")
        self.win.geometry("583x620")
        self.win.resizable(False,False)
        self.win.config(bg="blue2")
        self.cuaderno1 = ttk.Notebook(self.win)
        self.ingresoGasto()
        self.consultaDatos()
        self.modificaBorrado()
        self.sumaDatos()
        self.cuaderno1.grid(row=0,column=0,padx=20,pady=20)
        self.win.mainloop()
    
    def ingresoGasto(self):
        global imagen
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Ingreso Gasto")
        self.labelframe1 =LabelFrame(self.pagina1, text="Ingreso",bg="cyan2",font=("Arial"),bd=5)
        self.labelframe1.grid(row=0,column=0,padx=100,pady=30)
        self.labelnom1=Label(self.labelframe1, text="Nombre:")
        self.labelnom1.grid(row=0,column=0,padx=20,pady=5,sticky="e")
        self.labelnom1.config(bg="cyan2")
        self.nombregasto=StringVar()
        self.entrynom1=Entry(self.labelframe1, textvariable=self.nombregasto)
        self.entrynom1.focus()
        self.entrynom1.grid(row=0,column=1,padx=10,pady=5)
        self.labelfech1=Label(self.labelframe1, text="Fecha:")
        self.labelfech1.grid(row=1,column=0,padx=20,pady=5,sticky="e")
        self.labelfech1.config(bg="cyan2")
        self.fechagasto=StringVar()
        self.entryfech1=Entry(self.labelframe1, textvariable=self.fechagasto)
        self.entryfech1.grid(row=1,column=1,padx=10,pady=5)
        self.labelmon1=Label(self.labelframe1, text="Monto:")
        self.labelmon1.grid(row=2,column=0,padx=20,pady=5,sticky="e")
        self.labelmon1.config(bg="cyan2")
        self.montogasto=StringVar()
        self.entrymon1=Entry(self.labelframe1, textvariable=self.montogasto)
        self.entrymon1.grid(row=2,column=1,padx=10,pady=5)
        self.botoncarga=ttk.Button(self.labelframe1, text="Cargar",command=self.cargarGasto)
        self.botoncarga.grid(row=3,column=1,padx=5,pady=5)
        imagen=ImageTk.PhotoImage(Image.open("/home/jungar/Escritorio/Python/gastos/Proyectos/imagenes/gastos.png"))
        labelimg=Label(self.pagina1, image = imagen)
        labelimg.grid(row=2,column=0,columnspan=2,sticky="ew",padx=65,pady=30)
        
    def validacion(self):
        return len(self.nombregasto.get()) != 0 and len(self.fechagasto.get()) != 0 and len(self.montogasto.get()) != 0
        
    def cargarGasto(self):
        
        if self.validacion():
            datos = (self.nombregasto.get(),self.fechagasto.get(),self.montogasto.get())
            self.gasto1.alta(datos)
            mb.showinfo("Informacion","Los datos fueron cargados")
            self.nombregasto.set("")
            self.fechagasto.set("")
            self.montogasto.set("")
            self.entrynom1.focus()
        else:
            mb.showerror("Informacion","Es obligatorio rellenar todos los campos ")
                            
       
    
    def consultaDatos(self):
        
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta Gasto")
        self.labelframe2 = LabelFrame(self.pagina2, text="Consulta Por Fecha",bg="cyan2",font=("Arial"),bd=5)
        self.labelframe2.grid(row=0,column=0,padx=50,pady=10)
        self.labelfech2=Label(self.labelframe2,text="Fecha:",bg="cyan2")
        self.labelfech2.grid(row=0,column=0,padx=10,pady=10,sticky="e")
        self.fechacosul=StringVar()
        self.entryfech2=Entry(self.labelframe2,textvariable=self.fechacosul)
        self.entryfech2.grid(row=0,column=1,pady=10)
        """self.labelnom2=Label(self.labelframe2,text="Nombre")
        self.labelnom2.grid(row=1,column=0,padx=10,pady=10)
        self.nombrecosul=StringVar()
        self.entrynom2=Entry(self.labelframe2,textvariable=self.nombrecosul, state="readonly")
        self.entrynom2.grid(row=1,column=1,padx=10,pady=10)
        self.labelmon2=Label(self.labelframe2,text="Monto")
        self.labelmon2.grid(row=2,column=0,padx=10,pady=10)
        self.montocosul=StringVar()
        self.entrynom2=Entry(self.labelframe2,textvariable=self.montocosul, state="readonly")
        self.entrynom2.grid(row=2,column=1,padx=10,pady=10)"""
        self.scrolledtext2=st.ScrolledText(self.labelframe2, width=30, height=5,bg="black",fg="green2")
        self.scrolledtext2.grid(row=1,column=1, padx=10, pady=10)
        self.botonconsul=ttk.Button(self.labelframe2,text="Consultar",command=self.consultar)
        self.botonconsul.grid(row=2,column=1,padx=5,pady=10)
        
        self.labelframe3 = LabelFrame(self.pagina2, text="Consultar todo",bg="cyan2",font=("Arial"),bd=5)
        self.labelframe3.grid(row=1,column=0,padx=120,pady=10)
        self.botonconsutodo=ttk.Button(self.labelframe3, text="Listado completo",command=self.consultar_all)
        self.botonconsutodo.grid(row=0,column=0, padx=10, pady=10)
        self.scrolledtext1=st.ScrolledText(self.labelframe3, width=30, height=10,bg="black",fg="green2")
        self.scrolledtext1.grid(row=1,column=0, padx=10, pady=10)
        
    def consultar(self):
        
        datos=(self.fechacosul.get(), )
        respuesta = self.gasto1.consulta(datos)
        self.scrolledtext2.delete("1.0", END)
        
        for fila in respuesta:
            self.scrolledtext2.insert(END,"id:"+str(fila[0])+"\nNombre:"+fila[1]+"\nMonto:"+str(fila[2])+"\n\n")
            
        """if len(repuesta)>0:
            self.nombrecosul.set(repuesta[0][0])
            self.montocosul.set(repuesta[0][1])
            
        else:
            self.nombrecosul.set("")
            self.montocosul.set("")
            mb.showinfo("Informacion", "No existe un gasto con dicha fecha")"""
    
    def consultar_all(self):
        
        respuesta = self.gasto1.recuperar_todos()
        self.scrolledtext1.delete("1.0", END)
        
        for fila in respuesta:
            self.scrolledtext1.insert(END,"id:"+str(fila[0])+"\nFecha:"+str(fila[1])+"\nNombre:"+fila[2]+"\nMonto:"+str(fila[3])+"\n\n")  
        
    def modificaBorrado(self):
        self.pagina4 =ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4,text="Modificar o Borrar")
        self.labelframe4= LabelFrame(self.pagina4,text="Modificar",bg="cyan2",font=("Arial"),bd=5)
        self.labelframe4.grid(row=0,column=0,padx=120,pady=20)
        self.labelmod1=Label(self.labelframe4,text="Codigo:",bg="cyan2")
        self.labelmod1.grid(row=0,column=0,padx=20,pady=10,sticky="e")
        self.codigomod=StringVar()
        self.entrycodigomod=Entry(self.labelframe4,textvariable=self.codigomod)
        self.entrycodigomod.grid(row=0,column=1,padx=10,pady=10)
        self.labelmod2=Label(self.labelframe4,text="Nombre:",bg="cyan2")
        self.labelmod2.grid(row=1,column=0,padx=20,pady=10,sticky="e")
        self.nombremod=StringVar()
        self.entrynombremod=Entry(self.labelframe4,textvariable=self.nombremod)
        self.entrynombremod.grid(row=1,column=1,padx=10,pady=10)
        self.labelmod3=Label(self.labelframe4,text="Monto:",bg="cyan2")
        self.labelmod3.grid(row=2,column=0,padx=20,pady=10,sticky="e")
        self.montomod=StringVar()
        self.entrymontomod=Entry(self.labelframe4,textvariable=self.montomod)
        self.entrymontomod.grid(row=2,column=1,padx=10,pady=10)
        self.botonmod=ttk.Button(self.labelframe4,text="Modificar",command=self.modificar)
        self.botonmod.grid(row=3,column=1,padx=10,pady=10)
        
        self.labelframe5= LabelFrame(self.pagina4,text="Borrado",bg="cyan2",font=("Arial"),bd=5)
        self.labelframe5.grid(row=1,column=0,padx=120,pady=50)
        self.labelbora=Label(self.labelframe5,text="Codigo:",bg="cyan2")
        self.labelbora.grid(row=0,column=0,padx=20,pady=10,sticky="e")
        self.codigobor=StringVar()
        self.entrybor=Entry(self.labelframe5,textvariable=self.codigobor)
        self.entrybor.grid(row=0,column=1,padx=15,pady=30)
        self.botonbor=ttk.Button(self.labelframe5,text="Borrar",comman=self.borrar)
        self.botonbor.grid(row=1,column=1,padx=10,pady=10)
        
    
    def borrar(self):
        
        datos = (self.codigobor.get(), )
        cantidad = self.gasto1.baja(datos)
        if cantidad==1:
            mb.showinfo("Informacion","Se borro el gasto con dicho codigo")
        else:
            mb.showinfo("Informacion","No existe el gasto con dicho codigo")
            
    
            
    def modificar(self):
        
        datos = (self.nombremod.get(),self.montomod.get(),self.codigomod.get())
        cantidad = self.gasto1.modificacion(datos)
        if cantidad==1:
            mb.showinfo("informacion","se modifico el gasto")
        else:
            mb.showinfo("informacion","no existe el gasto con dicho codigo")
            
    
    def sumaDatos(self):
        global imagen1
        self.pagina6 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina6,text="Sumar Gastos")
        self.labelframe6= LabelFrame(self.pagina6,text="Sumar",bg="cyan2",font=("Arial"),bd=5)
        self.labelframe6.grid(row=0,column=0,padx=90,pady=30)
        self.labelmod1=Label(self.labelframe6,text="Fecha Inicio:",bg="cyan2")
        self.labelmod1.grid(row=0,column=0,padx=20,pady=10,sticky="e")
        self.fechaini=StringVar()
        self.entryfechaini=Entry(self.labelframe6,textvariable=self.fechaini)
        self.entryfechaini.grid(row=0,column=1,padx=10,pady=10)
        self.entryfechaini.focus()
        self.labelmod2=Label(self.labelframe6,text="Fecha Final:",bg="cyan2")
        self.labelmod2.grid(row=1,column=0,padx=20,pady=10,sticky="e")
        self.fechafin=StringVar()
        self.entryfechafin=Entry(self.labelframe6,textvariable=self.fechafin)
        self.entryfechafin.grid(row=1,column=1,padx=10,pady=10) 
        self.labelmod3=Label(self.labelframe6,text="Resultado Suma:",bg="cyan2")
        self.labelmod3.grid(row=2,column=0,padx=20,pady=10,sticky="e")
        self.suma=StringVar()
        self.entrysuma=Entry(self.labelframe6,textvariable=self.suma,bg="black",fg="green2")
        self.entrysuma.grid(row=2,column=1,padx=10,pady=10) 
        self.botonsuma=ttk.Button(self.labelframe6,text="sumar",command=self.sumar)
        self.botonsuma.grid(row=3,column=1,padx=10,pady=10) 
        imagen1=ImageTk.PhotoImage(Image.open("/home/jungar/Escritorio/Python/gastos/Proyectos/imagenes/img"))
        labelimg=Label(self.pagina6, image = imagen1)
        labelimg.grid(row=2,column=0,columnspan=2,sticky="ew",padx=200)  
    
    def sumar(self):
        
        datos=(self.fechaini.get(),self.fechafin.get())
        
        if len(self.fechaini.get()) !=0 and len(self.fechafin.get()) !=0:
        
            respuesta = self.gasto1.suma(datos)
        
            if len(respuesta)>0:
                self.suma.set(respuesta)
            
        else:
            self.suma.set("")
            mb.showinfo("Informacion", "No se puede consultar introdusca fechas")
            
      
if __name__ == '__main__':
    app=Presupuesto()