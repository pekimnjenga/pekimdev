document.addEventListener('DOMContentLoaded', () => {
    const observerOptions = {
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('opacity-100');
                entry.target.classList.remove('opacity-0', 'translate-y-10');
            }
        });
    }, observerOptions);

    // Apply to glass cards
    document.querySelectorAll('.glass-card').forEach(card => {
        card.classList.add('transition-all', 'duration-700', 'opacity-0', 'translate-y-10');
        observer.observe(card);
    });
});

const swiper = new Swiper('.project-carousel', {
    slidesPerView: 1,
    spaceBetween: 30,
    loop: true,
    navigation: {
        nextEl: '.swiper-next',
        prevEl: '.swiper-prev',
    },
    breakpoints: {
        640: { slidesPerView: 2 },
        1024: { slidesPerView: 3 }, // Show exactly 3 cards on desktop as requested
    },
    speed: 800,
    autoplay: {
        delay: 5000,
        disableOnInteraction: false,
    },
});

// Initialize Projects Module Animations
document.addEventListener("DOMContentLoaded", () => {
    AOS.init({
        duration: 1000,
        once: true,
        easing: 'ease-out-cubic'
    });
});

document.addEventListener("DOMContentLoaded", () => {
    const filterButtons = document.querySelectorAll(".filter-btn");
    const projectCards = document.querySelectorAll(".project-card");

    filterButtons.forEach(button => {
        button.addEventListener("click", () => {
            filterButtons.forEach(btn => btn.classList.remove("active-filter"));
            button.classList.add("active-filter");

            const selection = button.getAttribute("data-filter");

            projectCards.forEach(card => {
                const targetCategory = card.getAttribute("data-category");

                if (selection === "all" || selection === targetCategory) {
                    card.style.display = "block";
                    setTimeout(() => {
                        card.style.opacity = "1";
                        card.style.transform = "translateY(0) scale(1)";
                    }, 50);
                } else {
                    card.style.opacity = "0";
                    card.style.transform = "translateY(10px) scale(0.98)";
                    setTimeout(() => {
                        card.style.display = "none";
                    }, 300);
                }
            });

            setTimeout(() => { AOS.refresh(); }, 350);
        });
    });
});


// AUTOMATIC SLIDESHOW LIGHTWEIGHT JAVASCRIPT

document.addEventListener("DOMContentLoaded", function () {
    const track = document.getElementById("testimonial-track");
    if (!track) return;
    const cards = track.children;
    const dotsContainer = document.getElementById("slider-dots");
    if (!dotsContainer) return;

    let currentIndex = 0;
    let cardsPerSlide = window.innerWidth >= 1024 ? 2 : 1;
    const maxSlides = Math.ceil(cards.length / cardsPerSlide);

    // 1. Generate active navigation dots dynamically
    for (let i = 0; i < maxSlides; i++) {
        const dot = document.createElement("button");
        dot.className = i === 0
            ? "h-2 rounded-full transition-all duration-300 w-8 bg-[#39FF14]"
            : "h-2 rounded-full transition-all duration-300 w-2 bg-slate-300";
        dot.setAttribute("aria-label", `Go to slide ${i + 1}`);
        dot.addEventListener("click", () => goToSlide(i));
        dotsContainer.appendChild(dot);
    }

    const dots = dotsContainer.children;

    // 2. Main translation sliding calculation logic
    function goToSlide(index) {
        currentIndex = index;

        // Avoid translating into dead whitespace on last odd slide on desktop
        if (window.innerWidth >= 1024 && currentIndex === maxSlides - 1 && cards.length % 2 !== 0) {
            track.style.transform = `translateX(-${(cards.length - 2) * 50}%)`;
        } else {
            const gapOffset = currentIndex * (window.innerWidth >= 1024 ? 16 : 0);
            track.style.transform = `translateX(calc(-${currentIndex * 100}% - ${gapOffset}px))`;
        }

        // Update dot visual tracking states smoothly
        Array.from(dots).forEach((dot, i) => {
            if (i === currentIndex) {
                dot.classList.replace("w-2", "w-8");
                dot.classList.replace("bg-slate-300", "bg-[#39FF14]");
            } else {
                dot.classList.replace("w-8", "w-2");
                dot.classList.replace("bg-[#39FF14]", "bg-slate-300");
            }
        });
    }

    // 3. Automated running cycle trigger (every 5 seconds)
    let autoSlideInterval = setInterval(() => {
        let nextIndex = currentIndex + 1;
        if (nextIndex >= maxSlides) nextIndex = 0;
        goToSlide(nextIndex);
    }, 5000);

    // 4. Recalibrate on desktop <-> mobile changes
    window.addEventListener("resize", () => {
        const updatedCardsPerSlide = window.innerWidth >= 1024 ? 2 : 1;
        if (updatedCardsPerSlide !== cardsPerSlide) {
            location.reload();
        }
    });
});

