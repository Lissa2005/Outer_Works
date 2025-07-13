function loadContent() {
  fetch('content_ST1.html')
    .then(response => {
      if (!response.ok) {
        throw new Error('Failed to load content_ST1.html');
      }
      return response.text();
    })
    .then(html => {
      const content = document.getElementById('content');
      if (content) {
        content.innerHTML = html;
      }
    })
    .catch(error => {
      console.error('Error:', error);
    });
}

function hideSplash(callback) {
  const splash = document.getElementById('splash');
  if (splash) {
    splash.style.opacity = '0';
    setTimeout(() => {
      splash.style.display = 'none';
      const content = document.getElementById('content');
      if (content) {
        content.style.display = 'block';
        loadContent();
      }
      document.body.style.overflow = 'auto';
      // If a callback is provided (e.g., redirect), call it now
      if (callback) callback();
    }, 1000);
  }
}

window.onload = () => {
  setTimeout(() => {
    hideSplash();
  }, 4000);
};

document.addEventListener("DOMContentLoaded", () => {
  const btn = document.getElementById("pageEditorBtn");
  if (btn) {
    btn.addEventListener("click", () => {
      hideSplash(() => {
        window.location.href = 'pageEditor_ST1.HTML';
      });
    });
  }
});
