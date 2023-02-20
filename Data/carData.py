from dataclasses import dataclass

@dataclass
class CarData:
        brand: str
        type: str
        price: str
        year: str
        fuelType: str
        gearBox: str
        mileage: str
        url: str
        
        def returnIterable(self):
                return [self.brand, self.type, self.price, self.year, self.fuelType, self.gearBox, self.mileage, self.url]