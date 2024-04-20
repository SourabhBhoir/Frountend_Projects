const b1 = document.querySelector('.b1');
const b2 = document.querySelector('.b2');
const b3 = document.querySelector('.b3');
const b4 = document.querySelector('.b4');
const body = document.querySelector('body');



b1.addEventListener('click',function(){
    body.style.backgroundColor = 'aqua';
});

b2.addEventListener('click',function(){
    body.style.backgroundColor = 'yellow';
});
b3.addEventListener('click',function(){
    body.style.backgroundColor = 'violet';
});
b4.addEventListener('click',function(){
    body.style.backgroundColor = 'yellowgreen';
});