from flask import Flask, request, jsonify
import redis
import os

app = Flask(__name__)

# התחברות ל-Redis (Railway מספקת את משתנה הסביבה REDIS_URL אוטומטית!)
REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379')
r = redis.from_url(REDIS_URL, decode_responses=True)

@app.route('/track', methods=['POST'])
def track():
    data = request.json
    city = data.get('city')

    if not city:
        return jsonify({"error": "City is required"}), 400

    try:
        # פקודה פשוטה ב-Redis שמקדמת את המונה של העיר ב-1 (או מייצרת אותו אם לא קיים)
        r.hincrby("weather_history", city, 1)
        return jsonify({"status": "tracked", "city": city}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/stats', methods=['GET'])
def get_stats():
    try:
        # שליפת כל המונים מ-Redis
        stats = r.hgetall("weather_history")
        # המרה של הערכים למספרים שלמים
        formatted_stats = {k: int(v) for k, v in stats.items()}
        return jsonify(formatted_stats)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5002))
    app.run(host='0.0.0.0', port=port)