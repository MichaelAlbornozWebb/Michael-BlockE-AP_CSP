document.addEventListener('DOMContentLoaded', function() { //DOM Content Loaded, or Document Object Model loads the document method of addEventListener, which returns the modified specified element within the document

    let correct = document.querySelector('.buttonmccorrect'); //declares a varible "correct" that is equal to the document method querySelector of any element with the class "buttonmccorrect"
    correct.addEventListener('click', function(event) { //on the event where the user clicks on the button
        correct.style.backgroundColor = 'green'; //change the button's background color to green
        document.querySelector('#multichoice').innerHTML = 'Correct!'; //chnage the inner HTML of any element with the id "multichoice" to have their text be "Correct!"
        });

    let incorrects = document.querySelectorAll('.buttonmc'); //declares a varible "correct" that is equal to the document method querySelector of any element with the class "buttonmc"
    for(let i = 0; i < incorrects.length; i++) //makes a for loop for every element that is being modified by the querySelector
    {
        incorrects[i].addEventListener('click', function(event) { //on the event where the user clicks on the button
        incorrects[i].style.backgroundColor = 'red'; //change the button's background color to red
        document.querySelector('#multichoice').innerHTML = 'Incorrect'; //chnage the inner HTML of any element with the id "multichoice" to have their text be "Incorrect!"
        });
    }

    document.querySelector('#check').addEventListener('click', function(){ //in the document, for every elemnt with the id "check," the addEventListener method will be added onto it, and the function that activiates it will be when the user clicks on the element
       let input = document.querySelector('input'); //declares a varible "correct" that is equal to the document method querySelector of any "input" element
       if(input.value == 'Thompson Webb'){ //if the value of the declared varible "input" is equal to the string 'Thompson Webb'
           input.style.backgroundColor = 'green'; //change the background color of the elemenet to green
           document.querySelector('#writtenChoice').innerHTML = 'Correct!'; //chnage the inner HTML of any element with the id "writtenChoice" to have their text be "Correct!"
       } else { //if the value of the declared varible "input" is equal to any other string
           input.style.backgroundColor = 'red'; //change the background color of the elemenet to red
           document.querySelector('#writtenChoice').innerHTML = 'Incorrect'; //chnage the inner HTML of any element with the id "writtenChoice" to have their text be "Incorrect!"
       }
    });
});
