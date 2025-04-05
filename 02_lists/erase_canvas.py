import tkinter as tk
import time

CANVAS_WIDTH: int = 400
CANVAS_HEIGHT: int = 400

CELL_SIZE: int = 40
ERASER_SIZE: int = 20

class EraserApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')
        self.canvas.pack()
        
        # Initialize the cells list
        self.cells = []
        
        # Create the grid of blue squares
        self.create_grid()
        
        # Variable to hold the eraser
        self.eraser = None
        
        # Bind left-click to create the eraser
        self.canvas.bind("<Button-1>", self.create_eraser)
        
        # Bind mouse motion to move the eraser
        self.canvas.bind("<Motion>", self.move_eraser)

    def create_grid(self):
        num_rows = CANVAS_HEIGHT // CELL_SIZE
        num_cols = CANVAS_WIDTH // CELL_SIZE
        
        for row in range(num_rows):
            for col in range(num_cols):
                left_x = col * CELL_SIZE
                top_y = row * CELL_SIZE
                right_x = left_x + CELL_SIZE
                bottom_y = top_y + CELL_SIZE
                
                # Create a blue rectangle and store its ID
                cell = self.canvas.create_rectangle(left_x, top_y, right_x, bottom_y, fill='blue')
                self.cells.append(cell)

    def create_eraser(self, event):
        if self.eraser is None:  # Only create eraser once
            x, y = event.x, event.y
            self.eraser = self.canvas.create_rectangle(
                x, y, x + ERASER_SIZE, y + ERASER_SIZE, fill='pink'
            )

    def move_eraser(self, event):
        if self.eraser is not None:
            # Move the eraser to the mouse position
            x, y = event.x, event.y
            self.canvas.coords(self.eraser, x, y, x + ERASER_SIZE, y + ERASER_SIZE)
            
            # Check for overlapping cells and erase them
            self.erase_objects(x, y)

    def erase_objects(self, eraser_x, eraser_y):
        # Define the eraser's bounding box
        left_x = eraser_x
        top_y = eraser_y
        right_x = left_x + ERASER_SIZE
        bottom_y = top_y + ERASER_SIZE
        
        # Find overlapping objects
        overlapping = self.canvas.find_overlapping(left_x, top_y, right_x, bottom_y)
        
        # Change color of overlapping cells to white (except the eraser)
        for obj in overlapping:
            if obj != self.eraser and obj in self.cells:
                self.canvas.itemconfig(obj, fill='white')

def main():
    root = tk.Tk()
    root.title("Eraser App")
    app = EraserApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()