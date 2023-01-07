from tkinter import *

def clear_all() :
    "Function for clearing the contents of all entry boxes"
    p_field.delete(0, END) 
    r_field.delete(0, END)
    t_field.delete(0, END)
    compound_field.delete(0, END)
    
    # set focus on the principle_field entry box 
    p_field.focus_set()
     
def calculate_ci():
    "Function to find compound interest"
    # get a content from entry box
    p = int(p_field.get())
    r = float(r_field.get())
    t = int(t_field.get())
    
    # Calculates compound interest 
    CI = p * (pow((1 + r / 100), t))-p
    
    # insert method inserting the 
    # value in the text entry box.
    compound_field.insert(0,CI)

# Driver code
if __name__ == "__main__" :

    # Create a GUI window
    root = Tk()

    # Set the background colour of GUI window
    root.configure(background = 'light blue')

    # Set the configuration of GUI window
    root.geometry("400x250")
    root.title("Compound Interest Calculator") 

    # Create a Principle Amount : label
    label1 = Label(root, text = "Principle Amount(Rs) : ",fg = 'black', bg = 'Yellow')

    # Create a Rate : label
    label2 = Label(root, text = "Rate(%) : ",fg = 'black', bg = 'Yellow')

    # Create a Time : label
    label3 = Label(root, text = "Time(years) : ",fg = 'black', bg = 'Yellow')

    # Create a Compound Interest : label
    label4 = Label(root, text = "Compound Interest : ",fg = 'black', bg = 'Yellow')

    # grid method is used for placing the widgets at respective positions 
    label1.grid(row = 1, column = 0, padx = 10, pady = 10) 
    label2.grid(row = 2, column = 0, padx = 10, pady = 10) 
    label3.grid(row = 3, column = 0, padx = 10, pady = 10)
    label4.grid(row = 5, column = 0, padx = 10, pady = 10)

    # Create a entry box for filling or typing the information.
    p_field = Entry(root)   
    r_field = Entry(root) 
    t_field = Entry(root)
    compound_field = Entry(root)

    p_field.grid(row = 1, column = 1, padx = 10, pady = 10) 
    r_field.grid(row = 2, column = 1, padx = 10, pady = 10) 
    t_field.grid(row = 3, column = 1, padx = 10, pady = 10)
    compound_field.grid(row = 5, column = 1, padx = 10, pady = 10)

    button1 = Button(root, text = "Submit", bg = "red", fg = "black", command = calculate_ci)
    button2 = Button(root, text = "Clear", bg = "red", fg = "black", command = clear_all)
    button1.grid(row = 4, column = 1, pady = 10)
    button2.grid(row = 6, column = 1, pady = 10)

    # Start the GUI 
    root.mainloop()