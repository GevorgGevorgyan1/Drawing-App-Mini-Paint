import tkinter as tk
from tkinter import colorchooser, filedialog
from PIL import Image, ImageDraw

window = tk.Tk()
window.title("Drawing App-Mini Paint")
window.geometry("700x500")
window.config(bg='white')

current_color = 'black' # stores the current brush color
brush_size=5 # stores the brush_size
last_x, last_y = None, None # stores the last drawing position

canvas_width, canvas_height = 550, 400
image = Image.new("RGB", (canvas_width, canvas_height), 'white')
draw = ImageDraw.Draw(image)

def start_draw(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

def draw_line(event):
    global last_x, last_y
    if last_x and last_y:
        canvas.create_line((last_x, last_y, event.x, event.y), width=brush_size, fill=current_color, capstyle=tk.ROUND, smooth=True)
        draw.line((last_x, last_y, event.x, event.y), fill=current_color, width=brush_size)
    last_x, last_y = event.x, event.y

def choose_color():
    global current_color
    color = colorchooser.askcolor(title="Choose Brush Color")[1]
    if color:
        current_color = color

def change_brush_size_2():
    global brush_size
    brush_size = 2

def change_brush_size_5():
    global brush_size
    brush_size = 5

def change_brush_size_10():
    global brush_size
    brush_size = 10

def change_brush_size_15():
    global brush_size
    brush_size = 15

def clear_canvas():
    canvas.delete("all")
    global image, draw
    image = Image.new("RGB", (canvas_width, canvas_height), "white")
    draw = ImageDraw.Draw(image)

def save_drawing():
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png")])
    if file_path:
        image.save(file_path)
        tk.messagebox.showinfo("Saved", "Your drawing has been saved successfully!")

def use_eraser():
    global current_color
    current_color = "white"  # Set brush color to white (eraser effect)

canvas = tk.Canvas(window, bg="white", width=canvas_width, height=canvas_height)
canvas.pack(pady=10)

canvas.bind("<Button-1>", start_draw) # Detects when the left mouse button is pressed.
canvas.bind("<B1-Motion>", draw_line) # Detects when the mouse is dragged.

buttons_frame = tk.Frame(window, bg="#f0f0f0")
buttons_frame.pack()

color_button = tk.Button(buttons_frame, text="Pick Color 🎨", command=choose_color, font=("Arial", 10, "bold"),
                         bg="#ffcc00", fg="black")
color_button.grid(row=0, column=0, padx=5, pady=5)

clear_button = tk.Button(buttons_frame, text="Clear Canvas ❌", command=clear_canvas, font=("Arial", 10, "bold"),
                         bg="red", fg="white")
clear_button.grid(row=0, column=1, padx=5, pady=5)

save_button = tk.Button(buttons_frame, text="Save Drawing 💾", command=save_drawing, font=("Arial", 10, "bold"),
                        bg="#4CAF50", fg="white", relief="raised")
save_button.grid(row=0, column=2, padx=5, pady=5)

tk.Label(buttons_frame, text="Brush Size:", font=("Arial", 10, "bold"), bg="#f0f0f0").grid(row=0, column=3, padx=5)
tk.Button(buttons_frame, text="2", command=change_brush_size_2, bg="#ddd", width=3).grid(row=0, column=4, padx=2)
tk.Button(buttons_frame, text="5", command=change_brush_size_5, bg="#ddd", width=3).grid(row=0, column=5, padx=2)
tk.Button(buttons_frame, text="10", command=change_brush_size_10, bg="#ddd", width=3).grid(row=0, column=6, padx=2)
tk.Button(buttons_frame, text="15", command=change_brush_size_15, bg="#ddd", width=3).grid(row=0, column=7, padx=2)

eraser_button = tk.Button(buttons_frame, text="Eraser 🧽", command=use_eraser,
                          font=("Arial", 10, "bold"), bg="gray", fg="white", relief="raised")
eraser_button.grid(row=0, column=8, padx=5)
window.mainloop()