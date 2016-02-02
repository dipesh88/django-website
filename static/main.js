function set_sidebar(sidebar_item){
    switch (sidebar_item){
    case 'expenses':
        {$("#sidebar-expenses").addClass("active");
        $("#sidebar-balance").removeClass("active");
        $("#sidebar-settings").removeClass("active");}
        break;
    case 'balance':
        {$("#sidebar-expenses").removeClass("active");
        $("#sidebar-balance").addClass("active");
        $("#sidebar-settings").removeClass("active");}
        break;
    case 'settings':
        {$("#sidebar-expenses").removeClass("active");
        $("#sidebar-balance").removeClass("active");
        $("#sidebar-settings").addClass("active");}
        break;
    }
    }

function show_static_info(){

msg = "This alert is served from static files\n"
msg = msg + "=============================\n";
msg = msg + "Serving static js, css files:\n"
msg = msg + "Development: Web server django dev server, DEBUG=True. Files are served directly from the repository static directory by django (mysite/site_repo/static) \n";
msg = msg + "Production: Web server Nginx/Apache, DEBUG=False. Files are served from the static_root directory, by Nginx location alias. \n"
msg = msg + "Testing: Web server Nginx/Apache, DEBUG=True. Files are served from static_root with nginx, but with the original file name (instead of the hashed name which collectstatic adds) \n";
msg = msg + "See Readme"
alert(msg);
}

