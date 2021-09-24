const elCanvasDojo = document.getElementById('work-canvasdojo')

elCanvasDojo.addEventListener('click', e => {
    // e.preventDefault();
    window.location.href = 'https://marketplace.visualstudio.com/items?itemName=ArthurKim.canvas-dojo'
})

const elGreatAward = document.getElementById('work-greataward')

elGreatAward.addEventListener('click', e => {
    window.location.href = 'https://znxkznxk1030.github.io/great-award/'
})

const elRapidCello = document.getElementById('work-rapidcello')

elRapidCello.addEventListener('click', e => {
    window.location.href = 'https://www.cellorapid.com/cello/web/login.html'
})


const t2 = gsap
    .timeline({
        scrollTrigger: {
            trigger: '.works',
            start: 'top center',
            end: 'center center',
        },
    })

t2.from('.works__background', {transform: "scale(1.5)"})