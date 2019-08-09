from flask import Blueprint

analysis = Blueprint('analysis',
                    __name__,
                    template_folder='templates',
                    static_folder='static',
                    static_url_path='/smokeresearchweb/analysis')

from . import views
