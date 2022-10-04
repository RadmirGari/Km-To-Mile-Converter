import tkinter as t

window = t.Tk()
window.title("KM to Mile Super Calc")
window.minsize(width=400, height=200)
label_km = t.Label(text="KM")
label_km.grid(column=2, row=0)
label_is = t.Label(text="is ")
label_is.grid(column=0, row=1)
label_miles = t.Label(text="Miles")
label_miles.grid(column=2, row=1)
label_text = t.Label(text=0)
label_text.grid(column=1, row=1)

def convert():
    Km = int(entry.get())
    Miles = (Km / 1.609)
    label_text.config(text=f"{Miles}")

button = t.Button(text="Convert", command=convert)
button.grid(column=1, row=2)

entry = t.Entry()
entry.grid(column=1, row=0)

window.mainloop()