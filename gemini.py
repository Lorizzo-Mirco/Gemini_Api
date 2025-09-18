from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key="AIzaSyBSqLpZGGwXCN8zhADt6m7jOh71HvOMOGk")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Qual'è la capitale italiana"
)
print(response.text)