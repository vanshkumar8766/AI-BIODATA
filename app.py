from flask import Flask, request, jsonify, render_template
import wikipedia

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    name = data.get("name")
    question = data.get("question")

    try:
        summary = wikipedia.summary(name, sentences=3)
        # Basic "AI-like" answer generation
        answer = f"{name} के बारे में जानकारी:\n{summary}\n\nसवाल: {question}\nजवाब: उपलब्ध जानकारी के आधार पर, {name} शायद ऐसा कर सकते हैं क्योंकि {summary.split('.')[0]}."
    except:
        answer = "इस नाम के लिए जानकारी नहीं मिली।"

    return jsonify({"answer": answer})
if __name__ == "__main__":
    app.run(debug=True)