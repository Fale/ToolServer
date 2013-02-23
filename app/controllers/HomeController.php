<?php
class HomeController extends BaseController {
    public $layout = 'layouts.default';
    public function index()
    {
        $this->layout->title = 'title';
        $this->layout->content = 'home';
    }
}
