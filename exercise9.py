cities = []
while True:
    city = input("Enter a city name (or type 'stop' to finish): ").strip()
    if city.lower() == 'stop':
        break
    population = len(city.replace(" ", "")) * 1_000_000
    cities.append((city, population))

sorted_cities = sorted(cities, key=lambda x: x[1], reverse=True)

print("\nCities and their populations:")
for city, population in sorted_cities:
    print("The city " + str(city) + " has "+ str(len(city.replace(" ", ""))) +" letters, so its population is " + str(population))
