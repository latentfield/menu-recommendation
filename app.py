from flask import  Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1> 메뉴 추천 시스템</h1>
    <p>프로젝트가 시작되었습니다!</p>
    """

if __name__ == '__main__':
    app.run(debug=True)
