from flask import Flask, request

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form.to_dict()
    html = "<h2>Form submitted successfully!</h2><ul>"
    for k, v in data.items():
        html += f"<li><strong>{k.replace('-', ' ')}:</strong> {v}</li>"
    html += "</ul>"
    return html

if __name__ == '__main__':
    app.run(debug=True)