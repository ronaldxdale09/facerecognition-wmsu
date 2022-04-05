
<?php 
 include('db.php');
                        if (isset($_POST['update'])) {
                            $year = $_POST['year'];
                        
                            
                            // echo $name;
                

                            // echo $status;
        
                            $query = "UPDATE settings SET academicYear = '$year'";
                                $results = mysqli_query($con, $query);


                                    //yung md5 for encryption yan, pero dih na ata possible yung feature na reset password pang gagamit tayo md5, pero oknayan atleast encrypted. 
                                    if ($results) {  
   
                                            header("Location: ../settings.php");
                                           
                                       
                                    } else {
                                        echo "ERROR: Could not be able to execute $query. ".msqli_error($con);
                                    }
                                exit();
                                }
 ?>