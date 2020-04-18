function posted_job_selected(){
    // alert('book selected');
    x = document.getElementById("posted_joo");
    b = x.options[x.selectedIndex].value
    console.log('book function runed' + ' this :' + b)
   
  
    $.ajax({
           url: "applied_candi_by_job",
           data:{
             'xyz' : b
           },
           dataType: "json",
           success:function (data){
             document.getElementById('print_selected').innerHTML = data["respond"]
           }
    });
  
  };