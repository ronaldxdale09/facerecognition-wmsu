<?php  
include('function/db.php');

 //filter.php  
 if(isset($_POST["from_date"], $_POST["to_date"], $_POST["face_id"]))  
 {  
      $output = '';  
      $query = "  
           SELECT * FROM attendance  
           WHERE face_id ='".$_POST["face_id"]."' AND date BETWEEN '".$_POST["from_date"]."' AND '".$_POST["to_date"]." '  
      ";  
      $result = mysqli_query($con, $query);  
      $output .= '  
           <table class="table table-hover">  
                <tr>  
                <th>Name </th>
                <th> Type </th>
                <th>Time </th>
                <th>Date</th>
                <th>Match Score</th>
                </tr>  
      ';  
      if(mysqli_num_rows($result) > 0)  
      {  
           while($row = mysqli_fetch_array($result))  
           {  
                $output .= '  
                     <tr>  
                         
                          <td>'. $row["name"] .'</td>  
                          <td>'. $row["personType"] .'</td>  
                          <td>'. $row["time"] .'</td>  
                          <td>'. $row["date"] .'</td>  
                          <td>'. $row["match_score"] .'</td>  
                     </tr>  
                ';  
           }  
      }  
      else  
      {  
           $output .= '  
                <tr>  
                     <td colspan="5">No Record Found</td>  
                </tr>  
           ';  
      }  
      $output .= '</table>';  
      echo $output;  
 }  
 ?>