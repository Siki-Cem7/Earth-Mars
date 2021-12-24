import requests
import json





class Earth():

    def __init__(self):

        self.api_key = "57380ca145e7db79b903346d9c60090b"
        self.resp_json = None
        self.data = None

        # Earth Weather
        self.country_name = ""
        self.country_temp = None
        self.sky = None
        self.atmospheric_press = None
        self.wind_speed = None
        self.coordx = None
        self.coordy = None

        self.url = f"http://api.openweathermap.org/data/2.5/weather?q={self.country_name}&appid={self.api_key}"





    def request(self):

        # Make the GET request to nasa API and save the data in Resp
        self.resp_json = requests.get(self.url)
        self.data = self.resp_json.json()
        print(self.data)



    def get_temp_earth(self):

        # Temp in Kelvin
        self.country_temp = self.data["main"]["temp"]



    def get_sky_earth(self):

        self.sky = self.data["weather"]["description"]



    def get_pressure_earth(self):

        # Pressure in hPa
        self.atmospheric_press = self.data["main"]["pressure"]



    def get_wind_earth(self):

        # Wind speed in m/s
        self.wind_speed = self.data["wind"]["speed"]



    def get_coord_earth(self):

        self.coordx = self.data["coord"]["lon"]
        self.coordy = self.data["coord"]["lat"]
