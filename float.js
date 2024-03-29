const elHome = document.getElementById('home')
const elProgress = document.getElementById('home-progress')
let elProgressText = document.getElementById('home-progress-text')

const getScrollPercentage = () => {
  console.log(elHome.scrollHeight, window.scrollY);
  return (( window.scrollY ) / (elHome.scrollHeight) * 100)
}

const updateScollProgress = () => {
  const percentage = getScrollPercentage() >= 100 ? 100 : getScrollPercentage()
  elProgress.style.height = `${percentage}%`
  elProgressText.innerText = `${Math.ceil(percentage)}%`
}

window.addEventListener('scroll', () => {
  updateScollProgress();
})