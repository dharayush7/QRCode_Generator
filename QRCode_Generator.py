from tkinter import *
from tkinter import ttk
import qrcode


def gtdata():
    global url
    global nm
    global size
    global border
    global colour
    
    url = urltxt.get()
    nm = text1.get()
    size = size_combo.get()
    border = border_combo.get()
    colour = colour_combo.get()

def condata():
    global consize
    global conborder
    global concolour
    
    if "Small" in size:
        consize = 10
    elif "Mediam(Recomonded)" in size:
        consize = 20
    elif "Big" in size:
        consize = 40
    else:
        consize = 20
    
    if "Small" in border:
        conborder = 2
    elif "Mediam(Recomonded)" in border:
        conborder = 5
    elif "Big" in border:
        conborder = 10
    else:
        conborder = 5
    
    concolour = colour.lower()
        
def main():
    qr = qrcode.QRCode(version=1,
                    error_correction = qrcode.constants.ERROR_CORRECT_H,
                    box_size = consize,border = conborder,)
    qr.add_data(url)
    qr.make(fit = True)
    img = qr.make_image(fill_color= concolour)
    img.save(nm+"qrcode.png")
    

    
def lb(text:"str",X_coordinate:"float",Y_coordinate:"float"):
    label3 = Label(
        canva,
        text = text,
        font = ("Roboto",20),
        bg = "#ffffff",
        highlightthickness=0,
        fg="black",
        bd=0,
        anchor=W
    )
    label3.place(
        x=X_coordinate,y=Y_coordinate,
        width=500,
        height=30
    )


def b0cl():
    label2.config(text="Loading...")
    try:
        
        lb("Getting Data...",0,35)
        gtdata()
        condata()
        
        lb("Processing..",0,70)
        if nm == "" or url == "":
            lb("A error occurred",0,105)
            lb("URL or image name is empty!",0,140)
        else:
            main()
            pt ="Your QR Code saved as "+ nm +"qrcode.png"
            lb(pt,0,105)
        
    except:
        lb("A error occurred",0,35)
        
    
    
window = Tk()
window.title("QRCode_Generator")
window.geometry("1000x700")
window.config(bg="#9b9b9b")

label = Label(
    window, 
    text = "QR Code Generetor",
    font = ("Roboto",30,"bold"),
    bg = "#9b9b9b",
    fg="black",
    bd=0,
)
label.place(
    x=0,y=50,
    width=1000,
    height=40
)

label = Label(
    window, 
    text = "Enter Your URL or Massage bellow:",
    font = ("Roboto",15),
    bg = "#9b9b9b",
    fg="black",
    bd=0,
    anchor=W
)
label.place(
    x=50,y=125,
    width=320,
    height=25
)
urltxt = Entry(
    window,
    textvariable="",
    font=("Roboto",20),
    highlightthickness=1,
    borderwidth=2,
    # border=0,
    bg="#ffffff"
    
)
urltxt.place(
    x= 50,y=150,
    height=50,
    width=900
)

size_list = [
    "Small",
    "Mediam(Recomonded)",
    "Big"
]

label=Label(
    window, 
    text = "Size:",
    font = ("Roboto",15),
    bg = "#9b9b9b",
    fg="black",
    bd=0,
)
label.place(
    x=50,y=220,
    width=300,
    height=20
)

size_combo = ttk.Combobox(
    window,font=("Roboto",20),
    value = size_list,
)
size_combo.place(
    x=50,y=250,
    width=293.3,
    height=50
)
size_combo.set("Mediam(Recomonded)")

border_list = [
    "Small",
    "Mediam(Recomonded)",
    "Big"
]

label=Label(
    window, 
    text = "border:",
    font = ("Roboto",15),
    bg = "#9b9b9b",
    fg="black",
    bd=0,
)
label.place(
    x=353.3,y=220,
    width=293.3,
    height=20
)

border_combo = ttk.Combobox(
    window,font=("Roboto",20),
    value = border_list,
)
border_combo.place(
    x=353.3,y=250,
    width=293.3,
    height=50
)
border_combo.set("Mediam(Recomonded)")

colour_list = [
    "Black",
    "Red",
    "Blue",
    "Yellow",
    "Green"
]

label=Label(
    window, 
    text = "Colour:",
    font = ("Roboto",15),
    bg = "#9b9b9b",
    fg="black",
    bd=0,
)
label.place(
    x=656.6,y=215,
    width=293.3,
    height=25
)

colour_combo = ttk.Combobox(
    window,font=("Roboto",20),
    value = colour_list,
)
colour_combo.place(
    x=656.6,y=250,
    width=293.3,
    height=50
)
colour_combo.set("Black")

label=Label(
    window, 
    text = "Enter image name",
    font = ("Roboto",15),
    bg = "#9b9b9b",
    fg="black",
    bd=0,
)
label.place(
    x=50,y=315,
    width=160,
    height=25
)

text1 = Entry(
    window,
    textvariable = "",
    font=("Roboto",20),
    highlightthickness=1,
    borderwidth=2,
    # border=0,
    bg="#ffffff"
    
)
text1.place(
    x= 50,y=340,
    height=50,
    width=450
)

b0 = Button(
    window,
    text="GENERET",
    font=("Roboto",35),
    relief=RAISED,
    command=b0cl
)
b0.place(
    x=600,y=340,
    height=50,
    width=280
)

label=Label(
    window, 
    text = "Status:",
    font = ("Roboto",15),
    bg = "#9b9b9b",
    fg="#262626",
    bd=0,
)
label.place(
    x=50,y=420,
    width=450,
    height=25
)

canva=Canvas(
    window,
    background="#ffffff",
    bd=1,
    
)
canva.place(
    x=50,y=450,
    height=200,
    width=500
)

label2=Label(
    canva, 
    text = "empty",
    font = ("Roboto",20),
    bg = "#ffffff",
    highlightthickness=0,
    fg="black",
    bd=0,
    anchor=W
)
label2.place(
    x=0,y=0,
    width=450,
    height=30
)



window.mainloop()