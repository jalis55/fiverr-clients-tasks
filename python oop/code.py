from vernamcipher.cryptographic import Cryptographic

plaintext = "Hello World"
key = 'Hello likne'

encrypted_data = Cryptographic.exclusive_operations(plaintext, key)

decrypted_data = Cryptographic.exclusive_operations(encrypted_data, key)

print(encrypted_data)
print(decrypted_data)