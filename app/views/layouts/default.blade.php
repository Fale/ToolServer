<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Fale's ToolServer - @yield('title')</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="author" content="Fabio Alessandro Locati">
    <link rel="stylesheet" type="text/css" href="{{ path('bootstrap/css/bootstrap.min.css') }}" />
    <style>
      body {
        padding-top: 60px;
      }
    </style>
  </head>
  <body>
    <div class="navbar navbar-inverse navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          <button type="button" class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="brand" href="#">@yield('title')</a>
          <div class="nav-collapse collapse">
            <ul class="nav">
              <li class="active"><a href="#">Home</a></li>
              <li><a href="#about">About</a></li>
              <li><a href="#contact">Contact</a></li>
            </ul>
          </div><!--/.nav-collapse -->
        </div>
      </div>
    </div>
    <div class="container">
      @yield('content')
    </div> <!-- /container -->
        <a href="https://github.com/fale/ToolServer">
            <img style="position: absolute; top:41px; right: 0; border: 0;" 
                 src="https://s3.amazonaws.com/github/ribbons/forkme_right_red_aa0000.png"
                 alt="Fork me on GitHub" />
        </a>
    </body>
</html>
