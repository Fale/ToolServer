@extends('layouts.default')

@section('title')Cite boot @stop

@section('content')
    <h1>ISBN API doc</h1>
        All the functions that can be used with a browser, can be used with APIs.
        <h3>ISBN Existance</h3>
            To check if some ISBN code is valid, is enough querying the /~fale/isbn/check/[ISBN NUMBER].
            <h4>Results</h4>
                <ul>
                    <li><b>0</b>: ISBN is not registered or invalid</li>
                    <li><b>1</b>: ISBN is valid (but it can be another book ISBN)</li>
                </ul>
        <h3>Templating</h3>
            To obtein the template for some ISBN code, is enough querying the /~fale/isbn/cite/[PROJECT]/[ISBN NUMBER].
            <h4>Results</h4>
                The template in plain-text will be returned.
@stop
