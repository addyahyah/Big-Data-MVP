document.addEventListener("DOMContentLoaded",
  function (event) {
    function selectYear (event) {
      //This select the year value
      var year =
       document.getElementById("year").value;

       //This change the display year
      document.getElementById("yearSelected").innerHTML = year;

       queue()
        .defer(d3.csv, "/byYear/"+year)
        .await(function(error, dataByYear){
                makeGraphs(error,dataByYear,"#figure2");
                });
    }
    // Unobtrusive event binding
    document.querySelector("input")
      .addEventListener("change", selectYear);
  }
);


