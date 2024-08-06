from flask import Flask, render_template, request
import google.generativeai as genai

app = Flask(__name__)

# Configure the generative AI model with your API key
genai.configure(api_key='AIzaSyDCRQ1QC_LMuLiioVUD6aKhckq_CXZ0dIc')
model = genai.GenerativeModel('gemini-pro')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form['feedback']
    prompt = f'''
    you are a sentiment classification mode refer below example and classify feedback into "p" or "n" category. return only category in output
    feedback: what a lovely product
    sentiment: p
    feedback: it is totally time wasting product
    sentiment: n
    feedback: {user_input}
    sentiment
    '''
    response = model.generate_content(prompt, generation_config={"max_output_tokens": 100, "temperature": 0.2})
    sentiment = response.text.strip()
    return render_template('result.html', sentiment=sentiment, feedback=user_input)

if __name__ == '__main__':
    app.run(debug=True)