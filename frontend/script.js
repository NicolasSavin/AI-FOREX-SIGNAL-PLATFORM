const API_BASE = "http://127.0.0.1:8000"; // заменим на Railway позже

let totalSignals = 0;
let inProfit = 0;

async function loadAISignals() {
    const res = await fetch(`${API_BASE}/ai_signals`);
    const signals = await res.json();
    const container = document.getElementById("ai-signals");
    container.innerHTML = "";

    totalSignals = signals.length;
    inProfit = signals.filter(s => s.in_profit).length;

    signals.forEach(sig => {
        const div = document.createElement("div");
        div.className = "signal-card";
        div.innerHTML = `
            <h3>${sig.pair} - ${sig.timeframe}</h3>
            <p>Вероятность: ${sig.probability}%</p>
            <p>Статус: ${sig.status}</p>
            <p>В профите: ${sig.in_profit ? "Да" : "Нет"}</p>
            <p>${sig.description}</p>
        `;
        container.appendChild(div);

        // Анимация: мигаем, если сигнал активный
        if(sig.status === "active") {
            div.style.animation = "pulse 1s infinite";
        }
    });

    document.getElementById("total-signals").innerText = totalSignals;
    document.getElementById("in-profit").innerText = inProfit;
}

async function loadTelegramPosts() {
    const res = await fetch(`${API_BASE}/telegram_post`);
    const data = await res.json();
    const container = document.getElementById("telegram-posts");

    // Добавляем новый пост сверху
    const postDiv = document.createElement("div");
    postDiv.className = "telegram-post";
    postDiv.innerText = data.post;
    container.prepend(postDiv);

    // Удаляем старые, если больше 1
    while(container.children.length > 1) {
        container.removeChild(container.lastChild);
    }
}

// Обновляем каждые 5 секунд
setInterval(loadAISignals, 5000);
setInterval(loadTelegramPosts, 7000);

loadAISignals();
loadTelegramPosts();
