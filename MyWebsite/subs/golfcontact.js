document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#submit').addEventListener('click', function(){ //in the document, for every elemnt with the id "check," the addEventListener method will be added onto it, and the function that activiates it will be when the user clicks on the element
        let input = document.querySelector('input'); //declares a varible "correct" that is equal to the document method querySelector of any "input" element
        if(input.value == ''){ //if the value of the declared varible "input" is equal to the string 'Thompson Webb'
            alert("Please Enter All Information")
        } else { //if the value of the declared varible "input" is equal to any other string
            alert("Thank You!")
        }
     });
 });