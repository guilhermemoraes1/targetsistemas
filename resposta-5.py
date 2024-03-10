def inverter_string(original):
    invertida = ""

    for i in range(len(original) - 1, -1, -1):
        invertida += original[i]

    return invertida


string_original = "Palavra"
string_invertida = inverter_string(string_original)
print("String original:", string_original)
print("String invertida:", string_invertida)
