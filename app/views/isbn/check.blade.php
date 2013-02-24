@extends('layouts.default')

@section('title')Check ISBN @stop

@section('content')
    <h1>Welcome to Fale's Cita libro tool</h1>
    <form>
        <fieldset>
            <div class="input-append">
                <input class="span2" id="isbn" type="text" placeholder="ISBN">
                <button class="btn" id="submit" type="button">Create!</button>
            </div>
        </fieldset>
    </form>
    <div id="result"></div>

    <script type="text/javascript">
        $(document).ready(function() {
            $("#submit").click(function(){
                var isbn = $("#isbn").val();
                var result = document.getElementById('result');
                $.ajax({
                    type: "GET",
                    url: "/~fale/isbn/check/" + isbn,
                    dataType: "html",
                    success: function(msg)
                    {
                        if (msg == 0){
                            $("#result").html("ISBN code does not exist");
                            result.className = 'alert alert-error';
                        }else{
                            $("#result").html("ISBN code is valid");
                            result.className = 'alert alert-success';
                        }
                    },
                    error: function()
                    {
                        $("#result").html("Google Books not avilable");
                        result.className = 'alert alert-error';
                    }
                });
            });
        });
    </script>
@stop
