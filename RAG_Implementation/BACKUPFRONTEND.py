#Calling function from PdfParserForGemma_MAHA.py
#from PdfParserForGemma_MAHA import pdfParser 
#pdfParser()
#Create a front end with a button to select PDF file and another button to execute pdfparser function and also show the console output in the front end
#modify below code to redirect console output to the front end

import tkinter as tk
from tkinter import filedialog, scrolledtext
from PdfParserForGemma_MAHA import pdfParser 
def select_pdf_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    pdf_path_var.set(file_path)
    console_output.insert(tk.END, f"Selected PDF file: {file_path}\n")
def run_pdf_parser():
    pdf_path = pdf_path_var.get()
    if pdf_path:
        console_output.insert(tk.END, "Running PDF parser...\n")
        pdfParser(pdf_path)
        console_output.insert(tk.END, "PDF parsing completed.\n")
    else:
        console_output.insert(tk.END, "Please select a PDF file first.\n")
# Create the main window
root = tk.Tk()
root.title("PDF Parser Front End")
# PDF file selection
pdf_path_var = tk.StringVar()
select_button = tk.Button(root, text="Select PDF File", command=select_pdf_file)
select_button.pack(pady=10)
# Run parser button
run_button = tk.Button(root, text="Run PDF Parser", command=run_pdf_parser)
run_button.pack(pady=10)
# Console output area
console_output = scrolledtext.ScrolledText(root, width=80, height=20)
console_output.pack(pady=10)
# Start the GUI event loop
root.mainloop() 
