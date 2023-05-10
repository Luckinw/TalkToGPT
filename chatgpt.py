import requests


def talkgpt(content):
    url = "https://api.openai.com/v1/chat/completions"

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": f"{content}"}],
        "temperature": 1.0,
        "top_p": 1.0,
        "n": 1,
        "stream": False,
        "presence_penalty": 0,
        "frequency_penalty": 0,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {'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'}"
    }

    response = requests.post(url, headers=headers, json=payload, stream=False)
    return response.json()['choices'][0]['message']['content']
