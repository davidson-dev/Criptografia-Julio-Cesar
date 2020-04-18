#importing
import requests
import json
import hashlib


#getting api response
r = requests.get("https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=SEU_TOKEN")
response = r.json() #attributing json to a variable

#saving json content
data = open('answer.json', "w")
json.dump(response, data)
data.close()

#getting content just in "cifrado" index to decrypt
encrypted = response["cifrado"]
print("Encrypted message: ", encrypted)

#will reiceve decrypted message
message = ""

#decrypting message
for m in encrypted:
    if chr(ord(m)).isidentifier(): #method to validate character
        
        if (ord(m) - response['numero_casas']) < 97: #"ord" parameter to indentify the character, from ASCII table each character has a 
            message += chr(ord(m) - response['numero_casas'] + 26) # index number. In this case, lower case letters starts from index 97
            
        else:
            message += chr(ord(m) - response['numero_casas']) #"chr" validate the character according to his index
            
    else:
        message += chr(ord(m)) #

print("\nDecrypted message: ", message)

#replacing json content that already exists with the answer
result = {
    'numero_casas': response['numero_casas'],
    'token': response['token'],
    'cifrado': response['cifrado'],
    'decifrado': message,
    'resumo_criptografico': hashlib.sha1(message.encode()).hexdigest() #encoding to sha1
	}

#saving new json content with the answer
data = open('answer.json', "w")
json.dump(result, data)
data.close()

#submitting the json file
url = ("https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=SEU_TOKEN")
files = {"answer": open("answer.json", "rb")}
r = requests.post(url, files=files)
print("\nSubmission status", r)






