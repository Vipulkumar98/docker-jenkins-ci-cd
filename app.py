from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>DevOps CI/CD Project</title>
        </head>
        <body style="font-family: Arial; text-align: center; margin-top: 100px;">
            <h1>DevOps CI/CD Pipeline Project</h1>
            <p>Application deployed using Docker, Jenkins, GitHub, and Docker Hub.</p>
            <p><b>Version 2.0 - Updated via Jenkins CI/CD Pipeline</b></p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
