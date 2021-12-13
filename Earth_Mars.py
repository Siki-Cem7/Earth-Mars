import Earth_Tem
import Mars_Tem
from tkinter import *
from PIL import Image, ImageTk
import random


class Earth_to_Mars():

    def __init__(self):

        # Make Window
        self.root = Tk()
        self.root.geometry("1080x720")
        self.root.config(bg="black")
        self.frame = Frame(self.root)
        self.frame.pack()
        self.font = "Apple Chancery"
        self.logo()
        self.photo_earth()
        self.city_choose()



        self.root.mainloop()



    def logo(self):

        # Place the logo in the program
        self.logo_lbl = Label(self.frame, text="Earth-to-Mars", font=(self.font, 50), bg="black", fg="white")
        self.logo_lbl.pack()


    def photo_earth(self):

        # Place the photo of earth in program
        self.photo_e = Image.open("Earth.jpeg")
        self.photo_e = ImageTk.PhotoImage(self.photo_e)
        self.image_earth = Label(image=self.photo_e, bg="black")
        self.image_earth.image = self.photo_e
        self.image_earth.place(x=30, y=80)



    def city_choose(self):

        # I make a label and an spinbox to choose which city the user wanna compare with mars
        self.city_lbl = Label(self.root, text="Choose City: ", bg="black", fg="white", font=(self.font, 25))
        self.city_lbl.place(x=50, y=300)
        self.country_list = []

        with open("country_list.txt") as list:
            for line in list:


                line = line.replace(",", "")
                line = line.replace("\"", "")
                line = line.replace(":", "")


                self.country_list.append(line.rstrip())


        print(self.country_list)


        self.city = StringVar()
        self.city.set("Country")
        self.city_opt = OptionMenu(self.root, self.city, *self.country_list)
        self.city_opt.place(x=30, y=350)










if __name__ == "__main__":

    earth_to_mars = Earth_to_Mars()
