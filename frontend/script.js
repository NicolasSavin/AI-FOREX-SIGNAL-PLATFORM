fetch("https://ai-forex-signal-platform.onrender.com/ai_signals")
  .then(res => res.json())
  .then(signals => {
    const container = document.getElementById("signals-container");
    signals.forEach((sig, index) => {
      const card = document.createElement("div");
      card.className = "signal-card fade-in";
      card.style.animationDelay = `${index * 0.05}s`; // небольшая задержка анимации
      card.innerHTML = `
        <h3>${sig.pair} (${sig.timeframe})</h3>
        <p>Вероятность: ${sig.probability}%</p>
        <p>${sig.status === "active" ? "🟢 Активный" : "🔴 Неактивный"}</p>
        <p>${sig.description}</p>
        <img src="${sig.image_url}" />
      `;
      container.appendChild(card);
    });
  });
