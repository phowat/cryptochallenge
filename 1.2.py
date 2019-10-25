
hex = bytearray.fromhex('1c0111001f010100061a024b53535009181c')
x = bytearray.fromhex('686974207468652062756c6c277320657965')

one_xor_two = bytes(a ^ b for (a, b) in zip(hex, x))

print(one_xor_two.hex())
