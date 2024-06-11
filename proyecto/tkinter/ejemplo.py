import tkinter as tk

def dibujar_tablero(canvas):
    tamaño_celda = 100
    for i in range(4):
        # Dibujar líneas horizontales
        canvas.create_line(0, i * tamaño_celda, 300, i * tamaño_celda)
        # Dibujar líneas verticales
        canvas.create_line(i * tamaño_celda, 0, i * tamaño_celda, 300)

def main():
    root = tk.Tk()
    root.title("Tablero 3x3")
    canvas = tk.Canvas(root, width=300, height=300)
    canvas.pack()
    dibujar_tablero(canvas)
    root.mainloop()

if __name__ == "__main__":
    main()
