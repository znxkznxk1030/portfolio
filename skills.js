// ====== Skills ====== //

const t3 = gsap
    .timeline({
        scrollTrigger: {
            trigger: '.skills',
            start: 'top center',
            end: 'center center',
            // markers: true,
        },
    })

t3.from('.skills__data', { opacity: 0, "margin-top": "-50px", transition: "all .2s ease-in", stagger: 0.15 }, 'skill_start');
t3.from('.skills__background', {transform: "scale(2)"}, 'skill_start')