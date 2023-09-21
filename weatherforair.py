from tkinter import *
from PIL import ImageTk, Image
# ----------------------------Weather Info API - Air Quality With Tkinder in GUI ----------------------------------
import mysql.connector
from PIL.Image import ID
from mysql.connector import Error, cursor
import requests
import json
root = Tk()
root.title("Air Qulaity Index For USA Only!")
root.geometry("600x250")
root.configure(background='green')
frame = LabelFrame(root, text="Enter USA PIN#", padx=100, pady=50)
frame.pack(padx=10, pady=10)
frame.configure(background='yellow')

def zipvalue():
    zipcode=IntVar()
    zipcode = zip_Entrybox.get()
    print(zip_Entrybox.get())
    requesturl = 'http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode='\
                 +zipcode+'&distance=25&API_KEY=927FC7BD-2CBD-4128-9350-DCC5BE69DD38'
    print(requesturl)
    try:
        api_request = requests.get(requesturl)
        api_json = json.loads(api_request.content)
        city = api_json[0]['ReportingArea']
        quality = api_json[0]['AQI']
        category = api_json[0]['Category']['Name']
        api_json = f'City--->{city}\n AQI--->{quality}\n Categoty--->{category}'
        if (category == 'Good'):
            weather_color = '#0C0'
        elif (category == 'Moderate'):
            weather_color = '#FFFF00'
        elif (category == 'Unhealthy for senstive Groups'):
            weather_color = '#ff9900'
        elif (category == 'Unhealthy'):
            weather_color = '#FF0000'
        elif (category == 'Very Unhealthy'):
            weather_color = '#990066'
        elif (category == 'Hazardous'):
            weather_color = '#660000'
        my_label = Label(frame, text=api_json, font=("Helvetica", 20), background=weather_color)
        my_label.grid(row=5, column=0, columnspan=2)
    except Exception as e:
        api_json = (f"Error is {e}")
        my_label = Label(frame, text=api_json, font=("Helvetica", 20), background='red')
        my_label.grid(row=5, column=0, columnspan=2)

zipcode =StringVar()
zip_Entrybox = Entry(frame)
zip_Entrybox.grid(row=1, column=0, columnspan=2)
#zipcode1 =zip_Entrybox
#print(zipcode1)
#mybtn= Button(root,text='Click Me!',padx=100,pady=100,command=myClick,fg='blue',bg='green')
zip_btn=Button(frame,text='Search',command=zipvalue,fg='blue',bg='green')
zip_btn.grid(row=2,column=0,columnspan=2)

mainloop()
