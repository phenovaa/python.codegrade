decimaal = 45
binair = bin(decimaal)
print(binair[2:])

binair = "1010101"
decimaal = int(binair, 2)
print(decimaal)

binair_a = "10111"
binair_b = "1101"
totaal_binair = binair_a + binair_b
binair_vorm = int(totaal_binair, 2)
print(binair_vorm)

decimaal = 255
hexadecimaal = hex(decimaal)
print(hexadecimaal)

hexadecimaal = "2A"
decimaal = int(hexadecimaal, 16)
print(decimaal)

hexadecimaal_a = 0xC4
hexadecimaal_b = 0x3A
totaal_hexadecimaal = hexadecimaal_a + hexadecimaal_b
print(hex(totaal_hexadecimaal)[2:])

binair = "1101"
decimaal = int(binair, 2)
print(decimaal)

hexadecimaal = "F0"
decimaal = int(hexadecimaal, 16)
print(decimaal)

decimaal_a = 123
decimaal_b = 456
totaal_decimaal = decimaal_a + decimaal_b
print(totaal_decimaal)

decimaal = 157
binair = bin(decimaal)
hexadecimaal = hex(decimaal)
print(binair[2:])
print(hexadecimaal[2:])

binair = "11101101"
decimaal = int(binair, 2)
hexadecimaal = hex(decimaal)
print(decimaal)
print(hexadecimaal)

hexadecimaal = "AB4"
decimaal = int(hexadecimaal, 16)
binair = bin(decimaal)
print(decimaal)
print(binair[2:])