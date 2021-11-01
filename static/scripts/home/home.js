console.log("fffffffffff")


// When english is checked --> display english
$("#english-check-box").click(function(){
    if($('#english-check-box').is(":checked"))
        $(".words-container .english-noun").css("opacity", "1")
    else 
        $(".words-container .english-noun").css("opacity", "0")
});

// When german is checked --> display german
$("#plural-check-box").click(function(){
    if($('#plural-check-box').is(":checked"))
        $(".words-container .plural-noun").css("opacity", "1")
    else 
        $(".words-container .plural-noun").css("opacity", "0")
});

// Change color on click
//feminine
$(document).ready(function() {
    var pathname = window.location.pathname;
    if (pathname.indexOf('feminine') > -1) {
        $('.words-container').addClass('die-color');
    }
 });
 //masculine
 $(document).ready(function() {
    var pathname = window.location.pathname;
    if (pathname.indexOf('masculine') > -1) {
        $('.words-container').addClass('der-color');
    }
 });



/*
$("#german-check-box").click(function(){
    $(".words-container p:nth-child(3)").css("opacity", "1");
}); */


