const coinDisplay = document.getElementById('coin-display');

// Fetch and display real-time data for coins
function fetchCoinData() {
    fetch('/api/recent-trades') // Updated API endpoint for filtered trades
        .then(response => response.json())
        .then(data => {
            coinDisplay.innerHTML = ''; // Clear previous data
            data.forEach(coin => {
                const coinDiv = document.createElement('div');
                coinDiv.className = 'coin';
                coinDiv.innerHTML = `
                    <h3>${coin.symbol}</h3>
                    <p>Price Change: ${coin.priceChangePercent}%</p>
                    <p>Volume: ${coin.volume}</p>
                    <p>Last Price: ${coin.lastPrice}</p>
                `;
                coinDisplay.appendChild(coinDiv);
            });
        })
        .catch(error => console.error('Error fetching coin data:', error));
}

// Real-time update using WebSocket for minimal latency
const socket = new WebSocket('ws://127.0.0.1:5000/ws/recent-trades');

// On receiving data from the WebSocket
socket.onmessage = (event) => {
    const data = JSON.parse(event.data);
    coinDisplay.innerHTML = ''; // Clear previous data
    data.forEach(coin => {
        const coinDiv = document.createElement('div');
        coinDiv.className = 'coin';
        coinDiv.innerHTML = `
            <h3>${coin.symbol}</h3>
            <p>Price Change: ${coin.priceChangePercent}%</p>
            <p>Volume: ${coin.volume}</p>
            <p>Last Price: ${coin.lastPrice}</p>
        `;
        coinDisplay.appendChild(coinDiv);
    });
};

socket.onerror = (error) => console.error('WebSocket error:', error);
