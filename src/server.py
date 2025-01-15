from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO
import requests

app = Flask(
    __name__, template_folder="html", static_folder="../static"
)
socketio = SocketIO(app)

# Fetch coins from Binance
@app.route('/api/recent-trades')
def recent_trades():
    url = "https://api.binance.com/api/v3/ticker/24hr"
    response = requests.get(url)
    data = response.json()

    # Filter profitable coins
    profitable_coins = [
        {
            "symbol": coin["symbol"],
            "priceChangePercent": float(coin["priceChangePercent"]),
            "lastPrice": float(coin["lastPrice"]),
            "volume": float(coin["volume"]),
        }
        for coin in data if float(coin["priceChangePercent"]) > 0
    ]
    return jsonify(sorted(profitable_coins, key=lambda x: x["priceChangePercent"], reverse=True))

# WebSocket for real-time updates
@socketio.on('connect')
def handle_connect():
    print("Client connected!")

@app.route('/')
def home():
    return render_template('workspace.html')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
