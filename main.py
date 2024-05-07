import json
import pickle

class Airplane:
    def __init__(self, model, capacity, manufacturer):
        self.model = model
        self.capacity = capacity
        self.manufacturer = manufacturer

    def __repr__(self):
        return f"Airplane(model='{self.model}', capacity={self.capacity}, manufacturer='{self.manufacturer}')"

    def pack_pickle(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
        print(f"{self.model} packed into {filename} using pickle.")

    @staticmethod
    def unpack_pickle(filename):
        with open(filename, 'rb') as file:
            plane = pickle.load(file)
        print(f"{filename} unpacked using pickle.")
        return plane

    def pack_json(self, filename):
        data = {
            'model': self.model,
            'capacity': self.capacity,
            'manufacturer': self.manufacturer
        }
        with open(filename, 'w') as file:
            json.dump(data, file)
        print(f"{self.model} packed into {filename} using JSON.")

    @staticmethod
    def unpack_json(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        plane = Airplane(data['model'], data['capacity'], data['manufacturer'])
        print(f"{filename} unpacked using JSON.")
        return plane

# Example usage:
airplane1 = Airplane("Boeing 747", 416, "Boeing")
airplane1.pack_pickle("airplane_pickle.pkl")
airplane2 = Airplane.unpack_pickle("airplane_pickle.pkl")

airplane1.pack_json("airplane_json.json")
airplane3 = Airplane.unpack_json("airplane_json.json")

print(airplane2)
print(airplane3)
