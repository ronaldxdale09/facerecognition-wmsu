

<?php 
 include('db.php');
                        if (isset($_POST['update'])) {
                            $id = $_POST['face_id'];
                            $name = $_POST['name'];
                            $status = $_POST['status'];

                            
                            // echo $name;
                            if ($status ==''){
                                $status = 'INACTIVE';
                            }

                            // echo $status;
        
                            $query = "UPDATE known_faces SET name = '$name', status='$status' WHERE name='$name'";
                                $results = mysqli_query($con, $query);


                                    //yung md5 for encryption yan, pero dih na ata possible yung feature na reset password pang gagamit tayo md5, pero oknayan atleast encrypted. 
                                    if ($results) {  
   
                                            header("Location: ../userInformation.php?view=$id");
                                           
                                       
                                    } else {
                                        echo "ERROR: Could not be able to execute $query. ".msqli_error($con);
                                    }
                                exit();
                                }
 ?>