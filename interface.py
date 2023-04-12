import tkinter as tk
import sympy as sp

class EquationInputUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Equation Input")
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # create label for instructions
        self.instructions_label = tk.Label(self, text="Enter the number of equations:")
        self.instructions_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # create input box for number of equations
        self.num_equations_input = tk.Entry(self)
        self.num_equations_input.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # create button to submit number of equations
        self.submit_num_equations_button = tk.Button(self, text="OK", command=self.create_equation_inputs)
        self.submit_num_equations_button.grid(row=0, column=2, padx=10, pady=10, sticky="w")

        # create exit button
        self.exit_button = tk.Button(self, text="Exit", command=self.master.quit)
        self.exit_button.grid(row=0, column=3, padx=10, pady=10, sticky="w")

        # create clear button
        self.clear_button = tk.Button(self, text="Clear", command=self.clear_inputs, state="disabled")
        self.clear_button.grid(row=0, column=5, padx=10, pady=10, sticky="w")

        # create button to show solutions
        self.show_solutions_button = tk.Button(self, text="Show \nSolutions", command=self.show_solutions, state="disabled")
        self.show_solutions_button.grid(row=1, column=2, padx=10,  pady=10, sticky="w")


    def create_equation_inputs(self):
        # get number of equations entered by user
        num_equations = int(self.num_equations_input.get())

        # create labels and input boxes for equations
        self.equation_labels = []
        self.equation_inputs = []
        for i in range(num_equations):
            # create label for equation number
            label = tk.Label(self, text=f"Equation {i+1}:")
            label.grid(row=i+1, column=0, padx=10, pady=10, sticky="w")
            self.equation_labels.append(label)

            # create input box for equation
            equation_input = tk.Entry(self)
            equation_input.grid(row=i+1, column=1, padx=10, pady=10, sticky="w")
            self.equation_inputs.append(equation_input)

        self.clear_button["state"] = "normal"
        self.show_solutions_button["state"] = "normal"

    def clear_inputs(self):
        # clear input boxes for equations
        for equation_input in self.equation_inputs:
            equation_input.delete(0, tk.END)

        # disable submit and clear buttons
        self.clear_button["state"] = "disabled"
        
    def show_solutions(self):
        # get equations entered by user
        equations = [equation_input.get() for equation_input in self.equation_inputs]

        # solve each equation and display solution
        self.solution_labels = []
        for i, equation in enumerate(equations):
            try:
                solution = sp.solve(equation)
                label_text = f"Solution to Equation {i+1}: {solution}"
            except:
                label_text = f"No solution found for Equation {i+1}"

            label = tk.Label(self, text=label_text)
            label.grid(row=i+2, column=2, padx=10, pady=10, sticky="w")
            self.solution_labels.append(label)

        # disable show solutions button
        self.show_solutions_button["state"] = "disabled"
            
if __name__ == "__main__":
    root = tk.Tk()
    app = EquationInputUI(master=root)
    app.mainloop()