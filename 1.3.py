hex = bytearray.fromhex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
winner = None
winner_count = 0

for i in range(256):
    candidate = bytes(a ^ i for (a) in hex).decode('ascii', errors='ignore')
    candidate_count = 0
    for c in candidate:
        if c.isalpha():
            candidate_count += 1
    if candidate_count > winner_count:
        winner = candidate
        winner_count = candidate_count

print(winner)
