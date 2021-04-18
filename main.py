import base64

#private key
key = "saidimneverlackingalwayspistolpackingwitthemautomaticswegonsendthemtoheaven"

#get the message input
message = input("Enter your message: ")

encrypted = []

#encrypt letter by letter with the key
for i in range(len(message)):
    key_c = key[i%len(key)]
    encrypted.append(chr(ord(message[i]) + ord(key_c)%256))
encryption = base64.urlsafe_b64encode("".join(encrypted).encode()).decode()
print("The Encrypted message is : "+ encryption)

#decrypt the message 
decrypt = []
message = base64.urlsafe_b64decode(encryption).decode()
for i in range(len(message)):
    key_c = key[i%len(key)]
    decrypt.append(chr((256 + ord(message[i]) - ord(key_c))%256))
print("The decrypted message is : "+ "".join(decrypt))

