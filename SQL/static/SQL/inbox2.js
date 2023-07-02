let div = document.querySelector("#w3-exerciseform")
let old_div = "";
document.addEventListener("DOMContentLoaded", function() {
    
})
function test(title) {
    fetch(`/answer/${title}`)
    .then(response => {
        if (!response.ok) {
            throw new Error("Request failed with status " + response.status);
          }
        return response.json();
    })
    .then(data => {
        
        const input = document.getElementsByTagName('input')
        let answer = ""
        for(let i=0;i<input.length;i++) {
            answer = answer.concat(" ",input[i].value)
        }
        console.log(answer)
        console.log(data)
        old_div = document.querySelector("#w3-exerciseform").innerHTML
           if(answer.trim().toUpperCase() === data.toUpperCase()) {
                div.innerHTML = `
                <div id="assignmentCorrect" onclick="closeNotCorrect()" style="display: block;">
                    <h2>Correct!</h2>
                    <span style="cursor:pointer" id="correctnextbtn">❮ Back </span>
                </div> 
                `
           }
           else {
                div.innerHTML = `
                    <div id="assignmentNotCorrect" onclick="closeNotCorrect(event)" style="display: block;">
                        <h2>Not Correct</h2>
                        <p>Click <u>here</u> to try again.</p>   
                    </div>
                `
           }
    })
}
function closeNotCorrect(event) {
    div.innerHTML = old_div
}
