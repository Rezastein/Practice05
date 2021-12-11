kontak = {"Ari": 8126788, "Dina": 87677776}
print(kontak['Ari'])
kontak["Riko"] = 87654544
kontak["Dina"] = 88999776
print(kontak.keys())
print(kontak.values())
print(kontak.items())
del kontak["Dina"]
print(kontak.items())