from tkinter import *
import tkinter as tk 
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root=Tk()
root.title("Weather App By Aryan.co")
root.geometry("900x500+300+200")
root.resizable(False,False)
root.iconphoto(True, tk.PhotoImage(file="Copy of logo.png"))

def getweather():
    try:
        city=textfield.get()

        geolocator=Nominatim(user_agent="geoapiExercises")
        location=geolocator.geocode(city)
        obj=TimezoneFinder()
        result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
    
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="Current Weather")

    #Weather...

        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=96b2588cbd77f1f1130e0b0ea9f1cbf3"

        json_data=requests.get(api).json()
        condition=json_data['weather'][0]['main']
        description=json_data['weather'][0]['description']
        temp=int(json_data['main']['temp']-273.15)
        pressure=json_data['main']['pressure']
        humidity=json_data['main']['humidity']
        wind=json_data['wind']['speed']

        t.config(text=(temp,"°"))
        c.config(text=(condition ,"|","FEELS","LIKE",temp,"°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    except Exception as e:
        messagebox.showerror("Weather App by Aryan.co","Invalid Entry !!")




#Search Box implementation
search_image=PhotoImage(file="Copy of search.png")
my_image=Label(image=search_image)
my_image.place(x=20,y=20)

textfield=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",fg="white",border=0)
textfield.place(x=50,y=40)
textfield.focus()

search_icon=PhotoImage(file="Copy of search_icon.png")
searchimg=Button(image=search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getweather)
searchimg.place(x=400,y=34)

#logo implementation
Logo_img=PhotoImage(file="Copy of logo.png")
Logo=Label(image=Logo_img)
Logo.place(x=150,y=100)

#Bottom Box implementation
frame_1=PhotoImage(file="Copy of box.png")
frame_myimg=Label(image=frame_1)
frame_myimg.pack(padx=5,pady=5,side=BOTTOM)

#Time 
name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("helvetica",20))
clock.place(x=30,y=130)

#Label Implementataion
label1=Label(root,text="Wind",font=("helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)

label2=Label(root,text="Humidity",font=("helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label2.place(x=250,y=400)

label3=Label(root,text="Description",font=("helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label3.place(x=430,y=400)

label4=Label(root,text="Pressure",font=("helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label4.place(x=650,y=400)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("Arial",15,"bold"))
c.place(x=400,y=250)

w=Label(text="...",font=("Arial",20,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)

h=Label(text="...",font=("Arial",20,"bold"),bg="#1ab5ef")
h.place(x=250,y=430)

d=Label(text="...",font=("Arial",20,"bold"),bg="#1ab5ef")
d.place(x=430,y=430)

p=Label(text="...",font=("Arial",20,"bold"),bg="#1ab5ef")
p.place(x=650,y=430)








root.mainloop()

#End of my 2nd Project(mini)....


