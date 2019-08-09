from smokeresearch import create_app
import os


if __name__ == '__main__':
    app = create_app()
    app_context = app.app_context()
    app_context.push()

    app.run(host='0.0.0.0', port=5555)
