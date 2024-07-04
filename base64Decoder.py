import base64

encoded_text = "eWVldA==" # zakodowana wiadomość
decoded_bytes = base64.b64decode(encoded_text)
decoded_text = decoded_bytes.decode('utf-8')

print(decoded_text)