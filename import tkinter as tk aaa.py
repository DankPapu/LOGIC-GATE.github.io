import tkinter as tk
from tkinter import messagebox

class LogicGateDrawer:
    def __init__(self, root):
        self.root = root
        self.root.title("Logic Gate Drawer")

        self.canvas = tk.Canvas(root, width=400, height=300)
        self.canvas.pack()

        self.instructions_label = tk.Label(root, text="Ingresa la expresión lógica (por ejemplo, A'BCD):")
        self.instructions_label.pack()

        self.expression_entry = tk.Entry(root)
        self.expression_entry.pack()

        self.draw_button = tk.Button(root, text="Dibujar Puerta Lógica", command=self.draw_gate)
        self.draw_button.pack()

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_canvas)
        self.reset_button.pack()

    def draw_gate(self):
        expression = self.expression_entry.get().upper()

        # Limpiar el lienzo (canvas)
        self.canvas.delete("all")

        # Dibujar la puerta lógica correspondiente
        self.draw_logic_expression(expression)

    def reset_canvas(self):
        # Limpiar el lienzo (canvas)
        self.canvas.delete("all")

        # Limpiar la entrada de expresión
        self.expression_entry.delete(0, 'end')

        messagebox.showinfo("Reset", "Lienzo reiniciado")

    def draw_logic_expression(self, expression):
        variables = set()
        negated_variables = set()

        # Analizar la expresión lógica
        for char in expression:
            if char.isalpha():
                if "'" in expression:
                    negated_variables.add(char)
                else:
                    variables.add(char)

        # Dibujar la puerta lógica correspondiente
        if not all(v.isupper() for v in variables.union(negated_variables)):
            messagebox.showinfo("Error", "Ingresa solo letras mayúsculas para las variables.")
            return

        num_variables = len(variables) + len(negated_variables)

        if 1 <= num_variables <= 4:
            if num_variables == 1:
                self.draw_not_gate(variables, negated_variables)
            elif num_variables == 2:
                self.draw_xor_gate(variables, negated_variables)
            elif num_variables == 3:
                self.draw_or_gate(variables, negated_variables)
            elif num_variables == 4:
                self.draw_and_gate(variables, negated_variables)
        else:
            messagebox.showinfo("Error", "Número de variables no admitido.")

    def draw_and_gate(self, variables, negated_variables):
        self.canvas.create_text(200, 50, text="AND", font=("Helvetica", 12, "bold"))
        for i, var in enumerate(["A", "B", "C", "D"]):
            # Dibujar variable negada
            if var in negated_variables:
                self.canvas.create_text(30, 100 + i * 50, text=var + "'", font=("Helvetica", 10, "bold"))
            else:
                self.canvas.create_text(30, 100 + i * 50, text=var, font=("Helvetica", 10, "bold"))

            self.canvas.create_line(50, 100 + i * 50, 150, 100 + i * 50, width=2)  # Entrada
        self.canvas.create_line(250, 150, 300, 150, width=2)  # Salida

    def draw_or_gate(self, variables, negated_variables):
        self.canvas.create_text(200, 50, text="OR", font=("Helvetica", 12, "bold"))
        for i, var in enumerate(["A", "B", "C", "D"]):
            # Dibujar variable negada
            if var in negated_variables:
                self.canvas.create_text(30, 100 + i * 50, text=var + "'", font=("Helvetica", 10, "bold"))
            else:
                self.canvas.create_text(30, 100 + i * 50, text=var, font=("Helvetica", 10, "bold"))

            self.canvas.create_line(50, 100 + i * 50, 150, 100 + i * 50, width=2)  # Entrada
        self.canvas.create_oval(145, 50, 155, 200, fill="white")  # Círculo en el símbolo OR

    def draw_not_gate(self, variables, negated_variables):
        self.canvas.create_text(200, 50, text="NOT", font=("Helvetica", 12, "bold"))
        # Solo se acepta una variable para la compuerta NOT
        var = variables.pop() if variables else None

        if var:
            # Dibujar variable negada
            if var in negated_variables:
                self.canvas.create_text(30, 75, text=var + "'", font=("Helvetica", 10, "bold"))
            else:
                self.canvas.create_text(30, 75, text=var, font=("Helvetica", 10, "bold"))

            self.canvas.create_line(50, 75, 150, 75, width=2)  # Entrada
            self.canvas.create_line(250, 75, 300, 75, width=2)  # Salida
            self.canvas.create_line(150, 75, 150, 75, width=2, dash=(5, 2))  # Símbolo NOT
            self.canvas.create_oval(145, 70, 155, 80, fill="white")  # Círculo en el símbolo NOT

    def draw_xor_gate(self, variables, negated_variables):
        self.canvas.create_text(200, 50, text="XOR", font=("Helvetica", 12, "bold"))
        for i, var in enumerate(["A", "B", "C", "D"]):
            # Dibujar variable negada
            if var in negated_variables:
                self.canvas.create_text(30, 100 + i * 50, text=var + "'", font=("Helvetica", 10, "bold"))
            else:
                self.canvas.create_text(30, 100 + i * 50, text=var, font=("Helvetica", 10, "bold"))

            self.canvas.create_line(50, 100 + i * 50, 150, 100 + i * 50, width=2)  # Entrada
        self.canvas.create_line(250, 150, 300, 150, width=2)  # Salida
        self.canvas.create_line(150, 50, 150, 200, width=2, dash=(5, 2))  # Símbolo XOR
        self.canvas.create_line(145, 50, 155, 60, width=2)  # Línea diagonal en el símbolo XOR
        self.canvas.create_line(145, 60, 155, 50, width=2)  # Línea diagonal en el símbolo XOR

def main():
    root = tk.Tk()
    app = LogicGateDrawer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
