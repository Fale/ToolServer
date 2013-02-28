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
Route::get('isbn/citaLibro/{isbn}', Array('uses' => 'IsbnController@itwiki'));
//Route::get('isbn/cite', function(){ return View::make('isbn.citaLibro');});
Route::get('isbn/cite/{project}/{isbn}', Array('uses' => 'IsbnController@cite'));
Route::get('isbn/check', function(){ return View::make('isbn.check');});
Route::get('isbn/check/{isbn}', Array('uses' => 'IsbnController@checkIsbn'));
