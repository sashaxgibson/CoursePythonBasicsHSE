phones = {'police': 102, 'ambulance': 103, 'firefighters': 101}
for service, phone in phones.items():
    print(service, phone)
print(phones['police'])
pebis = 'dupa'
phones[pebis] = 'zhepa'
print(phones)
