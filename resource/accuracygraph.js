$(document).ready(function(){
    $.ajax({
      url : "linegraph.php",
      type : "GET",
      success : function(data){
        console.log(data);
  
      },
      error : function(data) {
  
      }
    });
  });

  <script type="text/javascript" src="https://code.jquery.com/jquery-1.7.1.min.js"></script>
