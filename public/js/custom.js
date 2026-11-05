(function($, window, undefined) {
	"use strict";
	jQuery(document).ready(function ($) {
		// Animation on scroll
		new WOW().init();

		// revolution slider
		$('.fullwidthbanner').revolution({
        	delay:6000,
        	startwidth:1170,
        	startheight:1100,
        	onHoverStop: "on",
        	hideTimerBar: "off",
            thumbWidth: 100,
            thumbHeight: 50,
            thumbAmount: 3,
            hideThumbs: 200,
            navigationType: "bullet",
            navigationArrows: "verticalcentered",
            navigationStyle: "preview4",
            touchenabled: "on",
            navOffsetHorizontal: 0,
            navOffsetVertical: 20,
            stopAtSlide: -1,
            stopAfterLoops: -1,
            hideCaptionAtLimit: 0,
            hideAllCaptionAtLilmit: 0,
            hideSliderAtLimit: 0,
            hideThumbsOnMobile:"on",
         	hideNavDelayOnMobile:1500,
         	hideBulletsOnMobile:"on",
         	hideArrowsOnMobile:"on",
         	hideThumbsUnderResoluition:0,
            fullWidth: "on",
            shadow: 0
      	});
	});
})(jQuery, window);
