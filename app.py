from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


# Define your OpenAI API credentials

api_key = "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"
headers = {'Content-Type': 'application/json',
           'Authorization': f'Bearer {api_key}'}


# Define a function to create the OpenAI API request payload

def payload(prompt):
    return {
        'model': 'image-alpha-001',
        'prompt': prompt,
        'num_images': 1,
        'size': '256x256',
        'response_format': 'url'
    }


# Define the index route that renders the form template

@app.route('/')
def index():
    return render_template('index.html')


# Define the result route that processes the form data and displays the generated image

@app.route('/result', methods=['POST'])
def result():
    description = request.form['description']
    response = requests.post('https://api.openai.com/v1/images/generations',
                             headers=headers, json=payload(description))
    response.raise_for_status()
    response_data = json.loads(response.text)
    image_url = response_data['data'][0]['url']
    return image_url


if __name__ == '__main__':
    app.run()
