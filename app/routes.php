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
Route::get('isbn/api', function(){ return View::make('isbn.api');});
Route::get('isbn/citaLibro', function(){ return Redirect::to('isbn/cite?project=itwiki');});
Route::get('isbn/citaLibro/{isbn}', function($isbn){ return Redirect::to("isbn/cite/itwiki/$isbn");});
Route::get('isbn/cite', function(){ return View::make('isbn.cite');});
Route::get('isbn/cite/{project}/{isbn}', Array('uses' => 'IsbnController@cite'));
Route::get('isbn/check', function(){ return View::make('isbn.check');});
Route::get('isbn/check/{isbn}', Array('uses' => 'IsbnController@checkIsbn'));

/** PyWikipedia **/
Route::get('pywikipedia/user-fixes', function(){ return View::make('pywikipedia.userfixes');});
