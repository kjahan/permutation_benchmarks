<?php
function permutation($str, $i) {
	$n = strlen($str);
	if ($i == $n)
		print "$str\n";
	else {
		for ($j = $i; $j < $n; $j++) {
			swap($str, $i, $j);
			permutation($str, $i + 1);
			swap($str, $i, $j); // backtrack.
		}
	}
}

function swap(&$str,$i,$j) {
	$temp = $str[$i];
 	$str[$i] = $str[$j];
	$str[$j] = $temp;
}

$str = "abcdefghij";
permutation($str, 0);
?>
