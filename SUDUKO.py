import tkinter as tk

class SudokuGUI:
    def __init__(self, root, matrix):
        self.root = root
        self.matrix = matrix
        self.entries = {}

        self.create_widgets()

    def create_widgets(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                entry = tk.Entry(self.root, width=5, justify='center')
                entry.grid(row=i, column=j)
                if self.matrix[i][j] != 0:  # If the cell is not empty, insert the value
                    entry.insert(0, str(self.matrix[i][j]))
                self.entries[(i, j)] = entry

        # Add a button to save the matrix
        save_button = tk.Button(self.root, text="Save", command=self.save_matrix)
        save_button.grid(row=len(self.matrix), column=0, columnspan=len(self.matrix)//2, pady=10)

        # Add a button to reset the matrix
        reset_button = tk.Button(self.root, text="Reset", command=self.reset_matrix)
        reset_button.grid(row=len(self.matrix), column=len(self.matrix)//2, columnspan=len(self.matrix)//2, pady=10)

    def get_matrix(self):
        new_matrix = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[i])):
                value = self.entries[(i, j)].get()
                if value.isdigit():
                    row.append(int(value))
                else:
                    row.append(0)  # Default value if not an integer
            new_matrix.append(row)
        return new_matrix

    def save_matrix(self):
        # Get the updated matrix from the GUI
        self.matrix = self.get_matrix()
        print("Matrix saved:")
        for row in self.matrix:
            print(row)

    def reset_matrix(self):
        # Reset the entries to the original matrix values
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.entries[(i, j)].delete(0, tk.END)
                if self.matrix[i][j] != 0:
                    self.entries[(i, j)].insert(0, str(self.matrix[i][j]))

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sudoku GUI")

    # Initialize the sduko matrix with your existing data
    sduko = [[0 for j in range(9)] for k in range(9)]

    sduko[0][1] = 7
    sduko[0][4] = 2
    sduko[0][7] = 4
    sduko[0][8] = 6

    sduko[1][1] = 6
    sduko[1][6] = 8
    sduko[1][7] = 9

    sduko[2][0] = 2
    sduko[2][3] = 8
    sduko[2][6] = 7
    sduko[2][7] = 1
    sduko[2][8] = 9

    sduko[3][1] = 8
    sduko[3][2] = 4
    sduko[3][4] = 9
    sduko[3][5] = 7

    sduko[4][0] = 7
    sduko[4][1] = 1
    sduko[4][7] = 5
    sduko[4][8] = 9

    sduko[5][3] = 1
    sduko[5][4] = 3
    sduko[5][6] = 4
    sduko[5][7] = 8

    sduko[6][0] = 6
    sduko[6][1] = 9
    sduko[6][2] = 7
    sduko[6][5] = 2
    sduko[6][8] = 8

    sduko[7][1] = 5
    sduko[7][2] = 8
    sduko[7][7] = 6

    sduko[8][0] = 4
    sduko[8][1] = 3
    sduko[8][4] = 8
    sduko[8][7] = 7

    # Create the GUI application
    app = SudokuGUI(root, sduko)
    root.mainloop()


























