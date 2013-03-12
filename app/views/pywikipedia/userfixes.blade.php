@extends('layouts.default')

@section('title')PyWikipedia - User Fixes - {{$file}} @stop

@section('content')
    <h1>User Fixes - {{$file}}</h1>
        <?php
            $source = file_get_contents(base_path() . "/pywikipedia/user-fixes/" . $file . ".py");
            $geshi = new GeSHi($source, 'python');
            echo $geshi->parse_code();
        ?>
@stop
