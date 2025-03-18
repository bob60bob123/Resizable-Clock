# Resizable-Clock
Resizable Clock
# Resizable Clock

A customizable digital and analog clock application built with Python and Tkinter.

## Features

- Digital time display in HH:MM:SS format
- Analog clock with hour, minute, and second hands
- Resizable interface that adapts to window dimensions
- Interactive size adjustment buttons
- Minimalist black and white design with red second hand

## Requirements

- Python 3.x
- Tkinter (included in standard Python installation)

## Installation

1. Ensure you have Python installed on your system
2. No additional packages are required as Tkinter comes with Python

## Usage

1. Save the code to a file named `resizable_clock.py`
2. Run the program using:

```bash
python resizable_clock.py
```

3. The clock application will open in a new window

## Controls

- **Resize the window**: The clock and digital display automatically adapt to the new dimensions
- **Smaller button**: Decreases the analog clock size
- **Larger button**: Increases the analog clock size
- **Close button (X)**: Exits the application

## How It Works

The application combines both digital and analog clock displays:

- The digital clock updates every second to show the current time
- The analog clock features:
  - A circular clock face with hour markers
  - Hour hand (shortest)
  - Minute hand (medium length)
  - Second hand (longest, colored red)
  
The size of the clock elements adjusts dynamically when:
1. The window is resized
2. The "Smaller" or "Larger" buttons are clicked

## Customization

You can modify the following aspects of the clock:

- Colors (background, hands, text)
- Font styles and sizes
- Clock face design
- Size adjustment range
- Window dimensions

## Code Structure

- `ResizableClock` class extends `tk.Tk` to create the main application window
- `update_clock()` refreshes both digital and analog displays every second
- `draw_analog_clock()` handles the rendering of the analog clock face and hands
- Size adjustment methods modify the `size_factor` variable
- Window resize event is handled by the `on_resize()` method

## License

This code is available for personal and educational use.
