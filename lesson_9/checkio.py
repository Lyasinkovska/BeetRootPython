dct = {'name': "Enter name", 'lastname': 'Enter lastname:'}

print({k: input(v) for k, v in dct.items()})