#Calling function from PdfParserForGemma_MAHA.py
#from PdfParserForGemma_MAHA import pdfParser 
#pdfParser()
#Create a front end with a button to select PDF file and another button to execute pdfparser function and also redirect the console output to GUI
import tkinter as tk
from tkinter import filedialog, scrolledtext
from PdfParserForGemma_MAHA import pdfParser
import sys
import threading
class RedirectText(object):
    def __init__(self, text_area):
        self.text_area = text_area

    def write(self, string):
        self.text_area.insert(tk.END, string)
        self.text_area.see(tk.END)

    def flush(self):
        pass
def run_pdf_parser(pdf_path):
    pdfParser(pdf_path)
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        threading.Thread(target=run_pdf_parser, args=(file_path,)).start()
app = tk.Tk()
app.title("PDF Parser for Gemma MAHA")
app.geometry("800x600")
select_button = tk.Button(app, text="Select PDF File", command=select_file)
select_button.pack(pady=10)
output_text = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=100, height=30)
output_text.pack(pady=10)
sys.stdout = RedirectText(output_text)
sys.stderr = RedirectText(output_text)
app.mainloop()  
