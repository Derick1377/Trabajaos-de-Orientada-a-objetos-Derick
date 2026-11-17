import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title('Semana 7 - Registro de computadora')
ventana.geometry('520x490')
ventana.configure(bg='#f3f5f9')
ventana.resizable(False, False)

estilo = ttk.Style()
estilo.theme_use('clam')
estilo.configure('TEntry', padding=7)
estilo.configure('TButton', font=('Arial', 11, 'bold'), padding=10)

contenedor = tk.Frame(ventana, bg='#ffffff', padx=28, pady=24,
                      highlightbackground='#dfe3ea', highlightthickness=1)
contenedor.place(x=36, y=25, width=448, height=440)

tk.Label(contenedor, text='Registro de computadora', font=('Arial', 18, 'bold'),
         bg='white', fg='#1c2b47').pack(anchor='w', pady=(0, 16))

campos = {}
for texto in ('Nombre', 'RAM', 'Estado', 'Tipo de identificador', 'Valor del identificador'):
    fila = tk.Frame(contenedor, bg='white')
    fila.pack(fill='x', pady=5)
    tk.Label(fila, text=texto + ':', font=('Arial', 10), bg='white',
             fg='#28364b', width=20, anchor='w').pack(side='left')
    entrada = ttk.Entry(fila, width=23)
    entrada.pack(side='left', fill='x', expand=True)
    campos[texto] = entrada

resultado = tk.StringVar(value='Resultado:')

def registrar():
    nombre = campos['Nombre'].get().strip()
    ram = campos['RAM'].get().strip()
    estado = campos['Estado'].get().strip()
    tipo = campos['Tipo de identificador'].get().strip()
    valor = campos['Valor del identificador'].get().strip()
    if not all((nombre, ram, estado, tipo, valor)):
        resultado.set('Resultado: Falta completar un campo')
    else:
        resultado.set(f'Resultado: {nombre} registrado - {ram} GB')

ttk.Button(contenedor, text='Registrar', command=registrar).pack(fill='x', pady=(22, 16))
tk.Label(contenedor, textvariable=resultado, bg='#edf2fb', fg='#183e79',
         font=('Arial', 10), anchor='w', padx=12, pady=14,
         wraplength=360).pack(fill='x')

ventana.mainloop()
