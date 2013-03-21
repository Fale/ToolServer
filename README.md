ToolServer
==========

Code of my ToolServer publichtml zone, pywikipedia rules and SGE commands to execute the pywikipedia rules

License
-------
All data in this repository are under the [AGPLv3 license](http://www.gnu.org/licenses/agpl-3.0.html)

Installation
------------
    git clone https://github.com/Fale/ToolServer.git
    cd ToolServer
    php composer.phar install
    cp -r app/config-demo/ app/config/
    php artisan key:generate
    chmod 775 app/storage
    chmod 700 app/config
