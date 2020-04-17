<?php
    /**
     * Include DataFunc class
     */
    include 'dataFunc.php';

    /**
     * Open txt file for data parsing
     */
    $txtFile = file_get_contents('test_data_in.txt');

    /**
     * Explode txt file contents into rows/array using new line delimiter
     */
    $rows = explode("\n", $txtFile);

    /**
     * Ignore txt file header array element for now
     */
    array_shift($rows);

    /**
     * Initialize new txt file for outputting
     */
    $file = "test_data_out.txt";

    /**
     * Initialize empty output array
     */
    $outputArray = array();
    
    /**
     * Iterate through $rows array and manipulate data
     */
    foreach($rows as $row => $data) {
        /**
         * Explode row data into array using tab delimiter
         */
         $rowData = explode("\t", $data);

        /**
         * Instantiate DataFunc class and complete required tasks
         */
        $dataFunc = new dataFunc;

        /**
         * Convert $rowData ID numbers
         */
        $maskedId = $dataFunc->mask($rowData[0], null, strlen($rowData[0])-2);
        
        /**
         * Strip First/Last Names of unwanted characters
         */
        $wantedFirst = $dataFunc->removeChars($rowData[1]);
        $wantedLast = $dataFunc->removeChars($rowData[2]);

        /**
         * Calculate and add TERM data
         */
        $termData = $dataFunc->calcTerm($rowData[4]);

        /**
         * Build $outputArray 
         */
        array_push($outputArray, $maskedId . "\t", $wantedFirst . "\t", $wantedLast . "\t", $rowData[3] . "\t", $termData . "\n");
    }

    /**
     * Add header back into $outputArray
     */
    array_unshift($outputArray, "ID\t", "FIRST\t", "LAST\t", "TYPE\t", "EFFECTIVE\t", "TERM");

    /**
     * Sort and write output to open txt file
     */
    ksort($outputArray);
    file_put_contents($file, $outputArray);

    echo "\ntxt file manipulation and outputting complete";
?>