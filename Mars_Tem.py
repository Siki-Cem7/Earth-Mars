import requests




class Mars():


    def __init__(self):

        # Initialize API key, url and resp
        self.api_key = "mqBn4UPKAYgA2QudGfROnCLaLE5lktHLUznRwXee"
        self.url = "https://api.nasa.gov/insight_weather/?api_key=mqBn4UPKAYgA2QudGfROnCLaLE5lktHLUznRwXee&feedtype=json&ver=1.0"
        self.resp_json = None
        self.data = None
        self.mars_temp = None




    def request(self):

        # Make the GET request to nasa API and save the data in Resp
        self.resp_json = requests.get(self.url)
        self.data = self.resp_json.json()
        print(self.data)



    def get_temp(self):

        None




if __name__ == "__main__":

    mars = Mars()
    mars.request()
