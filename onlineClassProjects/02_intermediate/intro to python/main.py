"""
Prompts the user for a weight on Earth
and a planet (in separate inputs). Then 
prints the equivalent weight on that planet.

Note that the user should type in a planet with 
the first letter as uppercase, and you do not need
to handle the case where a user types in something 
other than one of the planets (that is not Earth). 
"""

def main():
    # Get Earth weight and planet from user
    earth_weight = float(input("Enter a weight on Earth: "))
    planet = input("Enter a planet: ")
    
    # Capitalize the first letter of the planet name for output
    planet = planet.capitalize()
    
    # Define gravitational constants
    if planet == "Mercury":
        gravity = 0.376
    elif planet == "Venus":
        gravity = 0.889
    elif planet == "Mars":
        gravity = 0.378
    elif planet == "Jupiter":
        gravity = 2.36
    elif planet == "Saturn":
        gravity = 1.081
    elif planet == "Uranus":
        gravity = 0.815
    elif planet == "Neptune":
        gravity = 1.14
    
    # Calculate weight on the planet
    planet_weight = earth_weight * gravity
    
    # Round to 2 decimal places
    planet_weight = round(planet_weight, 2)
    
    # Print result
    print(f"The equivalent weight on {planet}: {planet_weight}")

if __name__ == "__main__":
    main()