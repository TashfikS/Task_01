from flask import Flask, request, jsonify
from GPT3_prompt import OpenAIClient

app = Flask(__name__)

@app.route('/recommend-fruits', methods=['POST'])
def recommend_fruits_api():
    try:
        data = request.get_json()
        answers = {
            "party_on_weekends": data["party_on_weekends"],
            "flavor": data["flavor"],
            "texture": data["texture"],
            "price_range": data["price_range"]
        }


        api_key = "OPENAI_API_KEY"
        client = OpenAIClient(api_key)
        recommendations = client.generate_fruit_recommendations(data["party_on_weekends"], 
                                                                data["flavor"], data["texture"], 
                                                                data["price_range"])

        # return jsonify({"recommended_fruits": recommended_fruits})
        return jsonify({"recommended_fruits": recommendations.content})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
