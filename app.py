from dotenv import load_dotenv
from ice_breaker import ice_breaker

from flask import Flask, render_template, request, jsonify

load_dotenv()

app = Flask(__name__)


@app.route("/")
def index():
   return render_template("index.html")

@app.route("/ice_breaker", methods=["POST"])
def ice_breaker_endpoint():
    data = request.get_json()
    name = data.get("name")
    technology = data.get("technology")
    company = data.get("company")

    if not name or not technology or not company:
        return jsonify({"error": "Name, technology, and company are required"}), 400

    try:
        summary, photo_url = ice_breaker(name, technology, company)
        return jsonify({"summary": summary.to_dict(), "photo_url": photo_url}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
    # app.run(debug=True)