from tkinter import *

window = Tk()
window.title("My application")

window.geometry("500x500")

head = Label(text="Welcome to Application").pack()

def calculation():
    age=txt_age.get()
    age=int(age)
    disease=txt_disease.get()
    disease=int(disease)
    if disease==1:
        disease=True
    else:
        disease=False
    print(age)
    print(disease)
    

txt_age=StringVar()
label1 = Label(text="อายุเท่าไหร่").pack()
entry1 = Entry(window,textvariable=txt_age).pack()

txt_disease=StringVar()
label2 = Label(text="มีโรคประจำตัวไหม").pack()
label3 = Label(text="ถ้ามีใส่ 1 ถ้าไม่มี่ใส่ 2").pack()
entry2 = Entry(window,textvariable=txt_disease).pack()

btn1 = Button(window,text="calculate",command=calculation).pack()




window.mainloop()