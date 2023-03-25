import requests

url = "https://chatgpt-4-bing-ai-chat-api.p.rapidapi.com/chatgpt-4-bing-ai-chat-api/0.2/send-message/"

payload = "bing_u_cookie=%3CREQUIRED%3E&question=Give%20me%203%20examples%20of%20how%20I%20can%20use%20you."
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "ef9f388820msh8a6df62e5f78f65p120aadjsn53c802623fd8",
	"X-RapidAPI-Host": "chatgpt-4-bing-ai-chat-api.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)