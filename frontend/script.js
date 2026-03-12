const API_BASE = "http://127.0.0.1:8000";

async function loadAISignals() {
    const res = await fetch(`${API_BASE}/ai_signals`);
    const signals = await res.json();
    const container = document.getElementById("ai-signals");
    container.innerHTML = "";
    signals.forEach(sig => {
        const div = document.createElement("div");
        div.innerHTML = `
            <h3>${sig.pair} - ${sig.timeframe}</h3>
            <p>Вероятность: ${sig.probability}%</p>
            <p>Статус: ${sig.status}</p>
            <p>${sig.description}</p>
        `;
        container.appendChild(div);
    });
}

async function loadTelegramPost() {
    const res = await fetch(`${API_BASE}/telegram_post`);
    const data = await res.json();
    const container = document.getElementById("telegram-post");
    container.innerHTML = `<p>${data.post}</p>`;
}

// Обновляем каждые 5 секунд
setInterval(loadAISignals, 5000);
setInterval(loadTelegramPost, 5000);

// Первоначальная загрузка
loadAISignals();
loadTelegramPost();
