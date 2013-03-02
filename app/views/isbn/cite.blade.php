@extends('layouts.default')

@section('title')Cite boot @stop

@section('content')
    <h1>Welcome to Fale's Cite book tool</h1>
    <form>
        <fieldset>
            <div class="input-prepend input-append">
                <select id="project" class="span2">
                    <option>itwiki</option>
                </select>
                <input class="span2" id="isbn" type="text" placeholder="ISBN">
                <div class="btn-group">
                    <button class="btn" id="submit" type="button">Create!</button>
                </div>
            </div>
        </fieldset>
    </form>
    <div id="result"></div>

    <script type="text/javascript">
        $(document).ready(function() {
            $("#submit").click(function(){
                var isbn = $("#isbn").val();
                var proj = $("#project").val();
                var result = document.getElementById('result');
                $.ajax({
                    type: "GET",
                    url: "/~fale/isbn/cite/" + proj + "/" + isbn,
                    dataType: "html",
                    success: function(msg)
                    {
                        if (msg == ""){
                            $("#result").html("ISBN code does not exist");
                            result.className = 'alert alert-error';
                        }else{
                            $("#result").html(msg);
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
