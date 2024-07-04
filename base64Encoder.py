import base64

decoded_text = "sam jesteś upo"
decoded_bytes = decoded_text.encode('utf-8')
encoded_bytes = base64.b64encode(decoded_bytes)
encoded_text = encoded_bytes.decode('utf-8')

print(encoded_text)