from tkinter import*
from customtkinter import*
from tkinter import messagebox
import requests


def search():

    api_key = '30d4741c779ba94c470ca1f63045390a'
    user_input=var.get()

    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

    if weather_data.json()['cod'] == '404':
        messagebox.showerror("WARNING","No City Found")
    else:
        weather = weather_data.json()['weather'][0]['main']
        weather = "(",weather,")"
        temp = round(weather_data.json()['main']['temp'])
        temp = int(temp)

        tempe = ((temp-32)*5/9)

    
        lbl2 = Label(root,text = tempe,font=("comicstans 79 bold"),pady=15,bg = "#39a7f1")
        lbl2.place(x=10,y = 200)

        
        lbl5 =  Label(root,text="°C                                       ",font=("comicstans 79 bold"),pady=15,bg = "#39a7f1")
        lbl5.place(x = 218,y = 200)

        lbl4 = Label(root,text=weather,font=("comicstans 30 bold"),pady=15,bg = "#39a7f1")
        lbl4.place(x = 400,y = 250)

        


         



root = Tk()
root.geometry("644x344")
root.maxsize(644,344)
root.minsize(644,344)
root.title("Weather App")
root.config(background="#39a7f1")
lbl1 = Label(root,text = "WEATHER APP",font=("comicstans 16 bold"),pady=15,bg = "#39a7f1")
lbl1.place(x=260,y = 10)


lbl2 = Label(root,text = "City Name   -   ",font=("comicstans 13 bold"),padx = 5,bg = "#39a7f1")
lbl2.place(x = 10,y = 80)
var = StringVar()
ent1 = Entry(root,font=("comicstans 13 bold"),borderwidth=5,textvariable=var)
ent1.place(x = 180,y=80)



btn1 = Button(root,text = "Search Weather",fg ="white",bg = "#39a7f1",command=search,borderwidth=5,font=("comicstans 10 bold"))
btn1.place(x=450,y=80)




root.mainloop()