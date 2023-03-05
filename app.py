from tkinter import *
from tkinter import ttk

win = Tk()
win.title("Ascent Academy")
win.config(bg="blue")
win.geometry("500x570")

name_label = Label(win,text="Asc Weather App",font=("Times New Roman",30,"bold"))
name_label.place(x=25,y=50,height=50,width=450)
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win,text="Asc Weather App",values=list_name,font=("Times New Roman",20,"bold"))
com.place(x=25,y=120,height=50,width=450)
done_button = Button(win,text="Done",font=("Times New Roman",20,"bold"))
done_button.place(y=190,height=50,width=100,x=200)
w_label = Label(win,text="Weather Climate",font=("Times New Roman",30,"bold"))
w_label.place(x=25,y=50,height=50,width=450)
w_label1 = Label(win,text="",font=("Times New Roman",30,"bold"))
w_label1.place(x=250,y=260,height=50,width=210)
wb_label = Label(win,text="Weather Description",font=("Times New Roman",17))
wb_label.place(x=25,y=330,height=50,width=210)
wb_label1 = Label(win,text="",font=("Times New Roman",17))
wb_label1.place(x=250,y=330,height=50,width=210)
temp_label = Label(win,text="Temperature",font=("Times New Roman",20))
temp_label.place(x=25,y=400,height=50,width=210)
temp_label1 = Label(win,text="",font=("Times New Roman",20))
temp_label1.place(x=250,y=400,height=50,width=210)
per_label = Label(win,text="Pressure",font=("Times New Roman",20))
per_label.place(x=25,y=470,height=50,width=210)
per_label1 = Label(win,text="",font=("Times New Roman",20))
per_label1.place(x=250,y=470,height=50,width=210)










win.mainloop()