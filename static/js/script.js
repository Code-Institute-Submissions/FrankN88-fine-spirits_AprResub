function menu(){
	$(".nav-bar-bottom").toggleClass("menu-open");
}

$(function(){
	$(".quantity_minus").click(function(){
		var quantity = parseInt($("[name='quantity']").val())-1;
		if(quantity<1) return;
		$("[name='quantity']").val(quantity);
	});

	$(".quantity_plus").click(function(){
		var quantity = parseInt($("[name='quantity']").val())+1;
		if(quantity>99) return;
		$("[name='quantity']").val(quantity);
	});
});