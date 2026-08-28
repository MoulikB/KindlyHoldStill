import math

def calculate_revolution_time(x,  speed, mu):

    # Simple allignment so y and z don't change in this scenario
    y = 0.0
    z = 0.0
    
    # 1. Calculate the current radius (distance from center)
    r = math.sqrt(x**2 + y**2 + z**2)

    # Keplerian Gravitational Orbit
    energy = (speed**2 / 2.0) - (mu / r)
    
    if energy >= 0:
        return "The object is on an escape trajectory (parabolic/hyperbolic) and will not complete a revolution."
    
    # Semi-major axis
    a = -mu / (2 * energy)
    # Kepler's Third Law for Period
    time_seconds = 2 * math.pi * math.sqrt(a**3 / mu)
    print(f"--- Gravitational Keplerian Orbit ---")
    # Converting seconds to hours for better readability if long
    print(f"Semi-major axis (a): {a:.2f}")
    print(f"Time for 1 Revolution: {time_seconds:.2f} seconds ({time_seconds/3600:.2f} hours)")
        
    return time_seconds

def calculate_coordinate_revolution(time,speed,mu):
    # 1. Find Semi Major Axis using Kepler's Third Law
    a = math.cbrt(mu*((time/(2*math.pi))**2))

    # 2. Find Radius
    # Specific energy (E) can be found directly from 'a' for a bound orbit: E = -mu / (2*a)
    energy = -mu / (2 * a)
    r = mu / ((speed**2 / 2.0) - energy)

    # 3. Map to sample X, Y, Z coordinates (assuming simple alignment)
    x = r
    y = 0.0
    z = 0.0
    
    print(f"--- Reverse Orbit: Finding Coordinates ---")
    print(f"Calculated Semi-major axis (a): {a:.4f} m")
    print(f"Coordinates are: ({r:.3e}, 0, 0)")
    return r


# Example Usage for Earth:
# Coordinates in meters, speed in m/s
t = calculate_revolution_time(x=1.496e11, speed=29780    , mu = 1.3271e20)
calculate_coordinate_revolution(t, 29780 , 1.3271e20)