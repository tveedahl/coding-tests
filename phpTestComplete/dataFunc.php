<?php
    class DataFunc {
        /**
         * Function to mask ID's
         */
        function mask ( $str, $start = 0, $length = null ) {
            $mask = preg_replace ( "/\S/", "xxx-xx-", $str );
            if( is_null ( $length )) {
                $mask = substr ( $mask, $start );
                $str = substr_replace ( $str, $mask, $start );
            } else{
                $mask = substr ( $mask, $start, $length );
                $str = substr_replace ( $str, $mask, $start, $length );
            }
            return $str;
        }

        /**
         * Function to remove unwanted FIRST/LAST name characters
         */
        function removeChars ($str) {
            $strippedStr = preg_replace("~[^A-Za-z-\s/]~", "", $str);
            return $strippedStr;
        }

        /**
         * Function to calculate TERM
         */
        function calcTerm ($effDate) {
            $termCalc = $effDate + 100;
            return $termCalc;
        }
    }
?>