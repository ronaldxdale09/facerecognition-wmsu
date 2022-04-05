<?php 
   include('include/header.php');
   include('include/navbar.php');
   ?>
<body>
<style>
button {
    background-color: #04AA6D;
  border: none;
  color: white;
  padding: 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
}
</style>

<?php

$getSettings = mysqli_query($con, "SELECT * from settings"); 
$arrYear = mysqli_fetch_array($getSettings);
$year = $arrYear['academicYear'];


if(isset($_GET['search']))
{
    $valueToSearch = $_GET['search'];
    $year = $valueToSearch;
    // search in all table columns
    // using concat mysql function
    $search_result = mysqli_query($con, "SELECT * from attendance WHERE CONCAT(`academicYear`) LIKE '%".$valueToSearch."%' ORDER BY id DESC");
    
}
 else {
    $search_result = mysqli_query($con, "SELECT * from attendance WHERE academicYear='".$arrYear['academicYear']."'  ORDER BY id DESC");
}


?>



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
                     <h4 class="m-b-10">LOG INFORMATION</h4>
                     <p class="m-b-0">Face Recognition System</p>
                  </div>
               </div>
               <div class="col-md-4">
                  <ul class="breadcrumb">
                  <button type="button" class="btn btn-info" data-toggle="modal" data-target="#myModal">
                        Academic Year
                        </button>
                  </ul>
               </div>
            </div>
         </div>
      </div>
      <!-- Page-header end -->
      <div class="pcoded-inner-content">
         <div class="main-body">
            <div class="page-wrapper">
               <!-- Hover table card start -->
               <div class="card">
                  <div class="card-header">
                     <h5>LOG RECORD |  <?php echo "Today is " . date("Y/m/d") ; ?> |        Academic Year : <?php echo $year ?></h5>
                     <br> <br>
                     <div class="row">
                        <div class="col-sm">
                           <div class="row">
                              <div class="col">
                                 <b></b>
                                 <h5> Date Filter </h5>
                              </div>
                              <div class="col"><b></b><input type="text" id="min" name="min"  class="form-control" placeholder="From Date" /> </div>
                              <div class="col"><input type="text" id="max" name="max"  class="form-control" placeholder="To Date" />  </div>
                           </div>
                        </div>
                        <div class="col-sm">
                       
                        </div>
                     </div>
                     
                  </div>
                  <div class="card-block table-border-style" id='DataTables'>
                     <div class="table-responsive " id="log_table">
                        <table class="table table-hover" id="table_id" class="display" style="width:100%">
                           <thead>
                              <tr>
                                 <th >Profile </th>
                                 <th>Name </th>
                                 <th>Type <br></th>
                                 <th>College <br></th>
                                 <th>Time </th>
                                 <th>Date</th>
                                 <th>Match Score</th>
                                 <th>Gate Entry</th>
                                 <th>Entry</th>
                             
                              </tr>
                              <th > </th>
                                 <th> </th>
                                 <th></th>
                                 <th></th>
                                 <th> </th>
                                 <th></th>
                                 <th></th>
                                 <th></th>
                                 <th></th>
                           </thead>
                           <tbody>
                              <?php while ($row = mysqli_fetch_array($search_result)) {
                                 $face_id= $row['face_id'];
                                 $getInfo = mysqli_query($con, "SELECT * from known_faces where face_id='$face_id'");
                                 $arr = mysqli_fetch_array($getInfo);
                                 
                                 if ($arr['status']=='ACTIVE'){
                                    $color='green';
                                 }
                                 else{
                                    $color='red';
                                 }
                                 
                                 if ($row['entry']=='Entrance'){
                                     $Ecolor='success';
                                  }
                                  else{
                                     $Ecolor='danger';
                                  }
                                 
                                 
                                 ?>
                              <tr>
                                 <td>
                                    <nobr> <img src="updated_facerecog/datasets/face.<?php echo $row['face_id'];?>.<?php echo $row['personType']; ?>/user.<?php echo $row['face_id']; ?>.10.jpg" alt="..." class="img img-fluid" width="45" style="border-radius: 50%;border:4px solid <?php echo $color ?>" ></nobr>
                                 </td>
                                 <td ><?php echo $row['name']; ?></td>
                                 <td><?php echo $row['personType']; ?></td>
                                 <td><?php echo $row['college']; ?></td>
                                 <td><?php echo $row['time']; ?></td>
                                 <td><?php echo $row['date']; ?></td>
                                 <td><?php echo $row['match_score']; ?>%</td>
                                 <td><?php echo $row['gate']; ?></td>
                                <td class="badge badge-<?php echo $Ecolor?>" style='text-align: center;'><?php echo $row['entry']; ?></td>
                              
                              </tr>
                              <?php } ?>
                           </tbody>
                           <tfoot>
                              <tr>
                                 <th >Profile </th>
                                 <th>Name </th>
                                 <th></th>
                                 <th></th>
                                 <th>Time </th>
                                 <th>Date</th>
                                 <th>Match Score</th>
                                 <th></th>
                                 <th></th>
                              </tr>
                           </tfoot>
                        </table>
                     </div>
                  </div>
               </div>
               <!-- Hover table card end -->
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
                                 <form  action="" method="get" enctype="multipart/form-data" >
                                 <div class="form-group">
                                <label>Academic Year </label>
                                <select name="search"   class="form-control action" required> 
                            <option value="2020-2021">2020-2021</option>
                            <option value="2021-2022">2021-2022</option>
                            <option value="2022-2023">2022-2023</option>
                            <option value="2024-2025">2024-2025</option>
                            <option value="2026-2027">2026-2027</option>
                            </select>
                            </div>
                                   
                              </div>
                              <!-- Modal footer -->
                              <div class="modal-footer">
                              <button type="search" class="btn btn-success" >Save</button>
                              <button type="button" class="btn btn-danger" data-dismiss="modal">Cancel</button>
                              </div>
                              </form>
                           </div>
                        </div>
                     </div>
<!-- end modal -->














               
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
   <!-- datatable -->
</body>
<!-- END -->
<script type="text/javascript" src="//cdn.datatables.net/1.10.21/js/jquery.dataTables.min.js"></script>
<script>
   // for date
   
   var minDate, maxDate;
    
   // Custom filtering function which will search data in column four between two values
   $.fn.dataTable.ext.search.push(
       function( settings, data, dataIndex ) {
           var min = minDate.val();
           var max = maxDate.val();
           var date = new Date( data[5] );
   
    
           if (
               ( min === null && max === null ) ||
               ( min === null && date <= max ) ||
               ( min <= date   && max === null ) ||
               ( min <= date   && date <= max )
           ) {
               return true;
           }
           return false;
       }
   );
   
   
   // for date filter
   
   
   $(document).ready(function() {
       // Create date inputs
       minDate = new DateTime($('#min'), {
           format: 'YYYY-MM-DD'
       });
       maxDate = new DateTime($('#max'), {
           format: 'YYYY-MM-DD'
       });
    
       // DataTables initialisation
       var table = $('#table_id').DataTable(
           {
              
           dom: 'Bfrtip',
           buttons: [
               'excelHtml5',
               'csvHtml5',
               'pdfHtml5',
               'print',

               
               
           ],
       initComplete: function () {
               this.api().columns( [ 2, 3, 7,8 ] ).every( function () {
                   var column = this;
                   var select = $(' <select  class="form-control action" required> <option value="">All</option></select>')
                       .appendTo( $(column.header()) )
                       .on( 'change', function () {
                           var val = $.fn.dataTable.util.escapeRegex(
                               $(this).val()
                           );
    
                           column
                                .search(val ? '^' + val + '$' : '', true, false)
                               .draw();
                       } );
    
                   column.data().unique().sort().each( function ( d, j ) {
                    select.append('<option value="' + d + '">' + d + '</option>')
                   } );
               } );
           }
       
       
       
       }
       );
    
       // Refilter the table
       $('#min, #max').on('change', function () {
           table.draw();
       });
   });
   
   
   
   
       
</script> 
<!-- filter -->
<!-- end filter -->
</html>
<script type="text/javascript" src="https://cdn.datatables.net/buttons/2.1.0/js/dataTables.buttons.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.1.3/jszip.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.53/pdfmake.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.53/vfs_fonts.js"></script>
<script type="text/javascript" src="https://cdn.datatables.net/buttons/2.1.0/js/buttons.html5.min.js"></script>
<script type="text/javascript" src="https://cdn.datatables.net/buttons/2.1.0/js/buttons.print.min.js"></script>
<!-- for date filter -->
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.18.1/moment.min.js"></script>
<script type="text/javascript" src="https://cdn.datatables.net/datetime/1.1.1/js/dataTables.dateTime.min.js"></script>