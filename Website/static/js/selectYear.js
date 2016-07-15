document.addEventListener("DOMContentLoaded",
  function (event) {
    //This uses d3 to update graoh
    d3.select("#year").on("input", function() { update(+this.value);});
    //this sets the default value
    update(+2005);
  // update the elements
    function update(year) {
        // adjust the text on the range slider
        document.getElementById("yearSelected").innerHTML = year;
        queue()
        .defer(d3.csv, "/byYear/"+year)
        .await(function(error, dataByAll){
          makeGraphs(error,dataByAll,"#figure2");
        });
    }

    //This uses the html dom manipulation to control the data
    function selectCourse(event) {
    //This select the course value
      var course =
       document.getElementById("course").value;
       queue()
        .defer(d3.csv, "/byCourse/"+course)
        .await(function(error, dataByCourse){
                makeGraphs(error, dataByCourse, "#figure3");
                });
    };
    // Unobtrusive event binding
    document.querySelector("button")
      .addEventListener("click", selectCourse);
  }
);