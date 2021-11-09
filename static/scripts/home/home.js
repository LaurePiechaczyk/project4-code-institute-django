//console.log("fffffffffff")

//-------------- colors picker

const femininColorPicker = document.getElementById('feminin-color-picker');
const masculinColorPicker = document.getElementById('masculin-color-picker');
const neutralColorPicker = document.getElementById('neutral-color-picker');

// default bg value
var femininBackground = '#c23d51'
var masculinBackground = '#4280c2'
var neutralBackground = '#4abf92'

// local stored bg value
femininBackground = localStorage.getItem('femininBackground');
masculinBackground = localStorage.getItem('masculinBackground');
neutralBackground = localStorage.getItem('neutralBackground');

// display the bg to all elements with the class + the color picker
document.querySelectorAll('.feminin-bg').forEach(function(femininElement) {
    femininElement.style.backgroundColor = femininBackground;
});
femininColorPicker.value = femininBackground;

document.querySelectorAll('.masculin-bg').forEach(function(masculinElement) {
    masculinElement.style.backgroundColor = masculinBackground;
});
masculinColorPicker.value = masculinBackground;

document.querySelectorAll('.neutral-bg').forEach(function(neutralElement) {
    neutralElement.style.backgroundColor = neutralBackground;
});
neutralColorPicker.value = neutralBackground;

// allow the user to choose color and save it in local storage 
femininColorPicker.addEventListener('change', function(){
    femininBackground = this.value
    document.querySelectorAll('.feminin-bg').forEach(function(femininElement) {
        femininElement.style.backgroundColor = femininBackground;
    });
    localStorage.setItem('femininBackground',femininBackground);
});

masculinColorPicker.addEventListener('change', function(){
    masculinBackground = this.value
    document.querySelectorAll('.masculin-bg').forEach(function(masculinElement) {
        masculinElement.style.backgroundColor = masculinBackground;
    });
    localStorage.setItem('masculinBackground',masculinBackground);
});

neutralColorPicker.addEventListener('change', function(){
    neutralBackground = this.value
    document.querySelectorAll('.neutral-bg').forEach(function(neutralElement) {
        neutralElement.style.backgroundColor = neutralBackground;
    });
    localStorage.setItem('neutralBackground',neutralBackground);
});


// ------------ ANIMATION HERO
TweenLite.set('.under-title',{x:'-100%'})
TweenLite.set('.hero-btn', {opacity:0})

const TL = gsap.timeline();

TL
//.to('.main-title', {x:0, duration:2})
.to('.under-title', {x:0, duration:1},)
.to('.hero-btn', {opacity:1})

//------------ Main title
var randomColor;

$(".main-title").hover(function(){
    getColor();
    gsap.to('.main-title-animation', {
        text:"LEARN using", 
        color:randomColor, 
        duration:1,
    });
  },
   function(){
    getColor();
    gsap.to('.main-title-animation', {
        text:"GERMAN in", 
        color:randomColor, 
        duration:1,
    });
});

function  getColor() {
    var colors = ['#a8c3ed','#f0b6db','#b6e5f0','#f0deb6','#cef5ea', 'white',];
    randomColor = colors[Math.floor(Math.random()*colors.length)];
}


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

/*
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

 */


