document.addEventListener("DOMContentLoaded",
  function (event) {
    
    function selectYear (event) {
      // this.textContent = "Said it!";
      var year =
       document.getElementById("year").value;

       queue()
        .defer(d3.csv, "/byYear/"+year)
        .await(function(error, dataByYear){
                makeGraphs(error,dataByYear,"#figure2");
                });
    }

    // Unobtrusive event binding
    document.querySelector("button")
      .addEventListener("click", selectYear);

  }
);


