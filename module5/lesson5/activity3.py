class bangladesh:
    def capital(self):
        print("Dhaka is the capital od bangladesh")
    def lang(self):
        print("Bengali is their native language")
    def currency(self):
        print("Taka is their main currency\n")

class USA:
    def capital(self):
        print("Washington DC is the capital od USA")
    def lang(self):
        print("American english is their native language")
    def currency(self):
        print('US dollar is their main currency')

BD = bangladesh()
US = USA()

for country in BD, US:
    country.capital()
    country.lang()
    country.currency()