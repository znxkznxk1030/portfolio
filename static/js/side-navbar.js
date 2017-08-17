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
	if($('.sidenav').hasClass('open-nav')){
		$('#left-arrow').css("display", "block");
		$('#right-arrow').css("display", "none");	
	}else{
		$('#left-arrow').css("display", "none");
		$('#right-arrow').css("display", "block");
	}
    }
);

$(document).ready(function(){
});

function openPosts(category){
	category.style.display="block";
}

function closePosts(category){
	category.style.display="none";
}
