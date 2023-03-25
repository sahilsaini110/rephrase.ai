import requests
import json

# accessing prompt_text
with open('prompt_text.txt') as f:
    prompt_text = f.read()

url = "https://stablediffusionapi.com/api/v3/text2img"

payload = json.dumps({
    "key": "ccrFQTXeJfqopsI6tIypuD8hauilUevAdtsN0DvMXA6JSVkn3EVzZCJXYJ7c",
    "prompt": prompt_text,
    "negative_prompt": "((out of frame)) ((not a person))",
    "width": "512",
    "height": "512",
    "samples": "1",
    "num_inference_steps": "20",
    "safety_checker": "no",
    "enhance_prompt": "yes",
    "seed": None,
    "guidance_scale": 7.5,
    "webhook": None,
    "track_id": None
})
headers = {
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkhNcHdjdFl4YWlRdWg4Y0M0ejN0UCJ9.eyJpc3MiOiJodHRwczovL2F1dGgucmVwaHJhc2UuYWkvIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDc5MzE5NjY0MDQ5NzA4MTMwNjYiLCJhdWQiOlsiaHR0cHM6Ly9kaXkucmVwaHJhc2UuYWkvYXV0aDAiLCJodHRwczovL3JlcGhyYXNlYWktcHJvZC51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjc5NzQ3NzQzLCJleHAiOjE2Nzk4MzQxNDMsImF6cCI6IjNLVTVqdkVxV0pCQ1VLblBYMjZvbmFTUHkzakozMEo0Iiwic2NvcGUiOiJvcGVuaWQgZW1haWwgcHJvZmlsZSByZWFkOnJlcGhyYXNlLmFpIGFsbDpkaXkgcmVhZDpyZXBocmFzZS5haSJ9.LwGcknsaVymqpzCiYcxL4rYDQD9fS7q9PHRURpjA4DAv4qki9SgISglx8jlB_r4L-quTiX_zZjbB4iqYgK-YBZWXIiRJN3gP6I4SL8fGEFlk244G5q0sax6pnKHgLNiV1vIZPWJevGLdJ5SmIFcP1G_5GMD4enRZRyCWElTnz2AB2KdEh7w5sAD8uk-rx97504D8kBJ-fog-fLMm-dEl7QEnbP70zZ-FkrJk2UkQgecQRUFEdXWW5mf8f9BOhvU4wxQZWUvqvljIk4mpl3p93N74NngaBD5BVMG0b0GMkguRA0nRviwdqWYM0DujfWT1s1zRBPmVpeFPjUcYA7fYmg',
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
data = response.json()
print(data)
print(prompt_text)