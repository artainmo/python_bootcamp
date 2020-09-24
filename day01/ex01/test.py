from game import GotCharacter, Stark

arya = Stark("Arya")
print(arya.__dict__)
# {'first_name': 'Arya', 'is_alive': True, 'family_name': 'Stark', 'house_words': 'Winter is Coming'}
arya.print_house_words()
# Winter is Coming
print(arya.is_alive)
arya.die()
print(arya.is_alive)
print(arya.__doc__)
