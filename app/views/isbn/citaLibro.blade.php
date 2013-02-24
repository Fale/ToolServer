@extends('layouts.default')

@section('title')Cita libro @stop

@section('content')
    <h1>Welcome to Fale's Cita libro tool</h1>
    <form name="module">
        <p>ISBN</p>
        <p><input type="text" name="isbn" id="isbn"></p>
        <input type="button" id="submit" value="Send">
    </form>
    <div id="result"></div>

    <script type="text/javascript">
        $(document).ready(function() {
            $("#submit").click(function(){
                var isbn = $("#isbn").val();
                var result = document.getElementById('result');
                $.ajax({
                    type: "GET",
                    url: "/~fale/isbn/citaLibro/" + isbn,
                    dataType: "html",
                    success: function(msg)
                    {
                        $("#result").html(msg);
                        result.className = 'alert alert-success';
                    },
                    error: function()
                    {
                        $("#result").html("Error, ISBN code not valid");
                        result.className = 'alert alert-error';
                    }
                });
            });
        });
    </script>
@stop
