import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd

# Define a function to process Excel files of Type 1
def process_excel_file_Type1():
    try:
        file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")]) #I work with excel files, but you can change it according to your needs
        if not file_path:
            return messagebox.showinfo('Information', 'File not selected')
# Read the Excel file into a DataFrame
        df = pd.read_excel(file_path, skiprows=5) #The initial 5 rows of the file are irrelevant, so I skipped them
# Filter the DataFrame based on specified criteria
        valid_companies = [''] #Enter valid companies according to your needs

        valid_employee_types = [''] #Enter valid employees according to your needs

        df = df[(df['Company'].isin(valid_companies)) &
        (df['Employee Type'].isin(valid_employee_types)) &
        (df['Worker Type'] == 'Employee')] #Define the worket type you want
 # Select specific columns to keep in the DataFrame
        columns = ['']
        df = df[columns]
# Informing the user if no matching records are found
        if df.empty:
            messagebox.showerror('Information', 'No matching records found.')
            return
# Prompt the user to save the processed DataFrame to a new Excel file        
        save_path = filedialog.asksaveasfilename(defaultextension=".xlsx")

        if save_path:
            df.to_excel(save_path, index=False)
            messagebox.showinfo('Success', 'File processed successfully')
# Handling exceptions that may occur during the process
    except Exception as e:
        error_message = f'An error occurred: {str(e)}'
        print(error_message)
        messagebox.showerror('Error', error_message)
# Define a function to process Excel files of Type 2 (similar to Type 1)
def process_excel_file_Type2():
    try:
        file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
        if not file_path:
            return messagebox.showinfo('Information', 'File not selected')

        df = pd.read_excel(file_path, skiprows=5)

        valid_companies = ['']

        valid_employee_types = ['']

        df = df[(df['Company'].isin(valid_companies)) &
        (df['Employee Type'].isin(valid_employee_types)) &
        (df['Worker Type'] == 'Employee')]

        columns = ['']
        df = df[columns]

        if df.empty:
            messagebox.showinfo('Information', 'No matching records found.')
            return
        
        save_path = filedialog.asksaveasfilename(defaultextension=".xlsx")

        if save_path:
            df.to_excel(save_path, index=False)
            messagebox.showinfo('Success', 'File processed successfully')

    except Exception as e:
        error_message = f'An error occurred: {str(e)}'
        print(error_message)
        messagebox.showerror('Error', error_message)
# Creating the Tkinter GUI window
root = tk.Tk()
root.title('BBDD')
# Creating buttons to trigger different file processing functions
process_button = tk.Button(root, text='Type1', command=process_excel_file_Type1)
process_button.pack(pady=30)

process_button = tk.Button(root, text='Type2', command=process_excel_file_Type2)
process_button.pack(pady=30)
# Running the Tkinter event loop
root.mainloop()