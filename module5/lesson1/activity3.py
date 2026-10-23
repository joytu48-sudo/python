class parrot:
    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age

bulu = parrot("Bulu",40)
subham = parrot("Subham", 14)

print(f"{bulu.name} ia a {bulu.species} whose age is {bulu.age}")
print(f"{subham.name} ia {bulu.name}'s child whose age is {subham.age} and also is a {subham.species}")