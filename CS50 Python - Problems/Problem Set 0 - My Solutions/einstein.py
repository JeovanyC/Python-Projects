def getEnergy(mass):
    energy = mass * 300000000 ** 2
    print("E: ", energy)

print("Tell me your mass, and I'll calculate your energy potential!")
weight = int(input("m:  "))

getEnergy(weight)