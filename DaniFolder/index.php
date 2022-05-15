<?php

    // Append the requested resource location to the URL
    $url = $_SERVER['REQUEST_URI'];
    $aux2 = $_SERVER['HTTP_HOST'];
    $aux = $_SERVER['QUERY_STRING'];
    echo $aux2;
    $array = array();
    //$url = "somepage?id=123&lang=gr&size=300";
    parse_str( parse_url( $url, PHP_URL_QUERY), $array );
    print_r( $array );
?>
