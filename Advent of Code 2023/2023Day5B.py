import re

class Seed:
    def __init__(self, seed):
        self.seed_number = seed
        self.soil_number = None
        self.fert_number = None
        self.water_number = None
        self.light_number = None
        self.temp_number = None
        self.humidity_number = None
        self.location_number = None

    def seed_to_soil(self):
        directions = re.findall(r'(\d+) (\d+) (\d+)', maps[1])
        for direction in directions:
            soil, seed, change = map(int, direction)
            if self.seed_number in range(seed, seed + change):
                self.soil_number = self.seed_number + soil - seed
        if self.soil_number == None:
            self.soil_number = self.seed_number
        return self.soil_number

    def soil_to_fertilizer(self):
        self.seed_to_soil()
        directions = re.findall(r'(\d+) (\d+) (\d+)', maps[2])
        for direction in directions:
            fert, soil, change = map(int, direction)
            if self.soil_number in range(soil, soil + change):
                self.fert_number = self.soil_number + fert - soil
        if self.fert_number == None:
            self.fert_number = self.soil_number
        return self.fert_number

    def fertilizer_to_water(self):
        self.soil_to_fertilizer()
        directions = re.findall(r'(\d+) (\d+) (\d+)', maps[3])
        for direction in directions:
            water, fert, change = map(int, direction)
            if self.fert_number in range(fert, fert + change):
                self.water_number = self.fert_number + water - fert
        if self.water_number == None:
            self.water_number = self.fert_number
        return self.water_number

    def water_to_light(self):
        self.fertilizer_to_water()
        directions = re.findall(r'(\d+) (\d+) (\d+)', maps[4])
        for direction in directions:
            light, water, change = map(int, direction)
            if self.water_number in range(water, water + change):
                self.light_number = self.water_number + light - water
        if self.light_number == None:
            self.light_number = self.water_number
        return self.light_number

    def light_to_temp(self):
        self.water_to_light()
        directions = re.findall(r'(\d+) (\d+) (\d+)', maps[5])
        for direction in directions:
            temp, light, change = map(int, direction)
            if self.light_number in range(light, light + change):
                self.temp_number = self.light_number + temp - light
        if self.temp_number == None:
            self.temp_number = self.light_number
        return self.temp_number

    def temp_to_humidity(self):
        self.light_to_temp()
        directions = re.findall(r'(\d+) (\d+) (\d+)', maps[6])
        for direction in directions:
            humidity, temp, change = map(int, direction)
            if self.temp_number in range(temp, temp + change):
                self.humidity_number = self.temp_number + humidity - temp
        if self.humidity_number == None:
            self.humidity_number = self.temp_number
        return self.humidity_number

    def humidity_to_location(self):
        self.temp_to_humidity()
        directions = re.findall(r'(\d+) (\d+) (\d+)', maps[7])
        for direction in directions:
            location, humidity, change = map(int, direction)
            if self.humidity_number in range(humidity, humidity + change):
                self.location_number = self.humidity_number + location - humidity
        if self.location_number == None:
            self.location_number = self.humidity_number
        return self.location_number


with open("Day5Input") as f:
    input = f.read()
maps = input.split('\n\n')
min_location = float('inf')
location_list = []
seeds1 = re.findall(r'(\d+) (\d+)', maps[0])
seeds2 = list(seeds1)
for seeds3, interval in seeds2:
    for x in range(int(seeds3), int(seeds3) + int(interval)):
        seed = Seed(x)
        a = seed.humidity_to_location()
        min_location = min(a, min_location)
        print(min_location)
print("Location:", min_location)