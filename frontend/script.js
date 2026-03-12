// Замените на свой публичный URL Render после деплоя
const API_BASE = "https://ai-forex-signal-platform.onrender.com";

async function loadSignals() {
    const response = await fetch(`${API_BASE}/ai_signals`);
    const data = await response.json();
    document.getElementById("signals").innerHTML = JSON.stringify(data, null, 2);
}

loadSignals();
