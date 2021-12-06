// ------------ ANIMATION Index page
// Main title
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
        text:"GERMAN with", 
        color:randomColor, 
        duration:1,
    });
});

function  getColor() {
    var colors = ['#a8c3ed','#f0b6db','#b6e5f0','#f0deb6','#cef5ea', 'white','#c23d51','#4280c2','#4abf92'];
    randomColor = colors[Math.floor(Math.random()*colors.length)];
};

// animation words changing in why not with colors
let delayNounsChange = 8;

let femininNounsList = ["Welt","Stimme","Stadt","Zeit"];
const tlFeminin = new TimelineMax({ repeat: -1, repeatDelay: 1 });
// example change words
for (let i = 0 ; i < femininNounsList.length; i++ ){
    tlFeminin
    .to('.feminin-example', {
        text:femininNounsList[i], 
        duration:1,
        delay:delayNounsChange,
    })
};

const tlMasculin = new TimelineMax({ repeat: -1, repeatDelay: 1 });
let masculinNounsList = ["Name","Mund","Monat","Baum"];
for (let i = 0 ; i < masculinNounsList.length; i++ ){
    tlMasculin
    .to('.masculin-example', {
        text:masculinNounsList[i], 
        duration:1,
        delay:delayNounsChange,
    })
};

const tlNeuter = new TimelineMax({ repeat: -1, repeatDelay: 1 });
let neuterNounsList = ["Gesicht","Wasser","Bett","Auge"];
for (let i = 0 ; i < neuterNounsList.length; i++ ){
    tlNeuter
    .to('.neuter-example', {
        text:neuterNounsList[i],
        duration:1,
        delay:delayNounsChange,
    })
};

//-------------- colors picker
const femininColorPicker = document.getElementById('feminin-color-picker');
const masculinColorPicker = document.getElementById('masculin-color-picker');
const neutralColorPicker = document.getElementById('neutral-color-picker');

var femininBackground;
var masculinBackground;
var neutralBackground;


var LocalStorageColors= localStorage.getItem('LocalStorageColors') || '';
if (LocalStorageColors != 'yes') {
    resetColors();
 localStorage.setItem('LocalStorageColors','yes');
}

getLocalStorageColors();
displayColorsInHtml();

// allow user to reset to the default colors
document.querySelector(".reset-colors").addEventListener("click", resetColors);

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


// default bg value
function defaultColors(){
    femininBackground = '#AD0935';
    masculinBackground = '#075493';
    neutralBackground = '#0A867B'; 
}

// get local stored bg value (if no stored the default will be used)
function getLocalStorageColors(){
    femininBackground = localStorage.getItem('femininBackground');
    masculinBackground = localStorage.getItem('masculinBackground');
    neutralBackground = localStorage.getItem('neutralBackground');      
}

// reset default when button is clicked
function resetColors(){
    defaultColors();
    displayColorsInHtml()
    localStorage.setItem('femininBackground',femininBackground);
    localStorage.setItem('masculinBackground',masculinBackground);
    localStorage.setItem('neutralBackground',neutralBackground);
}

// display the bg to all elements with the class + the color picker
function displayColorsInHtml(){
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
}

//------------ English plural versions

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

