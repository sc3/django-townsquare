//File for added JavaScript functions

/*Attempting to write a function that will populate a canvas object with info from
volunteer records*/

(function($)
{
	
	$.fn.badge=function()
	{
		
		var c=$("#badgearea");
		var ctx=c.getContext("2d");
		ctx.font="30px Arial";
		ctx.fillText("Hello World", 10, 50);

	};
	
	return this;
	
})(jQuery);


function badgewrite()
{

	var c=document.getElementById("badgearea2");
	var ctx=c.getContext("2d");
	ctx.font="30px Arial";
	ctx.fillText("Hello World", 10, 50);

}

