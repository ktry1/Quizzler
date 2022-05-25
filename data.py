import requests, html
class Question:
    def __init__(self):
        self.text=None
        self.answer=None

    def fetch_question(self):
        response = requests.get(url="https://opentdb.com/api.php?amount=1&category=27&type=boolean")
        question=html.unescape(response.json()["results"][0]["question"])
        answer =response.json()["results"][0]["correct_answer"]
        self.text=question
        self.answer=answer

question=Question()
