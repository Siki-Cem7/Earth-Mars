import sys

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
        self.earth_data()
        self.mars_photo()
        self.mars_data()



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
        self.image_earth.place(x=50, y=80)



    def city_choose(self):

        # I make a label and an spinbox to choose which city the user wanna compare with mars
        self.city_lbl = Label(self.root, text="Choose City: ", bg="black", fg="white", font=(self.font, 16))
        self.city_lbl.place(x=75, y=300)
        self.country_list = []



        with open("Country.txt", "r") as list:
            for line in list:
                self.country_list.append(line.rstrip())



        self.city = StringVar()
        self.city.set("Select your Country")
        self.city_opt = OptionMenu(self.root, self.city, *self.country_list)
        self.city_opt.place(x=100, y=350)
        self.city_opt.config(width=20)





    def earth_data(self):

        self.x = 50
        self.y = 420
        self.width = 107
        self.height = 15

        self.earth_data_lbl = Label()
        self.earth_data_lbl.config(width=self.width, height=self.height)
        self.earth_data_lbl.place(x=self.x, y=self.y)



    def mars_photo(self):

        self.bg = "black"
        self.pic_mars = "Mars.jpeg"

        self.mars_pic = Image.open(self.pic_mars)
        self.mars_pic = ImageTk.PhotoImage(self.mars_pic)
        self.image_mars = Label(image=self.mars_pic, bg=self.bg)
        self.image_mars.image = self.mars_pic
        self.image_mars.place(x=800, y=80)




    def mars_data(self):

        self.mars_data_lbl = Label()
        self.mars_day = StringVar()
        self.mars_day.set("Select day")
        self.mars_list = ["TEWSklsadjfkdnalköfdoihsakfjdajksljfdklösjbfnvaks<ödkjifdkfnjweik"]
        self.mars_data_opt = OptionMenu(self.root, self.mars_day, *self.mars_list)

        self.mars_data_lbl.config(width=20, height=2, text="Which day on Mars?", font=(self.font, 16), fg="white", bg=self.bg)
        self.mars_data_opt.config(width=20)

        self.mars_data_lbl.place(x=800, y=300)
        self.mars_data_opt.place(x=800, y=350)













if __name__ == "__main__":

    earth_to_mars = Earth_to_Mars()
