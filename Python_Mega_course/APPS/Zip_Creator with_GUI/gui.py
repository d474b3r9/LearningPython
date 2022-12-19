import PySimpleGUI as sg
import zip_creator


label1 = sg.Text("Sele ct files to compress:")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress")
output_label = sg.Text(key="output", text_color="green")

window = sg.Window('My To-Do App', layout=[[label1, input1, choose_button1],
                                           [label2, input2, choose_button2],
                                           [compress_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    zip_creator.make_archive(filepaths, folder)
    window["output"].update(value="Compression Completed !")

window.close()