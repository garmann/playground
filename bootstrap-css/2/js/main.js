var mySlider = {};

function initSlider(){
    var currentLeft = 0;
    var minleft = -200;
    var slider = document.getElementById('slider');

    var next = document.getElementById('next');
    var prev = document.getElementById('prev');

    mySlider.nextSlide = function(e){
        e.preventDefault();
      if (currentLeft > minleft){
        currentLeft = currentLeft - 100;
        slider.style.left = currentLeft + '%';
      } 
    }

    mySlider.prevSlide = function(e){
        e.preventDefault();
      if (currentLeft < 0){
        currentLeft = currentLeft + 100;
        slider.style.left = currentLeft + '%';
      } 
    }

    next.onclick = mySlider.nextSlide;
    prev.onclick = mySlider.prevSlide;
}

document.onload = initSlider();