import requests
from bs4 import BeautifulSoup
import json

res = requests.get('https://stackoverflow.com/questions')

soup = BeautifulSoup(res.text, "html.parser")

questions_data = {
    "questions":[]
}

questions = soup.select('.question-summary')

for que in questions:
    q = que.select_one('.question-hyperlink').getText()
    vote = que.select_one('.vote-count-post').getText()
    views = que.select_one('.views')['title']
    questions_data['questions'].append({
        "question": q,
        "vote": vote, 
        "views": views,
    })

json_data = json.dumps(questions_data)
print(json_data)