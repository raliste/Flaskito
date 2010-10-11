from flask import Flask, render_template

from flaskito import views

DEBUG = False
SECRET_KEY = "secret"

def create_app(config=None):
    app = Flask(__name__)

    app.config.from_object(__name__)
    if config:
        app.config.from_object(config)
        
    # Configure logging here
    
    # Configure extensions
    
    # Error handlers
    
    if not app.debug:
        @app.errorhandler(404)
        def page_not_found(error):
            return render_template('404.html', error=error)
            
        @app.errorhandler(500)
        def server_error(error):
            return render_template('500.html', error=error)
            
    # Before and after handlers
    
    @app.before_request
    def before_request():
        pass
        
    @app.after_request
    def after_request(request):
        # Play with your request here
        return request
        
    # Register modules
    
    app.register_module(views.front, url_prefix='')
    
    return app
