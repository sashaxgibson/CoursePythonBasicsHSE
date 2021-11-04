phones = {'police': 102, 'ambulance': 103, 'firefighters': 101}
for service, phone in phones.items():
    print(service, phone)
print(phones['police'])
pebis = 'dupa'
phones[pebis] = 'zhepa'
phones['benis'] = 'bagina'
print(phones)
phones['police'] = phones['police'] * 100
print(phones['police'] + 1)
