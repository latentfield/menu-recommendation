from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>메뉴 추천 시스템</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 600px;
                margin: 50px auto;
                padding: 20px;
                background-color: #f5f5f5;
            }
            .container {
                background-color: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }
            h1 {
                color: #333;
                text-align: center;
            }
            .question {
                margin: 20px 0;
            }
            label {
                display: block;
                margin: 10px 0 5px 0;
                font-weight: bold;
            }
            select, input {
                width: 100%;
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 5px;
                font-size: 14px;
            }
            button {
                width: 100%;
                padding: 15px;
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                font-size: 16px;
                cursor: pointer;
                margin-top: 20px;
            }
            button:hover {
                background-color: #45a049;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🍽️ 오늘 뭐 먹지?</h1>
            
            <div class="question">
                <label>음식 종류를 선택하세요:</label>
                <select id="food-type">
                    <option value="">선택해주세요</option>
                    <option value="korean">한식</option>
                    <option value="chinese">중식</option>
                    <option value="japanese">일식</option>
                    <option value="western">양식</option>
                </select>
            </div>
            
            <div class="question">
                <label>주차가 필요하신가요?</label>
                <select id="parking">
                    <option value="">선택해주세요</option>
                    <option value="yes">네, 필요해요</option>
                    <option value="no">아니요, 괜찮아요</option>
                </select>
            </div>
            
            <div class="question">
                <label>예산은 얼마인가요? (원)</label>
                <input type="number" id="budget" placeholder="예: 10000">
            </div>
            
            <button onclick="recommend()">메뉴 추천받기!</button>
            
            <div id="result" style="margin-top: 20px; padding: 20px; background-color: #e8f5e9; border-radius: 5px; display: none;">
                <h3>추천 결과</h3>
                <p id="recommendation"></p>
            </div>
        </div>
        
        <script>
            function recommend() {
                var foodType = document.getElementById('food-type').value;
                var parking = document.getElementById('parking').value;
                var budget = document.getElementById('budget').value;
                
                var result = document.getElementById('result');
                var recommendation = document.getElementById('recommendation');
                
                if (!foodType || !parking || !budget) {
                    alert('모든 항목을 선택해주세요!');
                    return;
                }
                
                // 간단한 추천 로직 (나중에 개선할 예정)
                var message = foodType + ' 음식을 원하시고, ';
                message += '주차는 ' + (parking === 'yes' ? '필요하시고' : '필요없으시고');
                message += ', 예산은 ' + budget + '원이시군요!<br><br>';
                message += '🎯 추천: 현재는 테스트 버전입니다. 곧 실제 식당을 추천해드릴게요!';
                
                recommendation.innerHTML = message;
                result.style.display = 'block';
            }
        </script>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)