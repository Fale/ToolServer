<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Fale's ToolServer - @yield('title')</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="author" content="Fabio Alessandro Locati">
    <link href="//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css" rel="stylesheet">
    <style>
      body {
        padding-top: 60px;
      }
    </style>
  </head>
  <body>
    <div class="navbar navbar-inverse navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="/isbn2tpl/">ISBN2Tpl</a>
        </div>
        <div class="collapse navbar-collapse">
          <p class="navbar-text pull-right{{Request::is('/isbn2tpl/contact') ? ' active' : '' }}">
            {{ link_to('/isbn2tpl/contact', 'Contact', array(), array('class' => 'navbar-link')) }}
          </p>
          <ul class="nav navbar-nav">
            <li{{ Request::is('/isbn2tpl/check') ? ' class="active"' : '' }}>{{ link_to('/isbn2tpl/check', 'Check')}}<li>
            <li{{ Request::is('/isbn2tpl/cite*') ? ' class="active"' : '' }}>{{ link_to('/isb2tpl/cite', 'Cite Template')}}</li>
            <li{{ Request::is('/isbn2tpl/api*') ? ' class="active"' : '' }}>{{ link_to('/isbn2tpl/api', 'API')}}</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="container">
      @yield('content')
    </div> <!-- /container -->
    </body>
    <script src="//ajax.googleapis.com/ajax/libs/jquery/2.1.0/jquery.min.js"></script>
    <script src="//netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js"></script>
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
