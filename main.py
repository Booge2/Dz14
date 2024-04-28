import pickle
import gzip
import os


class CountriesAndCapitals:
    def __init__(self):
        self.data = {}

    def add_country(self, country, capital):
        self.data[country] = capital

    def delete_country(self, country):
        if country in self.data:
            del self.data[country]
            print(f"Country '{country}' deleted.")
        else:
            print(f"Country '{country}' not found.")

    def search_country(self, country):
        if country in self.data:
            print(f"The capital of '{country}' is '{self.data[country]}'.")
        else:
            print(f"Country '{country}' not found.")

    def edit_country(self, country, new_capital):
        if country in self.data:
            self.data[country] = new_capital
            print(f"The capital of '{country}' updated to '{new_capital}'.")
        else:
            print(f"Country '{country}' not found.")

    def save_data(self):
        with gzip.open("countries_data.pkl.gz", "wb") as file:
            pickle.dump(self.data, file)
        print("Data saved successfully.")

    def load_data(self):
        if os.path.exists("countries_data.pkl.gz"):
            with gzip.open("countries_data.pkl.gz", "rb") as file:
                self.data = pickle.load(file)
            print("Data loaded successfully.")
        else:
            print("File with countries data not found.")


countries = CountriesAndCapitals()

countries.add_country("Ukraine", "Kyiv")
countries.add_country("Germany", "Berlin")
countries.add_country("France", "Paris")

countries.save_data()

countries.delete_country("Germany")

countries.load_data()

countries.search_country("Ukraine")

countries.edit_country("Ukraine", "Lviv")


# Завдання 2
class MusicLibrary:
    def __init__(self):
        self.data = {}

    def add_group(self, group, albums):
        self.data[group] = albums

    def delete_group(self, group):
        if group in self.data:
            del self.data[group]
            print(f"Group '{group}' deleted.")
        else:
            print(f"Group '{group}' not found.")

    def search_group(self, group):
        if group in self.data:
            print(f"Albums by '{group}': {', '.join(self.data[group])}")
        else:
            print(f"Group '{group}' not found.")

    def edit_group(self, group, new_albums):
        if group in self.data:
            self.data[group] = new_albums
            print(f"Albums by '{group}' updated to: {', '.join(new_albums)}")
        else:
            print(f"Group '{group}' not found.")

    def save_data(self):
        with gzip.open("music_data.pkl.gz", "wb") as file:
            pickle.dump(self.data, file)
        print("Data saved successfully.")

    def load_data(self):
        if os.path.exists("music_data.pkl.gz"):
            with gzip.open("music_data.pkl.gz", "rb") as file:
                self.data = pickle.load(file)
            print("Data loaded successfully.")
        else:
            print("File with music data not found.")


music_library = MusicLibrary()

music_library.add_group("The Beatles", ["Abbey Road", "Revolver", "Sgt. Pepper's Lonely Hearts Club Band"])
music_library.add_group("Led Zeppelin", ["Led Zeppelin IV", "Physical Graffiti", "Houses of the Holy"])

music_library.save_data()

music_library.delete_group("The Beatles")

music_library.load_data()

music_library.search_group("Led Zeppelin")

music_library.edit_group("Led Zeppelin", ["Led Zeppelin II", "Led Zeppelin III"])
