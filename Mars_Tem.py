import requests




class Mars():


    def __init__(self):

        # Initialize API key, url and resp
        self.api_key = "mqBn4UPKAYgA2QudGfROnCLaLE5lktHLUznRwXee"
        self.url = "https://api.nasa.gov/insight_weather/?api_key=mqBn4UPKAYgA2QudGfROnCLaLE5lktHLUznRwXee&feedtype=json&ver=1.0"
        self.resp_json = None
        self.data = None

        #Mars Weather
        self.sol_day = None
        self.mars_temp = None
        self.wind_speed = None
        self.atmospheric_press = None



    def request(self):

        # Make the GET request to nasa API and save the data in Resp
        self.resp_json = requests.get(self.url)
        self.data = self.resp_json.json()
        print(self.data)



    def get_actual_sol_day(self):

        tem_sol_days = self.data["sol_keys"][int(len(self.data["sol_keys"])) - 1]
        self.sol_day = tem_sol_days



    def get_temp_mars(self):

        # Mars temp in F
        self.mars_temp = self.data[self.sol_day]["AT"]["av"]



    def get_wind_mars(self):

        # Wind speed in m/s
        self.wind_speed = self.data[self.sol_day]["HWS"]["av"]



    def get_pressure_mars(self):

        # Atmospheric pressure in Pa
        self.atmospheric_press = self.data[self.sol_day]["PRE"]["av"]
