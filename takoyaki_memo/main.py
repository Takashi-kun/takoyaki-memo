# -*- coding: utf-8 -*-

import apps
import config

app = apps.create_app(config)

# This is only used when running locally. When running live, gunicorn runs
# the application.
if __name__ == '__main__':
    app.run(host='192.168.50.12', port=8080, debug=True)
