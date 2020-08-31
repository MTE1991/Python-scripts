from math import pi

G = 6.673e-11 # Nm^2 kg^-2
c = 3e8 # m/s
au = 1.496e11 # metre
ly = 9.46e15 # metre
parsec = 3.261 # light years
mass_sun = 1.98447e30 # kg
planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto")

# Distances from sun (au) :
dist_sun = (0.39, 0.72, 1, 1.52, 5.2, 9.5, 19.19, 30.07, 39.5)

# Radii of planets in km:
r = (2439.7, 6051.8, 6371, 3389.5, 69911, 58232, 25362, 24622, 1188.3)

# Planetary masses in kg:
mass = (3.285e23, 4.867e24, 5.9722e24, 6.39e23, 1.898e27, 5.683e26, 8.681e25, 1.024e26, 1.309e22)

g = lambda m, r : G*m/r**2 # Gravity
d = lambda m, v : m/v # Density
r_sch = lambda m : 2*G*m/c**2 # Schwarzchild radius
d_sch = lambda r : 3*c**2/8*pi*G*r**2 # Schwarzchild density

#Schwarzchild radii and densities of planets:
def r_s_planets():
    print("Planet\t\tSchwarzchild radius (metre)\t\tSchwarzchild density (kg/mˆ3)")
    for i in range(1,8):
        print(planets[i], "\t\t", r_sch(mass[i]).__format__(".3e"), "\t\t\t\t", d_sch(mass[i]).__format__(".3e"))
    print("\n")

# Distances from sun:  
def sun_to_p():
    print("Planet\t\tDistance from sun (AU)")
    for i in range(0,8):
        print(planets[i], "\t\t", dist_sun[i])
    print("\n")

# AU, ly or parsec to metre:
def conv_to_m(unit,val):
    if unit == "AU":
        return val * au
    elif unit == "PARSEC":
        return val * 3.261 * ly
    elif unit == "LY":
        return val * ly

sun_to_p()
r_s_planets()
print("0.7 AU = ", conv_to_m("AU", 0.7).__format__(".3e"),"m \n")
print("g in earth = ", g(mass[2], r[2]*1000).__format__(".3f"), "m/sˆ2\n")
print("Schwarzchild radius of sun = ", r_sch(mass_sun), "m \n")
