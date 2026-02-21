from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key="TU_API_KEY")

@app.route("/generar", methods=["POST"])
def generar():
    prompt = request.json["prompt"]

    img = client.images.generate(
        model="gpt-image-1",
        prompt=prompt
    )

    return jsonify({"url": img.data[0].url})

app.run(host="0.0.0.0", port=10000)
