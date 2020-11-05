import random 
import tkinter
import string

def generate_password():
	password=[]
	for i in range(5):
		alpha=random.choice(string.ascii_letters)
		symbol=random.choice(string.punctuation)
		number=random.choice(string.digits)
		password.append(alpha)
		password.append(symbol)
		password.append(number)

	y="".join(str(x)for x in password)
	lbl.config(text=y)

root=tkinter.Tk()
root.geometry("500x400")
btn=tkinter.Button(root,text="Generate Password",command=generate_password)
btn.grid(row=5,column=10)
lbl=tkinter.Label(root,font=("times",20,"bold"))
lbl.grid(row=7,column=10)
root.mainloop()