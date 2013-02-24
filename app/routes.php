<?php

/*
|--------------------------------------------------------------------------
| Application Routes
|--------------------------------------------------------------------------
|
| Here is where you can register all of the routes for an application.
| It's a breeze. Simply tell Laravel the URIs it should respond to
| and give it the Closure to execute when that URI is requested.
|
*/

Route::get('/', function(){ return View::make('home');});
Route::get('contact', function(){ return View::make('contact');});

/** ISBN **/
Route::get('isbn/citaLibro', function(){ return View::make('isbn.citaLibro');});
Route::get('isbn/citaLibro/{isbn}', Array('uses' => 'IsbnController@isbn'));
Route::get('isbn/check/{isbn}', Array('uses' => 'IsbnController@checkIsbn'));
