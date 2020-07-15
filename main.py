import PySimpleGUI as app
from pytube import YouTube


app.theme('DarkAmber')

layout = [
        [app.Text('Enter the video link below')],
        [app.Input()],
        [app.Button('Download')],
        ]

# create the window

window = app.Window('pyTube Downloader', layout, size=(400, 500))

while True:

    event, values = window.read()

    vidURL = values[0]

    YouTube(vidURL).streams.get_highest_resolution().download()


    if event == app.WIN_CLOSED or event == 'Cancel':
        break

window.close()
