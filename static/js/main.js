// ===== THEME MANAGEMENT =====
(function () {
  const themeToggle = document.getElementById("themeToggle");

  if (themeToggle) {
    const body = document.body;
    const icon = themeToggle.querySelector("i");

    // Load saved theme
    const savedTheme = localStorage.getItem("theme");
    if (savedTheme === "dark") {
      body.classList.add("dark-theme");
      if (icon) icon.className = "fas fa-sun";
    }

    // Toggle theme on click
    themeToggle.addEventListener("click", function () {
      body.classList.toggle("dark-theme");

      if (body.classList.contains("dark-theme")) {
        if (icon) icon.className = "fas fa-sun";
        localStorage.setItem("theme", "dark");
      } else {
        if (icon) icon.className = "fas fa-moon";
        localStorage.setItem("theme", "light");
      }
    });
  }
})();

// ===== GALLERY LIGHTBOX =====
(function () {
  const lightbox = document.getElementById("lightbox");
  if (!lightbox) return;

  let currentIndex = 0;
  let visibleImages = [];
  const lgImg = document.getElementById("largeImg");
  const caption = document.getElementById("caption");
  const closeBtn = document.querySelector(".close-lightbox");
  const prevBtn = document.querySelector(".prev-btn");
  const nextBtn = document.querySelector(".next-btn");

  // Add click handlers to gallery images
  function setupGalleryClick() {
    document.querySelectorAll(".photo-card").forEach((card) => {
      card.addEventListener("click", function () {
        visibleImages = Array.from(
          document.querySelectorAll(".photo-card:not(.hidden)"),
        );
        currentIndex = visibleImages.indexOf(this);

        updateLightboxContent(this);
        lightbox.classList.add("active");
        document.body.style.overflow = "hidden";
      });
    });
  }

  function updateLightboxContent(card) {
    const img = card.querySelector("img");
    const title = card.querySelector(".photo-info");

    if (img) lgImg.src = img.src;
    if (title) caption.innerText = title.innerText;
  }

  function updateLightboxByIndex() {
    if (!visibleImages.length) return;
    const card = visibleImages[currentIndex];
    const img = card.querySelector("img");
    const title = card.querySelector(".photo-info");

    if (img) lgImg.src = img.src;
    if (title) caption.innerText = title.innerText;
  }

  // Close lightbox
  if (closeBtn) {
    closeBtn.addEventListener("click", function () {
      lightbox.classList.remove("active");
      document.body.style.overflow = "auto";
    });
  }

  // Navigation
  if (prevBtn) {
    prevBtn.addEventListener("click", function () {
      if (visibleImages.length) {
        currentIndex--;
        if (currentIndex < 0) currentIndex = visibleImages.length - 1;
        updateLightboxByIndex();
      }
    });
  }

  if (nextBtn) {
    nextBtn.addEventListener("click", function () {
      if (visibleImages.length) {
        currentIndex++;
        if (currentIndex >= visibleImages.length) currentIndex = 0;
        updateLightboxByIndex();
      }
    });
  }

  // Click outside to close
  lightbox.addEventListener("click", function (e) {
    if (e.target === lightbox) {
      lightbox.classList.remove("active");
      document.body.style.overflow = "auto";
    }
  });

  // Keyboard navigation
  document.addEventListener("keydown", function (e) {
    if (!lightbox.classList.contains("active")) return;

    if (e.key === "Escape") {
      lightbox.classList.remove("active");
      document.body.style.overflow = "auto";
    } else if (e.key === "ArrowRight") {
      if (nextBtn) nextBtn.click();
    } else if (e.key === "ArrowLeft") {
      if (prevBtn) prevBtn.click();
    }
  });

  // Initialize gallery click handlers
  setupGalleryClick();
})();

// ===== GALLERY FILTER =====
window.filterGallery = function (category, element) {
  // Update active tab
  document
    .querySelectorAll(".tab")
    .forEach((t) => t.classList.remove("active"));
  if (element) element.classList.add("active");

  // Filter photos
  document.querySelectorAll(".photo-card").forEach((card) => {
    if (category === "all" || card.dataset.cat === category) {
      card.classList.remove("hidden");
    } else {
      card.classList.add("hidden");
    }
  });
};

// ===== LAZY LOADING IMAGE DETECTION =====
(function () {
  // Check if browser supports lazy loading
  if ("loading" in HTMLImageElement.prototype) {
    console.log("Browser supports native lazy loading");

    // Native lazy loading is supported, just mark images as loaded when they load
    const images = document.querySelectorAll(".img-wrapper img");
    images.forEach((img) => {
      if (img.complete) {
        img.classList.add("loaded");
      } else {
        img.addEventListener("load", function () {
          this.classList.add("loaded");
        });
      }
    });
  } else {
    // Fallback for older browsers - use Intersection Observer
    console.log("Using Intersection Observer fallback");

    const imageObserver = new IntersectionObserver(
      (entries, observer) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            const img = entry.target;

            // If image has data-src (for more advanced lazy loading)
            if (img.dataset.src && img.src !== img.dataset.src) {
              img.src = img.dataset.src;
            }

            img.classList.add("loaded");
            imageObserver.unobserve(img);
          }
        });
      },
      {
        rootMargin: "50px", // Start loading when image is 50px from viewport
      },
    );

    document.querySelectorAll(".img-wrapper img").forEach((img) => {
      imageObserver.observe(img);
    });
  }
})();

// contact page
// Add this at the end of your main.js file
document.addEventListener('DOMContentLoaded', function() {
    // Contact form loading effect
    const contactForm = document.getElementById("contactForm");
    const submitBtn = document.getElementById("submitBtn");
    
    if (contactForm && submitBtn) {
        contactForm.addEventListener("submit", function() {
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';
        });
    }
});




// blog share button action
function shareSite(url) {
    if (navigator.share) {
        navigator.share({
            title: "Check out this site 🚀",
            url: url
        });
    } else {
        navigator.clipboard.writeText(url);
        alert("Site link copied 🔥");
    }
}