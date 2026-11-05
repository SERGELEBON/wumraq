$("body").prepend('<div class="cursor"></div>');

$(document)
  .mousemove(function(e) {
  $('.cursor')
    .eq(0)
    .css({
    "left": e.pageX,
    "top": e.pageY - $(window).scrollTop()
  });
});

$("a").mouseenter(function(){
  $('.cursor').addClass('hover');
})
.mouseleave(function(){
  $('.cursor').removeClass('hover');
});