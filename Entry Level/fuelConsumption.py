def liters_100km_to_miles_gallon(liters):
    
    litresPerKm = liters/100
    litresPerMile = litresPerKm * 1.609344
    gallonsPerMile = litresPerMile / 3.785411784
    milePerGallon = 1/gallonsPerMile

    return milePerGallon

def miles_gallon_to_liters_100km(miles):

    milesPerLitre = miles/3.785411784
    kmPerLitre = milesPerLitre * 1.609344
    litrePerKm = 100/kmPerLitre
    
    return litrePerKm

print(liters_100km_to_miles_gallon(3.9)) 
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
