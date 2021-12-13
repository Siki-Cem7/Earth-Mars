import requests
import json


class Earth():

    def __init__(self):

        self.api_key = "57380ca145e7db79b903346d9c60090b"
        self.city_name = "Germany"
        self.url = f"http://api.openweathermap.org/data/2.5/weather?q={self.city_name}&appid={self.api_key}"
        self.resp_json = None
        self.data = None
        self.earth_temp = None




    def request(self):

        # Make the GET request to nasa API and save the data in Resp
        self.resp_json = requests.get(self.url)
        self.data = self.resp_json.json()
        print(self.data)


if __name__ == "__main__":

    earth = Earth()
    earth.request()