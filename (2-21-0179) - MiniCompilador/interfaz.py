import tkinter as tk
from tkinter import ttk
import subprocess
import os

# ================= FUNCION PRINCIPAL =================
def compilar():
    codigo = entrada.get("1.0", tk.END)

    with open("entrada.txt", "w") as f:
        f.write(codigo)

    try:
        resultado = subprocess.run(
            ["./compilador"],
            capture_output=True,
            text=True,
            shell=True
        )

        salida = resultado.stdout

    except:
        salida = ""

    # ===== LIMPIAR =====
    lexico.delete("1.0", tk.END)
    sintactico.delete("1.0", tk.END)
    semantico.delete("1.0", tk.END)
    codigo_c.delete("1.0", tk.END)
    tabla.delete(*tabla.get_children())

    # ================= LEXICO (MANUAL SEGURO) =================
    palabras = codigo.replace("\n", " ").split()

    for palabra in palabras:
        if palabra.upper() in ["INICIO", "FIN", "ENTERO", "ESCRIBIR", "LEER"]:
            lexico.insert(tk.END, f"KEYWORD: {palabra}\n")
        elif palabra.isdigit():
            lexico.insert(tk.END, f"NUMBER: {palabra}\n")
        elif palabra in ["=", "+", "-", "*", "/"]:
            lexico.insert(tk.END, f"OPERATOR: {palabra}\n")
        else:
            lexico.insert(tk.END, f"IDENTIFIER: {palabra}\n")

    # ================= SINTACTICO Y SEMANTICO =================
    if salida.strip() == "":
        sintactico.insert(tk.END, "Correcto\n")
        semantico.insert(tk.END, "OK\n")
    else:
        for linea in salida.split("\n"):
            if "[SINTACTICO]" in linea:
                sintactico.insert(tk.END, linea + "\n")
            elif "[SEMANTICO]" in linea:
                semantico.insert(tk.END, linea + "\n")

    # ================= TABLA DE SIMBOLOS =================
    variables = set()

    for linea in codigo.split("\n"):
        if linea.strip().startswith("ENTERO"):
            partes = linea.split()
            if len(partes) >= 2:
                variables.add(partes[1])

    for var in variables:
        tabla.insert("", "end", values=(var,))

    # ================= CODIGO C =================
    if os.path.exists("salida.c"):
        with open("salida.c", "r") as f:
            codigo_c.insert(tk.END, f.read())


# ================= VENTANA =================
root = tk.Tk()
root.title("Mini Compilador")
root.geometry("1200x750")
root.configure(bg="#0f172a")

# ================= TITULO =================
tk.Label(
    root,
    text="MINI COMPILADOR",
    font=("Segoe UI", 20, "bold"),
    fg="white",
    bg="#0f172a"
).pack(pady=10)

# ================= ENTRADA =================
entrada = tk.Text(
    root,
    height=7,
    bg="#020617",
    fg="white",
    insertbackground="white",
    font=("Consolas", 11),
    relief="flat"
)
entrada.pack(fill="x", padx=10)

# ================= BOTON =================
tk.Button(
    root,
    text="COMPILAR",
    command=compilar,
    bg="#22c55e",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    padx=20,
    pady=6
).pack(pady=10)

# ================= CONTENEDOR =================
frame = tk.Frame(root, bg="#0f172a")
frame.pack(fill="both", expand=True)

def crear_panel(titulo):
    panel = tk.Frame(frame, bg="#020617")

    tk.Label(
        panel,
        text=titulo,
        fg="#38bdf8",
        bg="#020617",
        font=("Segoe UI", 11, "bold")
    ).pack(anchor="w", padx=5)

    text = tk.Text(
        panel,
        bg="#020617",
        fg="white",
        insertbackground="white",
        font=("Consolas", 10),
        relief="flat"
    )
    text.pack(fill="both", expand=True, padx=5, pady=5)

    return panel, text

# ================= PANELES =================
p1, lexico = crear_panel("LEXICO")
p2, sintactico = crear_panel("SINTACTICO")
p3, semantico = crear_panel("SEMANTICO")
p5, codigo_c = crear_panel("CODIGO C")

# ================= TABLA OSCURA =================
tabla_frame = tk.Frame(frame, bg="#020617")

tk.Label(
    tabla_frame,
    text="TABLA DE SIMBOLOS",
    fg="#38bdf8",
    bg="#020617",
    font=("Segoe UI", 11, "bold")
).pack(anchor="w", padx=5)

style = ttk.Style()
style.theme_use("default")

style.configure("Treeview",
    background="#020617",
    foreground="white",
    rowheight=25,
    fieldbackground="#020617"
)

style.map('Treeview', background=[('selected', '#2563eb')])

tabla = ttk.Treeview(tabla_frame, columns=("Nombre",), show="headings")
tabla.heading("Nombre", text="VARIABLE")
tabla.pack(fill="both", expand=True, padx=5, pady=5)

# ================= GRID =================
p1.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
p2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
p3.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
tabla_frame.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
p5.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.rowconfigure(2, weight=1)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

root.mainloop()
