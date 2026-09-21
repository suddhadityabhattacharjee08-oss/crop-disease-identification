class Plant:
    def __init__(self, name, scientific_name, growing_season, water_requirement):
        self.name = name
        self.scientific_name = scientific_name
        self.growing_season = growing_season
        self.water_requirement = water_requirement

    def describe(self):
        print(f"\nCrop: {self.name}")
        print(f"Scientific name: {self.scientific_name}")
        print(f"Growing season: {self.growing_season}")
        print(f"Water requirement: {self.water_requirement}")

    def care(self):
        print(f"Use suitable soil, water, sunlight, and nutrient management for {self.name}.")


class Tomato(Plant):
    def care(self):
        print("Tomato: provide sunlight, moderate watering, and good air circulation.")


class Potato(Plant):
    def care(self):
        print("Potato: use well-drained soil, consistent moisture, and suitable temperatures.")


class Wheat(Plant):
    def care(self):
        print("Wheat: maintain suitable soil moisture, sunlight, and balanced nutrition.")


class Rice(Plant):
    def care(self):
        print("Rice: maintain adequate water availability and suitable growing conditions.")


class Maize(Plant):
    def care(self):
        print("Maize: provide sunlight, adequate moisture, and balanced soil nutrients.")
