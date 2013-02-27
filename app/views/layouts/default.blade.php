<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Fale's ToolServer - @yield('title')</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="author" content="Fabio Alessandro Locati">
    <link rel="stylesheet" type="text/css" href="{{ path('bootstrap/css/bootstrap.min.css') }}" />
    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
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
          <a class="brand" href="/~fale">Fale's Tools</a>
          <div class="nav-collapse collapse">
            <p class="navbar-text pull-right {{{ Request::is('/~fale/contact') ? ' active' : '' }}}">
              <a href="/~fale/contact" class="navbar-link">Contact</a>
            </p>
            <ul class="nav">
              <li class="dropdown">
                <a href="#" class="dropdown-toggle {{{ Request::is('~fale/isbn*') ? ' active' : '' }}}" data-toggle="dropdown">ISBN<b class="caret"></b></a>
                <ul class="dropdown-menu">
                  <li class="{{{ Request::is('~fale/isbn/check') ? ' class="active"' : '' }}}"><a href="/~fale/isbn/check">Check</a></li>
                  <li class="{{{ Request::is('~fale/isbn/citaLibro*') ? ' class="active"' : '' }}}"><a href="/~fale/isbn/citaLibro">Cita libro</a></li>
                </ul>
              </li>
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
    <script type="text/javascript" src="{{ path('bootstrap/js/bootstrap.min.js') }}"></script>
    <script type="text/javascript">

        var _gaq = _gaq || [];
            _gaq.push(['_setAccount', 'UA-38831639-1']);
            _gaq.push(['_trackPageview']);

        (function() {
            var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
                ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
            var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
        })();
    </script>
</html>
