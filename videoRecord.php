
<?php 
include('include/header.php');
include('include/navbar.php');
?>

<style> 
/* Three image containers (use 25% for four, and 50% for two, etc) */
.column {
  float: left;
  width: 23.33%;
  padding: 5px;
}

/* Clear floats after image containers */
.row::after {
  content: "";
  clear: both;
  display: table;
}

</style>

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
                                            <h5 class="m-b-10">Video Record Logs</h5>
                                            <p class="m-b-0">Western Mindanao State University</p>
                                        </div>
                                    </div>
                                    <div class="col-md-4">
                                        <ul class="breadcrumb">
                                            <li class="breadcrumb-item">
                                                <a href="index.html"> <i class="fa fa-home"></i> </a>
                                            </li>
                                            <li class="breadcrumb-item"><a href="#!">Video Record</a>
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
                                                        <h5>Date Filter</h5>
                                                        <form action="" method="get">
                                                        <div class="container">
                                                        <div class="row">
                                                    <div class="col"><b></b><input type="text" name="view" id='view' class="form-control" placeholder="Date Filter" /> </div>
                                                    <div class="col"> 
                                                        <button type="search"  class="btn btn-success btn-sm">Filter Date</button>  
                                                    </div>
                                                </div>

                                                        </form>




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
                                                    <div class="row">
                                                    <?php

$dir = "updated_facerecog/recorded/";
$videoW = 320;
$videoH = 240;
$exclude = array('.','..','.htaccess'); 
$q = (isset($_GET['view']))? strtolower($_GET['view']) : '';
if (!empty($q)) {
    $res = opendir($dir);
    while(false!== ($file = readdir($res))) { 
        
            if(strpos(strtolower($file),$q)!== false &&!in_array($file,$exclude)) { 
                echo 
                "
                    <div class=\"column\">
                        <video width=\"$videoW\" height=\"$videoH\" controls>
                          <source src=\"". $dir . $file ."\" type=\"video/mp4\">
                          <source src=\"". $dir . $file ."\" type=\"video/avi\">
                        </video>
                        <center>
                        <button type=\"button\" class=\"btn btn-outline-success\">". $file ."</button>
                        </center>
                    </div>
               
                ";
            } 
            
           
      

    }
  
    
}



else if (is_dir($dir))
{
    if ($dh = opendir($dir)){

        while (($file = readdir($dh)) !== false){

            if($file != '.' && $file != '..'){

                echo 
                "
                    <div class=\"column\">
                        <video width=\"$videoW\" height=\"$videoH\" controls>
                          <source src=\"". $dir . $file ."\" type=\"video/mp4\">
                          <source src=\"". $dir . $file ."\" type=\"video/avi\">
                        </video>
                        <center>
                        <button type=\"button\" class=\"btn btn-outline-success\">". $file ."</button>
                        </center>
                    </div>
               
                ";

            }
          

        }

        closedir($dh);

      }
     
}





?>

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
    <script>  
   $(document).ready(function(){  
        $.datepicker.setDefaults({  
             dateFormat: 'yy-mm-dd'   
        }); 
        $(function(){  
             $("#view").datepicker();  
          
        });   
       
   });  
</script>

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

</html>
