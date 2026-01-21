class car:
    def __init__(self, brand, color):
        self.color = color
        self.brand = brand
    
    def start(self):
        print(f"{self.color} {self.brand} is starting...")
    
    def stop(self):
        print(f"{self.color} {self.brand} has stopped.")
    
    def info(self):
        print(f"This car is a {self.color} {self.brand}.")


# Example usage
if __name__ == "__main__":
    my_car = car("Toyota", "Red")
    my_car.info()
    my_car.start()
    my_car.stop()