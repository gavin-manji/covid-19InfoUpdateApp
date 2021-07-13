import requests as r
import json
from tkinter import *
import tkinter as tk

window = Tk()

# Window Configurations
window.title('COVID-19 Info Update')
window.geometry('400x300')


# To arrange/ modify the GUI using canvas
canvas = tk.Canvas(window, bg="#325ea1")


# To attach the canvas to root
canvas.pack()


# Adding a frame
frame = tk.Frame(window, bg="light blue")
# Arranging the height, width and leaving space around(to make the frame centered)
frame.place(relwidth=0.7, relheight=0.7, relx=0.15, rely=0.15)

# Title or the main heading of the GUI
label = Label(window, text='COVID-19 INFO GUI', bg='Yellow')
label.pack()

frame = tk.Frame(window, bg="light blue")
# Arranging the height, width and leaving space around(to make the frame centered)
frame.place(relwidth=0.7, relheight=0.7, relx=0.15, rely=0.15)


def localCovidInfo():
    # api url used which is provided by hpb.health.gov.lk
    url = 'https://www.hpb.health.gov.lk/api/get-current-statistical'

    response = r.request("GET", url)

    info = json.loads(response.text)

    covidUpdate = []

    # Update Time printing by default
    updateDateTime = info['data']['update_date_time']

    # Local Cases Information
    localNewCases = info['data']['local_new_cases']
    localTotalCases = info['data']['local_total_cases']
    localTotalDeaths = info['data']['local_deaths']
    localNewDeaths = info['data']['local_new_deaths']

    infoLocalCases = f"Details Updated Date and Time: {updateDateTime} \n \n" \
                     f"Number of Local New Cases: {localNewCases} \n" \
                     f"The Total Number of Local Cases: {localTotalCases} \n\n" \
                     f"The Number of New Deaths: {localNewDeaths}\n" \
                     f"The Total Number of Local Deaths: {localTotalDeaths} \n" \

    covidUpdate.append(infoLocalCases)

    # writing the updated details to a .txt file
    with open('SL Covid19 Stats Update.txt', 'a') as s:
        for i in covidUpdate:
            s.write(i + '\n')
            s.write('----------------------- \n')

    # Output message in the GUI, with the covid19 local updated info
    output_message.set(infoLocalCases)


# Creating a button
button = Button(frame, text='Show Local Covid-19 Info Update', fg='white', bg='black', command=localCovidInfo)
button.pack()

# Output a blank line
label = Label(frame, text='\n', bg='light blue')
label.pack()

# Displaying the Output in the GUI
output_message = StringVar()
label = Label(frame, textvariable=output_message, bg='light blue')
label.pack()


window.mainloop()
