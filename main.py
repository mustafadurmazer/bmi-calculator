import tkinter
from PIL import Image, ImageTk

window = tkinter.Tk()
window.title("BmiCalculator")
window.minsize(300, 350)
window.configure(bg="light green")

img = Image.open("indir.jpg")
resizeimg = img.resize((150, 150))
new_image = ImageTk.PhotoImage(resizeimg)

myLabel = tkinter.Label(image=new_image)
myLabel.pack()

def hesaplama():
    try:
        boy = int(myEntry.get())
        kilo = int(myEntry2.get())
        bmi = kilo / ((boy * boy) / 10000)

        if bmi <= 20:
            result_text = f"Senin Bmi'n = {bmi:.2f}, Bmi<=20.Krakersin"
        elif 20 < bmi <= 30:
            result_text = f"Senin Bmi'n = {bmi:.2f}, 20<Bmi<=30.Kilon Normal"
        elif 30 < bmi <= 40:
            result_text = f"Senin Bmi'n = {bmi:.2f}, 30<Bmi<=40.Obezsin"
        else:
            result_text = f"Senin Bmi'n = {bmi:.2f}, Bmi>40. İneksin!"

        myLabel4.config(text=result_text)
        myLabel4.place(relx=0.5, rely=0.80, anchor="n")

    except ValueError:
        myLabel4.config(text="Hata: Geçerli sayısal bir değer girin!")
        myLabel4.place(relx=0.5, rely=0.80, anchor="n")

myButton = tkinter.Button(text="Hesapla", command=hesaplama)
myButton.config(width=10)
myButton.pack()
myButton.place(x=110, y=310)

myLabel1 = tkinter.Label(text="BmiCalculatore Hosgeldiniz", font=('Arial', 13))
myLabel1.config(bg="light green", fg="black")
myLabel1.pack()

myLabel2 = tkinter.Label(text="Boyunuzu Giriniz", font=('Arial', 9))
myLabel2.config(bg="light green", fg="gray")
myLabel2.pack()

myEntry = tkinter.Entry(width="20")
myEntry.pack()
myEntry.place(x=88, y=200)

myLabel3 = tkinter.Label(text="Kilonuzu Giriniz", font=('Arial', 9))
myLabel3.config(bg="light green", fg="gray")
myLabel3.pack()
myLabel3.place(x=102, y=225)

myEntry2 = tkinter.Entry(width="20")
myEntry2.pack()
myEntry2.place(x=88, y=250)

myLabel4 = tkinter.Label(text="", font=('Arial', 9))
myLabel4.pack()

window.mainloop()
