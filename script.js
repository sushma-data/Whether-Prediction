document.getElementById("weatherForm").addEventListener("submit", function (e) {
    e.preventDefault();

    // Correct way to get input values
    let temp = document.getElementById("temperature").value;
    let hum = document.getElementById("humidity").value;
    let wind = document.getElementById("wind").value;
    let pressure = document.getElementById("pressure").value;

    let prediction = "";

    if (hum > 70 && temp < 30) {
        prediction = "🌧️ Rainy Weather";
    } else if (temp > 30) {
        prediction = "☀️ Sunny Weather";
    } else {
        prediction = "☁️ Cloudy Weather";
    }

    document.getElementById("result").innerHTML =
        "Predicted Weather:<br>" + prediction;
});
