import os
import tkinter as tk
from tkinter import messagebox


def btn_guardar_click():
  nombre = txtb_nom.get()
  apellido = txtb_ape.get()
  telefono = txtb_tel.get()
  edad = txtb_edad.get()
  estatura = txtb_est.get()
  genero = genero_var.get()

  mensaje = (
      f" Nombres:{nombre}\n"
      f" Apellido:{apellido}\n"
      f" Genero:{genero}\n"
      f" Edad:{edad}\n"
      f" Telefono:{telefono}\n"
      f" Estatura:{estatura}\n"
  )

  rutaFile = "C:\\Users\\haloz\\Documents\\Actividad04py_Vr_0001.txt"
  archivoExiste = os.path.exists(rutaFile) and os.path.getsize(rutaFile) > 0

  try:
    os.makedirs(os.path.dirname(rutaFile), exist_ok=True)
    with open(rutaFile, "a", encoding="utf-8") as escritor:
      if archivoExiste:
        escritor.write("\n")
      escritor.write("Datos\n" + mensaje)
  except Exception as e:
    print(f"Error: {e}")

  messagebox.showinfo(
      "Registros de Usuario",
      mensaje,
      icon=messagebox.INFO,
  )


def limpiar():
  txtb_nom.delete(0, tk.END)
  txtb_ape.delete(0, tk.END)
  txtb_tel.delete(0, tk.END)
  txtb_edad.delete(0, tk.END)
  txtb_est.delete(0, tk.END)
  genero_var.set("")


root = tk.Tk()
root.title("Actividad04_FormulariodeRegistro_Vr0001")
root.geometry("450x420")
root.resizable(False, False)

tk.Label(root, text="Nombre:").place(x=50, y=30)
txtb_nom = tk.Entry(root)
txtb_nom.place(x=130, y=30, width=180)

tk.Label(root, text="Apellido:").place(x=50, y=70)
txtb_ape = tk.Entry(root)
txtb_ape.place(x=130, y=70, width=180)

tk.Label(root, text="Telefono:").place(x=50, y=110)
txtb_tel = tk.Entry(root)
txtb_tel.place(x=130, y=110, width=180)

tk.Label(root, text="Edad:").place(x=50, y=150)
txtb_edad = tk.Entry(root)
txtb_edad.place(x=130, y=150, width=180)

tk.Label(root, text="Estatura:").place(x=50, y=190)
txtb_est = tk.Entry(root)
txtb_est.place(x=130, y=190, width=180)

genero_var = tk.StringVar(value="")

gb_genero = tk.LabelFrame(root, text="Genero")
gb_genero.place(x=50, y=230, width=320, height=70)

tk.Radiobutton(
    gb_genero, text="Masculino", variable=genero_var, value="Masculino"
).place(x=10, y=10)
tk.Radiobutton(
    gb_genero, text="Femenino", variable=genero_var, value="femenino"
).place(x=110, y=10)
tk.Radiobutton(gb_genero, text="Otro", variable=genero_var, value="Otro").place(
    x=210, y=10
)

btn_guardar = tk.Button(root, text="Guardar", command=btn_guardar_click)
btn_guardar.place(x=70, y=330, width=90, height=30)

btn_limpiar = tk.Button(root, text="Limpiar", command=limpiar)
btn_limpiar.place(x=190, y=330, width=90, height=30)

root.mainloop()