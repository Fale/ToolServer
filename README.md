ToolServer
==========

Code of my ToolServer public_html zone

== Installation ==
    git clone https://github.com/Fale/ToolServer.git
    cd ToolServer
    curl -sS https://getcomposer.org/installer | php
    php composer.phar install
    cp -r app/config-demo/ app/config/
    php artisan key:generate
    chmod 775 app/storage
    chmod 700 app/config
