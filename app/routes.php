<?php

Route::group(array('prefix' => 'isbn2tpl'), function()
{

    Route::get('/', array(
        'as' => 'home',
        function(){ return View::make('home');}
    ));

    Route::get('api', array(
        'as' => 'api',
        function(){ return View::make('api');}
    ));

    Route::get('cite', array(
        'as' => 'cite',
        function(){ return View::make('cite');}
    ));

    Route::get('cite/{project}/{isbn}', array(
        'uses' => 'IsbnController@cite'
    ));

    Route::get('check', array(
        'as' => 'check',
        function(){ return View::make('check');}
    ));

    Route::get('check/{isbn}', array(
        'uses' => 'IsbnController@checkIsbn'
    ));

    Route::get('contact', array(
        'as' => 'contact',
        function(){ return View::make('contact');}
    ));

});
