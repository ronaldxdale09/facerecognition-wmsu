<?php
   include('include/header.php');
   include('include/navbar.php');
   
   if (isset($_GET['view'])) {
       $id = $_GET['view'];
     }
   
   $results = mysqli_query($con, "SELECT * from known_faces WHERE face_id='$id'"); 
   $row = mysqli_fetch_array($results)
   ?>
<head>
   <!--<link rel="stylesheet" href="../facerecog-webapp-main/assets//css/User.css"> -->
   <link rel="stylesheet" type="text/css" href="assets/css/toggle.css">
</head>
<body>
   <div class="pcoded-content">
      <!-- Page-header start -->
      <div class="page-header">
         <div class="page-block">
            <div class="row align-items-center">
               <div class="col-md-8">
                  <div class="page-header-title">
                     <h5 class="m-b-10">User Information</h5>
                  </div>
               </div>
               <div class="col-md-4">
                  <ul class="breadcrumb">
                     <li class="breadcrumb-item">
                        <a href="index.html"> <i class="fa fa-home"></i> </a>
                     </li>
                     <li class="breadcrumb-item"><a href="#!">User Information</a>
                     </li>
                  </ul>
               </div>
            </div>
         </div>
      </div>
      <br>
      <!-- Page-header end -->
   </div>
   <div class="container">
   <div class="main-body">
      <div class="row gutters-sm">
         <div class="col-md-2"></div>
         <div class="col-md-4 mb-3">
            <div class="card">
               <div class="card-body">
                  <div class="d-flex flex-column align-items-center text-center">
                     <?php 
                        if ($row['status']=='ACTIVE'){
                           $color='green';
                        }
                        else
                           $color='red'
                        
                        ?>
                     <img src="updated_facerecog/datasets/face.<?php echo $row['face_id'];?>.<?php echo $row['userType']; ?>/user.<?php echo $row['face_id']; ?>.15.jpg" alt="Admin" class="rounded-circle" width="150" style="border:5px solid <?php echo $color ?>">
                     <div class="mt-3">
                        <h4>   <?php echo $row['name'] ?></h4>
                        <b> <button type="button" style='width:200px;background-color:<?php echo $color ?>;border-radius:35px;color:white;'>
                        <?php echo $row['status'];?>
                        </button></b>
                     </div>
                  </div>
               </div>
               <!-- Button to Open the Modal -->
               <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#myModal">
               Update Information
               </button>
            </div>
         </div>
         <div class="col-md-6">
            <div class="card mb-3">
               <div class="card-body">
                  <div class="row">
                     <div class="col-sm-3">
                        <h6 class="mb-0">Full Name</h6>
                     </div>
                     <div class="col-sm-9 text-secondary">
                        <?php echo $row['name'] ?>
                     </div>
                  </div>
                  <hr>
                  <div class="row">
                     <div class="col-sm-3">
                        <h6 class="mb-0">Type</h6>
                     </div>
                     <div class="col-sm-9 text-secondary">
                        Student
                     </div>
                  </div>
                  <hr>
                  <div class="row">
                     <div class="col-sm-3">
                        <h6 class="mb-0">Birthdate</h6>
                     </div>
                     <div class="col-sm-9 text-secondary">
                        <?php echo $row['birthdate'] ?>
                     </div>
                  </div>
                  <hr>
                  <div class="row">
                     <div class="col-sm-3">
                        <h6 class="mb-0">College</h6>
                     </div>
                     <div class="col-sm-9 text-secondary">
                        <?php echo $row['college'] ?>
                     </div>
                  </div>
                  <hr>
                  <div class="row">
                     <div class="col-sm-3">
                        <h6 class="mb-0">Position</h6>
                     </div>
                     <div class="col-sm-9 text-secondary">
                        <?php echo $row['position'] ?>
                     </div>
                  </div>
                  <hr>
               </div>
               <div class="row">
                  <div class="col-md-4">
                  </div>
                  <div class="col-md-4">
                     <!-- The Modal -->
                     <div class="modal" id="myModal">
                        <div class="modal-dialog">
                           <div class="modal-content">
                              <!-- Modal Header -->
                              <div class="modal-header">
                                 <h4 class="modal-title">Update Information</h4>
                                 <button type="button" class="close" data-dismiss="modal">&times;</button>
                              </div>
                              <!-- Modal body -->
                              <div class="modal-body">
                                 <form  action="function/updateData.php" method="post" enctype="multipart/form-data" >
                                    <div class="form-group">
                                       <label>Face ID:</label>
                                       <input type="" name="face_id" value='<?php echo $row['face_id'] ?>' class="form-control" readonly>
                                    </div>
                                    <div class="form-group">
                                       <label>Full Name:</label>
                                       <input type="" name="name" value='<?php echo $row['name'] ?>' class="form-control">
                                    </div>
                                    <div class="form-group">
                                       <label>Birthdate :</label>
                                       <input type="" name="" value='<?php echo $row['birthdate'] ?>' class="form-control">
                                    </div>
                                    <div class="form-group">
                                       <label>College:</label>
                                       <input type="" name="" value='<?php echo $row['college'] ?>' class="form-control">
                                    </div>
                                    <div class="form-group">
                                       <label>Course :</label>
                                       <input type="" name="" value='<?php echo $row['course'] ?>' class="form-control">
                                    </div>
                                    <div class="form-group">
                                       <label>Status :</label> <br>
                                       <label class="switch">
                                          <input type="checkbox" name='status' id="togBtn" value="ACTIVE"  <?php echo ($row['status'] == 'ACTIVE' ) ? 'checked' : NULL ; ?>>
                                          <div class="slider round">
                                             <!--ADDED HTML --><span class="on">ACTIVE</span><span class="off">INACTIVE</span><!--END-->
                                          </div>
                                       </label>
                                    </div>
                              </div>
                              <!-- Modal footer -->
                              <div class="modal-footer">
                              <button type="submit" class="btn btn-success" name='update' id="update">Save</button>
                              <button type="button" class="btn btn-danger" data-dismiss="modal">Cancel</button>
                              </div>
                              </form>
                           </div>
                        </div>
                     </div>
                     
                  </div>

               </div>
               <br>
            </div>
         </div>
      </div>
   </div>
   <div class="row">
         <div class="col-sm-12">
            <div class="card">
               <div class="card-header">
                  <h5>Log Record of <?php echo $row['name']?></h5>
                  <br> <br>
                  <div class="row">
                     <div class="col"><b></b><input type="text" name="from_date" id="from_date" class="form-control" placeholder="From Date" /> </div>
                     <div class="col"><input type="text" name="to_date" id="to_date" class="form-control" placeholder="To Date" />  </div>
                     <div class="col"> 
                        <button type="button" name="filter" id="filter" value="Filter" class="btn btn-success btn-sm">Filter Date</button>  
                     </div>
                  </div>
                  <div class="card-block">
                     <div id="log_table">
                        <table class="table table-hover" id='record_table' width="100%" cellspacing="0">
                           <?php $logrecs = mysqli_query($con, "SELECT * from attendance where face_id='$id'"); ?>
                           <thead>
                              <tr>
                                 <th>Name </th>
                                 <th> Type </th>
                                 <th>Time </th>
                                 <th>Date</th>
                                 <th>Match Score</th>
                              </tr>
                           </thead>
                           <tbody>
                              <?php while ($arr = mysqli_fetch_array($logrecs)) { ?>
                              <tr>
                                 <td><?php echo $arr['name']; ?></td>
                                 <td><?php echo $arr['personType']; ?></td>
                                 <td><?php echo $arr['time']; ?></td>
                                 <td><?php echo $arr['date']; ?></td>
                                 <td><?php echo $arr['match_score']; ?></td>
                              </tr>
                              <?php } ?>
                           </tbody>
                        </table>
                     </div>
                  </div>
               </div>
            </div>
         </div>
                             

   <!--<div id="styleSelector"></div>
      </div>
      </div>
      </div>
      </div> -->
   <script type="text/javascript" src="assets/js/jquery/jquery.min.js "></script>
   <script type="text/javascript" src="assets/js/jquery-ui/jquery-ui.min.js "></script>
   <script type="text/javascript" src="assets/js/popper.js/popper.min.js"></script>
   <script type="text/javascript" src="assets/js/bootstrap/js/bootstrap.min.js "></script>
   <!-- waves js -->
   <script src="assets/pages/waves/js/waves.min.js"></script>
   <!-- jquery slimscroll js -->
   <script type="text/javascript" src="assets/js/jquery-slimscroll/jquery.slimscroll.js"></script>
   <script src="assets/js/pcoded.min.js"></script>
   <script src="assets/js/vertical/vertical-layout.min.js"></script>
   <script src="assets/js/jquery.mCustomScrollbar.concat.min.js"></script>
   <!-- Custom js -->
   <script type="text/javascript" src="assets/js/scripts.min.js"></script>
</body>
</html>
<script>  
   $(document).ready(function(){  
        $.datepicker.setDefaults({  
             dateFormat: 'yy-mm-dd'   
        });  
        $(function(){  
             $("#from_date").datepicker();  
             $("#to_date").datepicker();  
        });  
        $('#filter').click(function(){  
             var from_date = $('#from_date').val();  
             var to_date = $('#to_date').val();  
             if(from_date != '' && to_date != '')  
             {  
                  $.ajax({  
                       url:"filterPersonalRecord.php",  
                       method:"POST",  
                       data:{from_date:from_date, to_date:to_date,face_id:<?php echo $row['face_id'] ?>},  
                       success:function(data)  
                       {  
                            $('#log_table').html(data);  
                       }  
                  });  
             }  
             else  
             {  
                  alert("Please Select Date");  
             }  
        });  
   });  
</script>
<script type="text/javascript" src="//cdn.datatables.net/1.10.21/js/jquery.dataTables.min.js"></script>
<script>
   $(document).ready(function() {
       $('#record_table').DataTable({
        dom: 'Bfrtip',
        buttons: [
            'excelHtml5',
            'csvHtml5',
            'pdfHtml5',
            'print'
        ]
    } );
   });
</script>
<script type="text/javascript" src="https://cdn.datatables.net/buttons/2.1.0/js/dataTables.buttons.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.1.3/jszip.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.53/pdfmake.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.53/vfs_fonts.js"></script>
<script type="text/javascript" src="https://cdn.datatables.net/buttons/2.1.0/js/buttons.html5.min.js"></script>
<script type="text/javascript" src="https://cdn.datatables.net/buttons/2.1.0/js/buttons.print.min.js"></script>