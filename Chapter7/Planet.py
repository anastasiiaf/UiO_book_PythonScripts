import math as math
class Planet:
    def __init__(self, name, population, radius, mass):
        self.name = name
        self.population = population
        self.radius = radius
        self.mass = mass
        
    def density(self):
        return(self.mass/(4/3.0*math.pi*self.radius**3))
        
    def planet_info(self):
        print("Planet ",self.name," with radius of ",  self.radius, "m and mass of", self.mass , "kg has density of ", self.density(), "kg/m3 and population of ", self.population)

    
planet1 = Planet("Earth", 7497486172, 6371*1000, 5.972*1E+24)
planet1.planet_info()
print( planet1.name, "has a population of ", planet1.population)


"""
Program output:
  Planet  Earth  with radius of  6371000 m and mass of 5.972e+24 kg has density of  5513.258738589093 kg/m3 and population of  7497486172
  
  Earth has a population of  7497486172
"""