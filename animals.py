with open('animals.txt') as file:
    animals = set(line.strip() for line in file)
    print(animals)