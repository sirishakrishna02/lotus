import tkinter
root=tkinter.Tk()
root.title("student regestration form")

name_label=tkinter.Label(root,text="Enter your name")
name_label.pack()
name_textbox=tkinter.Entry(root)
name_textbox.pack()

email_label=tkinter.Label(root,text="Enter your email ")
email_label.pack()
email_textbox=tkinter.Entry(root)
email_textbox.pack()

phone_label=tkinter.Label(root,text="Enter your Phone no")
phone_label.pack()
phone_textbox=tkinter.Entry(root)
phone_textbox.pack()

submit_button=tkinter.Button(root,text="submit")
submit_button.pack()
root.mainloop()
