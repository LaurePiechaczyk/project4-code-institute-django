console.log("fffffffffff")

$("#english-check-box").click(function(){
    if($('#english-check-box').is(":checked"))
        $(".words-container .english-noun").css("opacity", "1")
    else 
        $(".words-container .english-noun").css("opacity", "0")
});

$("#plural-check-box").click(function(){
    if($('#plural-check-box').is(":checked"))
        $(".words-container .plural-noun").css("opacity", "1")
    else 
        $(".words-container .plural-noun").css("opacity", "0")
});

/*
$("#german-check-box").click(function(){
    $(".words-container p:nth-child(3)").css("opacity", "1");
}); */


