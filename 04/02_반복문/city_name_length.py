cities = ['seoul', 'daejeon', 'kimpo', 'suncheon', 'pusan']

cities_length = []
for city in cities:
    cities_length.append(len(city))

# print(max(cities_length), min(cities_length))
longest_length = max(cities_length)
shortest_length = min(cities_length)

longest_list = []
shortest_list = []

for city in cities:
    if len(city) == longest_length:
        longest_list.append(city)
    elif len(city) == shortest_length:
        shortest_list.append(city)
print(f"Long Name City: {''.join(longest_list)}")
print(f"Short Name City: {', '.join(shortest_list)}")