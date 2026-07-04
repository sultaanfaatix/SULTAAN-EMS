setTimeout(() => {
  document.querySelectorAll(".toast").forEach((toast) => {
    toast.style.opacity = "0";
    toast.style.transform = "translateY(-8px)";
    setTimeout(() => toast.remove(), 250);
  });
}, 4500);

if (window.APP_TRANSLATIONS) {
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  const skipTags = new Set(["SCRIPT", "STYLE", "TEXTAREA"]);
  const nodes = [];
  while (walker.nextNode()) {
    const node = walker.currentNode;
    if (!node.parentElement || skipTags.has(node.parentElement.tagName)) continue;
    nodes.push(node);
  }
  nodes.forEach((node) => {
    const original = node.nodeValue.trim();
    if (original && window.APP_TRANSLATIONS[original]) {
      node.nodeValue = node.nodeValue.replace(original, window.APP_TRANSLATIONS[original]);
    }
  });
}

const resultPanel = document.querySelector(".premium-result");
if (resultPanel) {
  const status = resultPanel.dataset.resultStatus;
  const isPass = status === "Gudbay";
  const burst = document.createElement("div");
  burst.className = `confetti-burst ${isPass ? "pass" : "support"}`;
  for (let i = 0; i < 34; i += 1) {
    const piece = document.createElement("span");
    piece.style.setProperty("--x", `${Math.random() * 100}%`);
    piece.style.setProperty("--d", `${Math.random() * 1.8}s`);
    piece.style.setProperty("--r", `${Math.random() * 360}deg`);
    burst.appendChild(piece);
  }
  document.body.appendChild(burst);
  setTimeout(() => burst.remove(), 10000);
}
