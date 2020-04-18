console.log("Hello World");


// function posted_job_selected() {
//     const a = document.getElementById('posted_joo');
//     const b = a.options[a.selectedIndex].value
//     alert(b);
    

//     $.ajax({
//         url: "{% url 'applied_candi_by_job' %}",
//         data:{
//           'selected_job' : b
//         },
//         dataType: "json",
//         success:function (data){
//           document.getElementById('print_selected').innerHTML = data["respond"]
//         }
//     });

// };

// console.log(b + 'heheheh');



function posted_job_selected(){
  // alert('book selected');
  x = document.getElementById("posted_joo");
  b = x.options[x.selectedIndex].value
  console.log('book function runed' + ' this :' + b)


  $.ajax({
         url: "{% url 'applied_candi_by_job' %}",
         data:{
           'selected_data' : b
         },
         dataType: "json",
         success:function (data){
           document.getElementById('print_selected').innerHTML = data["respond"]
         }
  });

};