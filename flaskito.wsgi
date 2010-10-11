import sys
import os

BASE_DIR = os.path.join(os.path_dirname(__file__))
sys.path.append(BASE_DIR)

try:
    import production_settings
except ImportError:
    raise Exception('Production settings file not found.')
    
    from flaskito import create_app
    
    application = create_app(production_settings)
