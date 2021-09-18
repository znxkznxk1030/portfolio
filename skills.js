// ====== Skills ====== //

const t2 = gsap
    .timeline({
        scrollTrigger: {
            trigger: '.skills',
            start: '30% center',
            end: 'center center',
            // markers: true,
        },
    })

t2.from('.skills__data', { opacity: 0, "margin-top": "-50px", transition: "all .2s ease-in", stagger: 0.15 });