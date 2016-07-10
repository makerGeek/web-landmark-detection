<?php
/* require the user as the parameter */
if(isset($_GET['img'])) {


	$imgName=$_GET['img'];
	$last_line = system('C:\\Python27\\python.exe getDimensions.py '.$imgName, $retval);

//	$last_line = exec('python t2', $retval);
//	echo "<br>ll:".$last_line;
//	echo "<br>rv:".$retval;

	// /* soak in the passed variable or set our own */
	// $number_of_posts = isset($_GET['num']) ? intval($_GET['num']) : 10; //10 is the default
	// $format = strtolower($_GET['format']) == 'json' ? 'json' : 'xml'; //xml is the default
	// $user_id = intval($_GET['user']); //no default
	//
	//
	// /* create one master array of the records */
	// $posts = array_fill(5, 6, 'banana');
	//
	//
	// /* output in necessary format */
	// if($format == 'json') {
	// 	header('Content-type: application/json');
	// 	echo json_encode(array('posts'=>$posts));
	// }
	// else {
	// 	header('Content-type: text/xml');
	// 	echo '<posts>';
	// 	foreach($posts as $index => $post) {
	// 		if(is_array($post)) {
	// 			foreach($post as $key => $value) {
	// 				echo '<',$key,'>';
	// 				if(is_array($value)) {
	// 					foreach($value as $tag => $val) {
	// 						echo '<',$tag,'>',htmlentities($val),'</',$tag,'>';
	// 					}
	// 				}
	// 				echo '</',$key,'>';
	// 			}
	// 		}
	// 	}
	// 	echo '</posts>';
	// }

}

?>
