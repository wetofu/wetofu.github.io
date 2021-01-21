// var search_input = document.querySelector("#search_input");

// search_input.addEventListener("keyup", function(e){
//   var span_items = document.querySelectorAll("li a");
//   var table_body = document.querySelector(".table_body ul");
//   var search_item = e.target.value.toLowerCase();
 
//  span_items.forEach(function(item){
//    if(item.textContent.toLowerCase().indexOf(search_item) != -1){
//       item.closest("li").style.display = "block";
//    }
//    else{
//      item.closest("li").style.display = "none";
//      }
//  })
  
// });
// function myFunction() {
//     var input, filter, ul, li, a, i, txtValue;
//     input = document.getElementById("search_input");
//     filter = input.value.toUpperCase();
//     ul = document.getElementById("myUL");
//     li = ul.getElementsByTagName("li");
//     // li = ul.getElementById("gantii");    
//     for (i = 0; i < li.length; i++) {
//         a = li[i].getElementsByTagName("a")[0];
//         txtValue = a.textContent || a.innerText;
//         if (txtValue.toUpperCase().indexOf(filter) > -1) {
//             li[i].style.display = "";
//         } else {
//             li[i].style.display = "none";
//         }
//     }
// }
