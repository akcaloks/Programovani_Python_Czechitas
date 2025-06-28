#Úkol 1 - Jana Barotová

from math import ceil
from abc import ABC, abstractmethod

class Locality:
    def __init__(self, name: str, locality_coefficient: float):
        self.name = name
        self.locality_coefficient = locality_coefficient

class Property(ABC):
    def __init__(self, locality: Locality):
        self.locality = locality

    @abstractmethod
    def calculate_tax(self):
        pass

class Estate(Property):
    def __init__ (self, locality: Locality, estate_type: str, area: float):
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area

    def __str__(self):
        return f"Nemovitost v katastrálním území {self.locality.name}, rozloha: {self.area} m², daň: {self.calculate_tax()} Kč."


    def calculate_tax(self):
        if self.estate_type == "land":
            coef = 0.85
        elif self.estate_type == "building_site":
            coef = 9
        elif self.estate_type == "forrest":
            coef = 0.35
        elif self.estate_type == "garden":
            coef = 2
        else:
            raise ValueError("Unknown estate type")

        tax = self.area * coef * self.locality.locality_coefficient
        return ceil(tax) 
    
class Residence(Property):
    def __init__ (self, locality: Locality, area: float, commercial: bool):
        super().__init__(locality)
        self.area = area
        self.commercial = commercial

    def calculate_tax(self):
        result = self.area * self.locality.locality_coefficient * 15
        if self.commercial:
            return result * 2
        return result
    
    def __str__(self):
        commercial_str = "komerční" if self.commercial else "rezidenční"
        return f"Nemovitost v katastrálním území {self.locality.name}, způsob využití: {commercial_str}, rozloha: {self.area} m², daň: {self.calculate_tax()} Kč."
    
class TaxReport:
    def __init__(self, name, property_list: list):
        self.name = name
        self.property_list = property_list  

    def add_property(self, property_object: object):
        self.property_list.append(property_object)

    def calculate_total_tax(self):
        total_tax = 0
        for property_object in self.property_list:
            total_tax += property_object.calculate_tax()
        return total_tax

manetin = Locality("Manětín", 0.8)
brno = Locality("Brno", 3)

zem_pozemek_manetin = Estate(manetin, "land", 900)
dum_manetin = Residence(manetin, 120, False)
kancelar_brno = Residence(brno, 90, True) 

report = TaxReport("Jana Nováková", [])
report.add_property(zem_pozemek_manetin)
report.add_property(dum_manetin)
report.add_property(kancelar_brno)

print(f"Daňové přiznání pro {report.name}")
print(zem_pozemek_manetin)
print(dum_manetin) 
print(kancelar_brno)
print(f"Celková daň: {report.calculate_total_tax()} Kč")