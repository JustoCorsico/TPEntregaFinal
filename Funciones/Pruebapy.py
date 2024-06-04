from Funciones import cargar_wav
from Funciones import plot_wav
print(cargar_wav())   
"""
from ipywidgets import Button
from tkinter import Tk, filedialog
from IPython.display import clear_output, display
files = []
def select_files():
    clear_output()
    root = Tk()
    root.withdraw() # Hide the main window.
    root.call('wm', 'attributes', '.', '-topmost', True) # Raise the root to the top of all windows.
    files.append(filedialog.askopenfilename()) # List of selected files will be set button's file attribute.
    print(files) # Print the list of files selected.

    fileselect = Button(description="Seleccione el archivo")
    fileselect.on_click(select_files)

    display(fileselect)
    files
select_files()
"""