<?php 
   include('include/header.php');
   include('include/navbar.php');
   ?>

<body>
   <!-- Pre-loader start -->
   <div class="theme-loader">
      <div class="loader-track">
         <div class="preloader-wrapper">
            <div class="spinner-layer spinner-blue">
               <div class="circle-clipper left">
                  <div class="circle"></div>
               </div>
               <div class="gap-patch">
                  <div class="circle"></div>
               </div>
               <div class="circle-clipper right">
                  <div class="circle"></div>
               </div>
            </div>
            <div class="spinner-layer spinner-red">
               <div class="circle-clipper left">
                  <div class="circle"></div>
               </div>
               <div class="gap-patch">
                  <div class="circle"></div>
               </div>
               <div class="circle-clipper right">
                  <div class="circle"></div>
               </div>
            </div>
            <div class="spinner-layer spinner-yellow">
               <div class="circle-clipper left">
                  <div class="circle"></div>
               </div>
               <div class="gap-patch">
                  <div class="circle"></div>
               </div>
               <div class="circle-clipper right">
                  <div class="circle"></div>
               </div>
            </div>
            <div class="spinner-layer spinner-green">
               <div class="circle-clipper left">
                  <div class="circle"></div>
               </div>
               <div class="gap-patch">
                  <div class="circle"></div>
               </div>
               <div class="circle-clipper right">
                  <div class="circle"></div>
               </div>
            </div>
         </div>
      </div>
   </div>
   <div class="pcoded-content">
      <!-- Page-header start -->
      <div class="page-header">
         <div class="page-block">
            <div class="row align-items-center">
               <div class="col-md-8">
                  <div class="page-header-title">
                     <h4 class="m-b-10">REGISTERED USER</h4>
                     <p class="m-b-0">WESTERN MINDANAO STATE UNIVESITY</p>
                  </div>
               </div>
               <div class="col-md-4">
                  <ul class="breadcrumb">
                     <li class="breadcrumb-item">
                        <a href="index.html"> <i class="fa fa-home"></i> </a>
                     </li>
                     <li class="breadcrumb-item"><a href="#!">Registered Users</a>
                     </li>
                  </ul>
               </div>
            </div>
         </div>
      </div>
      <!-- Page-header end -->
      <div class="pcoded-inner-content">
         <div class="main-body">
            <div class="page-wrapper">
               <div class="page-body">
                  <div class="row">
                     <div class="col-sm-12">
                        <div class="card">
                           <div class="card-header">
                              <h5>Hello card</h5>
                              
                              <div class="card-header-right">
                                 <ul class="list-unstyled card-option">
                                    <li>
                                       <i class="fa fa fa-wrench open-card-option"></i>
                                    </li>
                                    <li>
                                       <i class="fa fa-window-maximize full-card"></i>
                                    </li>
                                    <li>
                                       <i class="fa fa-minus minimize-card"></i>
                                    </li>
                                    <li>
                                       <i class="fa fa-refresh reload-card"></i>
                                    </li>
                                    <li>
                                       <i class="fa fa-trash close-card"></i>
                                    </li>
                                 </ul>
                              </div>
                           </div>
                           <div class="card-block">
                              <div class="row m-b-30">
                                 <div class="col-lg-12 col-xl-12">
                                    <div class="sub-title">Default</div>
                                    <!-- Nav tabs -->
                                    <ul class="nav nav-tabs md-tabs" role="tablist">
                                       <li class="nav-item">
                                          <a class="nav-link active" data-toggle="tab" href="#home3" role="tab">Student</a>
                                          <div class="slide"></div>
                                       </li>
                                       <li class="nav-item">
                                          <a class="nav-link" data-toggle="tab" href="#profile3" role="tab">Employee</a>
                                          <div class="slide"></div>
                                       </li>
                                    </ul>
                                    <!-- Tab panes -->
                                    <div class="tab-content card-block">
                                       <div class="tab-pane active" id="home3" role="tabpanel">
                                          <!-- STUDENT PAGE -->
                                          <!-- Hover table card start -->
                                          <div class="card">
                                          
                                             <div class="card-header">
                                                <h4>LIST OF REGISTERED STUDENT</h4>
                                                <div class="card-header-right">
                                                   <ul class="list-unstyled card-option">
                                                      <li><i class="fa fa fa-wrench open-card-option"></i></li>
                                                      <li><i class="fa fa-window-maximize full-card"></i></li>
                                                      <li><i class="fa fa-minus minimize-card"></i></li>
                                                      <li><i class="fa fa-refresh reload-card"></i></li>
                                                      <li><i class="fa fa-trash close-card"></i></li>
                                                   </ul>
                                                </div>
                                             </div>
                                             <div class="card-block table-border-style">
                                                <div class="table-responsive">
                                                   <table class="table table-hover" id="student-table">
                                                      <?php $results = mysqli_query($con, "SELECT * from known_faces WHERE userType='student'"); ?>
                                                      <thead>
                                                         <tr>
                                                            <th>Profile </th>
                                                            <th>Name </th>
                                                            <th>Gender</th>
                                                            <th>Birthdate </th>
                                                            <th>Course</th>
                                                           
                                                            <th>Action</th>
                                                         </tr>
                                                      </thead>
                                                      <tbody>
                                                         <?php while ($row = mysqli_fetch_array($results)) { 
                                                            
                                                            $face_id= $row['face_id'];
                                                            $getInfo = mysqli_query($con, "SELECT * from known_faces where face_id='$face_id'");
                                                            $arr = mysqli_fetch_array($getInfo);

                                                            if ($arr['status']=='ACTIVE'){
                                                               $color='green';
                                                            }
                                                            else{
                                                               $color='red';
                                                            }
                                                            
                                                            
                                                            
                                                            ?>
                                                         <tr>
                                                         <td><nobr> <img src="updated_facerecog/datasets/face.<?php echo $row['face_id'];?>.<?php echo $row['userType']; ?>/user.<?php echo $row['face_id']; ?>.10.jpg" alt="..." class="img img-fluid" width="45" style="border-radius: 50%;border:4px solid <?php echo $color ?>" ></nobr> </td>
                                                            <td><?php echo $row['name']; ?></td>
                                                            <td><?php echo $row['sex']; ?></td>
                                                            <td><?php echo $row['birthdate']; ?></td>
                                                            <td><?php echo $row['course']; ?></td>
                                                            <td><a href="userInformation.php?view=<?php echo $row['face_id']; ?>" class="btn btn-info "> VIEW PROFILE</a> </td>
                                                         </tr>
                                                      </tbody>
                                                      <?php } ?>
                                                   </table>
                                                </div>
                                             </div>
                                          </div>
                                          <!-- Hover table card end -->
                                          <!-- END STUDENT -->
                                       </div>
                                       <div class="tab-pane" id="profile3" role="tabpanel">
                                          <!-- EMPLOYEE PAGE -->
                                          <!-- Hover table card start -->
                                          <div class="card">
                                             <div class="card-header">
                                                <h4>LIST OF REGISTERED EMPLOYEE</h4>
                                                <div class="card-header-right">
                                                   <ul class="list-unstyled card-option">
                                                      <li><i class="fa fa fa-wrench open-card-option"></i></li>
                                                      <li><i class="fa fa-window-maximize full-card"></i></li>
                                                      <li><i class="fa fa-minus minimize-card"></i></li>
                                                      <li><i class="fa fa-refresh reload-card"></i></li>
                                                      <li><i class="fa fa-trash close-card"></i></li>
                                                   </ul>
                                                </div>
                                             </div>
                                             <div class="card-block table-border-style">
                                                <div class="table-responsive">
                                                <table class="table table-hover" id="student-table">
                                                      <?php $results = mysqli_query($con, "SELECT * from known_faces WHERE userType='Employee'"); ?>
                                                      <thead>
                                                         <tr>
                                                            <th>Profile </th>
                                                            <th>Name </th>
                                                            <th>Gender</th>
                                                            <th>Birthdate </th>
                                                            <th>College</th>
                                                            <th>Position</th>
                                                            <th>Action</th>
                                                         </tr>
                                                      </thead>
                                                      <tbody>
                                                         <?php while ($row = mysqli_fetch_array($results)) { 
                                                            
                                                            $face_id= $row['face_id'];
                                                            $getInfo = mysqli_query($con, "SELECT * from known_faces where face_id='$face_id'");
                                                            $arr = mysqli_fetch_array($getInfo);

                                                            if ($arr['status']=='ACTIVE'){
                                                               $color='green';
                                                            }
                                                            else{
                                                               $color='red';
                                                            }
                                                            
                                                            
                                                            
                                                            ?>
                                                         <tr>
                                                         <td><nobr> <img src="updated_facerecog/datasets/face.<?php echo $row['face_id'];?>.<?php echo $row['userType']; ?>/user.<?php echo $row['face_id']; ?>.10.jpg" alt="..." class="img img-fluid" width="45" style="border-radius: 50%;border:4px solid <?php echo $color ?>" ></nobr> </td>
                                                            <td><?php echo $row['name']; ?></td>
                                                            <td><?php echo $row['sex']; ?></td>
                                                            <td><?php echo $row['birthdate']; ?></td>
                                                            <td><?php echo $row['college']; ?></td>
                                                            <td><?php echo $row['position']; ?></td>
                                                            <td><a href="employeeInfo.php?view=<?php echo $row['face_id']; ?>" class="btn btn-info "> VIEW PROFILE</a> </td>
                                                         </tr>
                                                         <?php } ?>
                                                      </tbody>
                                                     
                                                   </table>
                                                </div>
                                             </div>
                                          </div>
                                          <!-- Hover table card end -->
                                          <!-- END EMPLOYEE -->
                                       </div>
                                    </div>
                                 </div>
                              </div>
                           </div>
                        </div>
                     </div>
                  </div>
               </div>
            </div>
         </div>
      </div>
      <div id="styleSelector"></div>
   </div>
   </div>
   </div>
   </div>
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
<script type="text/javascript" src="//cdn.datatables.net/1.10.21/js/jquery.dataTables.min.js"></script>
    <script>
    $(document).ready(function() {
        $('#student-table').DataTable();
    });
    </script>