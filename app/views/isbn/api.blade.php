@extends('layouts.default')

@section('title')Cite boot @stop

@section('content')
    <h1>ISBN API doc</h1>
        All the functions that can be used with a browser, can be used with APIs.
        <h3>ISBN Existance</h3>
            To check if some ISBN code is valid, is enough querying the /~fale/isbn/check/<i>[ISBN NUMBER]</i>.
            <h4>Results</h4>
                <ul>
                    <li><b>0</b>: ISBN is not registered or invalid</li>
                    <li><b>1</b>: ISBN is valid (but it can be another book ISBN)</li>
                </ul>
        <h3>Templating</h3>
            To obtain the template for some ISBN code, is enough querying the /~fale/isbn/cite/<i>[PROJECT]</i>/<i>[ISBN NUMBER]</i>.
            <h4>Supported projects</h4>
                At the moment only the following values are supported for the <i>[PROJECT]</i> field:
                <ul>
                    <li><b>itwiki</b> for <a href="http://it.wikipedia.org">it.wikipedia.org</a></li>
                    <li><b>enwiki</b> for <a href="http://en.wikipedia.org">en.wikipedia.org</a></li>
                </ul>
            <h4>Results</h4>
                The template in plain-text will be returned.
            <h4>Errors</h4>
                At this time, if no ISBN code has been found, the response will be <b>empty</b>.
@stop
