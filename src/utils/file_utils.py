import os
from tkinter import Tk, filedialog

def select_files(title, filetypes):
    if os.environ.get('CI'):
        # If running in a CI environment, use command-line arguments instead of file dialogs
        return os.environ.get(title).split(',')
    else:
        root = Tk()
        root.withdraw()  # Hide the root window
        initial_dir = os.path.dirname(os.path.abspath(__file__))  # Set default folder to script's location
        file_paths = filedialog.askopenfilenames(title=title, initialdir=initial_dir, filetypes=filetypes)
        return list(file_paths)

def create_output_folders():
    docx_output_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output", "docx")
    pdf_output_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output", "pdf")
    os.makedirs(docx_output_folder, exist_ok=True)
    os.makedirs(pdf_output_folder, exist_ok=True)
    return docx_output_folder, pdf_output_folder
