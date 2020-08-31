G = 6.673e-11 # Nm^2 kg^-2
c = 3e8 # m/s
au = 1.496e11 # metre
ly = 9.46e15 # metre
parsec = 3.261 # light years

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]

# Distances from sun (au) :
dist_sun = {
    "Mercury" : 0.39,
    "Venus" : 0.72,
    "Earth" : 1,
    "Mars" : 1.52,
    "Jupiter" : 5.2,
    "Saturn" : 9.5,
    "Uranus" : 19.19,
    "Neptune" : 30.07,
    "Pluto" : 39.5
}

# Radii of planets in km:
r = [2439.7, 6051.8, 6371, 3389.5, 69911, 58232, 25362, 24622, 1188.3]

# Planetary masses in kg:
mass = [3.285e23, 4.867e24, 5.9722e24, 6.39e23, 1.898e27, 5.683e26, 8.681e25, 1.024e26, 1.309e22]

def d_sun_to_p():
    print("Planet\t\tDistance from sun (AU)")
    for i, j in dist_sun.items():
        print(i,"\t\t",j)
    print("\n")

def r_s_planets():
    print("Planet\t\tSchwarzchild radius (metre)")
    for i in range(0,8):
        rs = 2*G*mass[i]/c**2
        print(planets[i],"\t\t", "{:e}".format(rs))
    print("\n")

def conv_to_m(unit,val):
    if unit == "AU":
        return val * au
    elif unit == "PARSEC":
        return val * 3.261 * ly
    elif unit == "LY":
        return val * ly

d_sun_to_p()
r_s_planets()
print(conv_to_m("AU", 1))