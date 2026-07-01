# Word Counter

A simple Python desktop application for counting words in a text.

This is a small practice project created to improve my Python skills and learn the basics of GUI development with Tkinter.


## Features

- Count words in any pasted text
- Supports English, German, and Russian text
- Simple desktop interface built with Tkinter
- Standalone executable created with PyInstaller

## Technologies

- Python 3
- Tkinter
- Regular Expressions (`re`)
- PyInstaller

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/Samaelison/word-counter.git
```

2. Navigate to the project directory:

```bash
cd word-counter
```

3. Run the application:

```bash
python gui.py
```

## Build Executable

To create a standalone executable:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed gui.py
```

The executable will be created inside the `dist` folder.
