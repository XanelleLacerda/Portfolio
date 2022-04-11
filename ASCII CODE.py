from tkinter import *

root = Tk()
root.title("ASCII CODE")
root.geometry("400x400")
root.configure(background="blue")

word = Entry(root)
word.place(relx=0.5, rely=0.4, anchor = CENTER)
label = Label(root, text="Name In ASCII code: ", bg="yellow", fg="black")

def Asciiconverter():
    input_word = word.get()
    
    for letter in input_word:
        label["text"] +=str(ord(letter)) + " "
     
button = Button(root, text="show name in ASCII code", command=Asciiconverter)
button.place(relx=0.5, rely=0.5, anchor = CENTER)
label.place(relx=0.5, rely=0.6, anchor = CENTER)        
        


root.mainloop()