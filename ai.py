import os
from groq import Groq

class AI:
    def __init__(self, statement, mode='chat'):
        self.client = Groq(api_key='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')
        self.result = self.detct_mode(statement, mode, client=self.client)

    def detct_mode(self, statement, mode, client):
        if mode == 'chat':
            result = self.chatai(statement, client)
            return result

    def chatai(self, statement, client):
        try:
            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": "short answer pls(one line), " + statement + ', thanks'}],
                model="llama3-8b-8192"
            )
            result = f'AI: {chat_completion.choices[0].message.content}'
            return result
        except Exception as e:
            return f"Error: {e}"