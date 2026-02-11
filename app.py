from flask import Flask, request, jsonify

# 식당 데이터 (나중에 DB로 이동 예정)
restaurants = [
    {
        'name': '김밥천국',
        'type': 'snack',
        'parking': False,
        'price': 5000,
        'spicy': 'mild'
    },
    {
        'name': '청기와 한정식',
        'type': 'korean',
        'parking': True,
        'price': 15000,
        'spicy': 'medium'
    },
    {
        'name': '짬뽕지존',
        'type': 'chinese',
        'parking': False,
        'price': 9000,
        'spicy': 'hot'
    },
    {
        'name': '스시로',
        'type': 'japanese',
        'parking': True,
        'price': 18000,
        'spicy': 'mild'
    },
    {
        'name': '파스타하우스',
        'type': 'western',
        'parking': True,
        'price': 13000,
        'spicy': 'mild'
    }
]

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
                    <option value="snack">분식</option>
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
                <label>맵기는 어느 정도로 할까요?</label>
                <select id="spicy-level">
                    <option value="mild">안 매워요</option>
                    <option value="medium">보통</option>
                    <option value="hot">매워요</option>
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
        var spicyLevel = document.getElementById('spicy-level').value;
        
        if (!foodType || !parking || !budget || !spicyLevel) {
            alert('모든 항목을 선택해주세요!');
            return;
        }
        
        // Flask 서버로 데이터 전송
        fetch('/recommend', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                foodType: foodType,
                parking: parking,
                budget: parseInt(budget),
                spicyLevel: spicyLevel
            })
        })
        .then(response => response.json())
        .then(data => {
            var result = document.getElementById('result');
            var recommendation = document.getElementById('recommendation');
            
            recommendation.innerHTML = data.message;
            result.style.display = 'block';
        });
    }
</script>
    </body>
    </html>
    """

@app.route('/recommend', methods=['POST'])
def recommend():
    # 사용자 입력 받기
    data = request.get_json()
    food_type = data.get('foodType')
    parking_needed = data.get('parking') == 'yes'
    budget = int(data.get('budget'))
    spicy_level = data.get('spicyLevel')
    
    # 조건에 맞는 식당 필터링
    matched_restaurants = []
    
    for restaurant in restaurants:
        # TODO: 여기에 필터링 조건 작성
        if restaurant['type'] != food_type:
            continue
        
        if parking_needed and not restaurant['parking']:
            continue

        if restaurant['price'] > budget:
            continue

        if restaurant['spicy'] != spicy_level:
            continue
        
        matched_restaurants.append(restaurant)
    
    # 결과 반환
    if matched_restaurants:
        result_text = '<h3>🎯 추천 식당</h3>'
        for r in matched_restaurants:
            result_text += f'<p><strong>{r["name"]}</strong> - {r["price"]}원</p>'
        
        return jsonify({
            'success': True,
            'message': result_text
        })
    else:
        return jsonify({
            'success': False,
            'message': '조건에 맞는 식당이 없습니다. 😢'
        })


if __name__ == '__main__':
    app.run(debug=True)