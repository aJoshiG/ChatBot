import requests

url = "http://127.0.0.1:5000/chat"  # Ensure your Flask server is running

data = {"message": "Hello"}  # Test message
response = requests.post(url, json=data)  # Send POST request

print("Chatbot Response:", response.json())  # Print the chatbot's reply

