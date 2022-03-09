<?php
//97
$i=0;$x="Fizz";$y="Buzz";while(++$i<101){echo($i%15==0?$x.$y:($i%3==0?$x:($i%5==0?$y:$i)))."\n";}