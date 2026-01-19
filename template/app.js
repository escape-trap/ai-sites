document.getElementById("app").innerHTML =
  "<input id='n' placeholder='Enter number'><button onclick='calc()'>Square</button><p id='r'></p>";

function calc(){
  let n = document.getElementById("n").value;
  document.getElementById("r").innerText = n*n;
}