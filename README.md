
# Drawing App (Mini Paint)

A simple **Drawing App** built using **Python** and **Tkinter**. This app allows users to draw on a canvas, choose brush colors, change brush sizes, use an eraser, and save their drawings as PNG files.

## Features

- **Draw on Canvas**: Users can draw freely on the canvas with their mouse.
- **Brush Color Selection**: Users can choose a custom color for drawing using a color picker.
- **Brush Size**: Adjustable brush sizes (2px, 5px, 10px, 15px).
- **Eraser**: Users can switch to an eraser tool to erase parts of their drawing.
- **Clear Canvas**: Option to clear the canvas and start a new drawing.
- **Save Drawing**: Save the current drawing as a PNG file.
  
## Requirements

- Python 3.x
- `Pillow` library (for handling image saving)
  
  Install `Pillow` with:

  ```bash
  pip install pillow
  ```

## Files

- `drawing_app.py`: The main Python file containing the drawing logic and UI elements.
- `image.py`: The image processing file where the drawing is created and stored.

## How to Run

1. Clone the repository:

    ```bash
    git clone https://github.com/GevorgGevorgyan1/drawing-app.git
    ```

2. Navigate to the project directory:

    ```bash
    cd drawing-app
    ```

3. Install the required libraries:

    ```bash
    pip install pillow
    ```

4. Run the Python script:

    ```bash
    python drawing_app.py
    ```

5. The drawing app window will appear, and you can start drawing on the canvas.

## How to Use

- **Pick Brush Color**: Click the "Pick Color 🎨" button to open the color picker and choose your brush color.
- **Draw**: Use your mouse to draw on the canvas. You can adjust the brush size using the available size buttons (2, 5, 10, 15).
- **Eraser**: Click the "Eraser 🧽" button to switch to the eraser mode, where you can erase parts of your drawing.
- **Clear Canvas**: Click "Clear Canvas ❌" to clear the canvas and start over.
- **Save Drawing**: Click "Save Drawing 💾" to save your drawing as a PNG file.
