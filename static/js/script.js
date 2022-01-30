function menu(){
	$(".nav-bar-bottom").toggleClass("menu-open");
}

/*
	OPEN SUB-MENU MOBILE
*/
$(function(){
	$(".sub-menu-head").click(function(e){
		$(e.target).parent().toggleClass("sub-menu-open");
	})
});


/*
	SCROLL TO TOP - ANIMATION + SCROLL
*/
$(window).scroll(function(){
	var pos = window.scrollY;
	if(pos > 50){
		$(".scroll_to_top").show();
	}else{
		$(".scroll_to_top").hide();		
	}
});

$(function(){
	$(".scroll_to_top").click(function(){
		$("html, body").animate({scrollTop:0}, 500);
	});
});