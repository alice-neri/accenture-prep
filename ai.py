import urllib.request
import urllib.parse

while True:
    prompt = input("You: ")

    if prompt == "exit":
        break

    safe_prompt = urllib.parse.quote(prompt)
    url = f"https://text.pollinations.ai/{safe_prompt}"

    with urllib.request.urlopen(url) as response:
        print("AI:", response.read().decode("utf-8"))