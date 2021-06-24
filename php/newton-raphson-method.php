<?php 
        // Formula: Xn+1 = Xn + C/Xn

        $X0 = 2;
        $C = 5;

        echo "Formula: Xn+1 = Xn + C/Xn\n";
        echo "X0: $X0\n";

        for ($n = 1; $n < 11; $n++) {
            $Xn = ($X0 + ($C / $X0)) / 2;
            if ($Xn == $X0) {
                break;
            } else {
                echo "X$n: $Xn\n";
                $X0 = $Xn;
            }
        }
?>