
def encode_cipher(s: str, shift: int) -> str:
    so = []
    for ch in s:
        if 'a' <= ch <= 'z':
            so.append(chr((ord(ch) - ord('a') + shift) % 26 + ord('a')))
        elif 'A' <= ch <= 'Z':
            so.append(chr((ord(ch) - ord('A') + shift) % 26 + ord('A')))
        else:
            so.append(ch)  
    return ''.join(so)


def decode_cipher(s: str, shift: int) -> str:
    return encode_cipher(s, -shift)

if __name__ == "__main__":
  print(encode_cipher("abc", 3))
  print(decode_cipher("abc", 3))

# prof solution
alphabet = "abcdefghijklmnopqrstuvwxyz"
shift = 3
cipher = {}

for i, letter in enumerate(alphabet):
  cipher[letter] = alphabet[(i + shift) % len(alphabet)]

message = "see me after class"
encoded = "".join(cipher.get(ch, ch) for ch in message)
print(encoded)

# ---
#build decoder
inverse_cipher = {v:k for k, v in cipher.items()}
original = "".join(inverse_cipher.get(ch, ch) for ch in encoded)
print(original)

ciphertext = "tlla ha aol spiyhyf hmaly zjovvs dl dpss zabkf avnlaoly mvy aol alza"
# <my solution>
for i in range(10):
  print(decode_cipher(ciphertext, i))
# </ my solution>
