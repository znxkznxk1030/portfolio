function openSideBar(){
    document.getElementById("sidebar").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
}

function closeSideBar(){
    document.getElementById("sidebar").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
}

btn=document.querySelector('.logo-menu');
btn.addEventListener('click', function(){
        $('.sidenav').toggleClass('open-nav');
        $('#main').toggleClass('open');
    }
);

$(document).ready(function(){
        $('.sidenav').toggleClass('open-nav');
        $('#main').toggleClass('open');
});

function openPosts(category){
	category.style.display="block";
}

function closePosts(category){
	category.style.display="none";
}
