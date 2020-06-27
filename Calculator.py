from tkinter import*

calc_app=Tk()
calc_app.title("Python Calculator")
calc_app.geometry("300x400")

#calc_frame=Frame(calc_app,bg="gray",width=300,height=400)
#calc_frame.grid(row=0,column=0,sticky="NW")
#calc_frame.grid_propagate(0)
#calc_frame.update()


home_label=Label(calc_app,text="PYTHON CALCULATOR",fg="red",anchor="center")
#home_label.place(x=25,y=25,anchor="center")
home_label.grid(row=0,column=0)

calc_app.mainloop()
