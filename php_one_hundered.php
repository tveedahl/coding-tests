<?php
    /**
     * Iterate through numbers 1 to 100
     */
    for($i = 1; $i < 101; $i++) {
        /**
         * Is $i a multiple of 3, 5, or both
         */
        if ($i % 3 == 0) {
            echo "Research\n";
        } elseif ($i % 5 == 0) {
            echo "Square\n";
        } else {
            echo "Research_Square\n";
        }    
    }
?>