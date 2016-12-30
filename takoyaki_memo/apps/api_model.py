# -*- coding: utf-8 -*-

import hashlib
import time
from flask import current_app

## import model
from . import model_cloudsql

class ApiModel:

    def __init__(self):
        if current_app.config['DATA_BACKEND'] == 'cloudsql':
            self.model = model_cloudsql

    def api_get(self, memo_id):
        data = self.model.read(memo_id)
        if data is None:
            return {'body': {}, 'code': 404}

        response = {'body': {}, 'code': 200}
        for key in data:
            response['body'][key] = data[key]

        return response

    def api_post(self, memo_id, context):
        if not context:
            return {'body': {}, 'code': 400}

        if memo_id and self.model.read(memo_id) is not None:
            ## memo_id is already used
            return {'body': {}, 'code': 400}

        epoch = int(time.time())
        if not memo_id or memo_id == 'new':
            base = '%s%d' % (context, epoch)
            memo_id = hashlib.md5(base).hexdigest()

        data = {
            'id': memo_id,
            'text': context,
            'created_at': epoch
        }

        result = self.model.create(data)

        response = {'body': {}, 'code': 200}
        for key in result:
            response['body'][key] = result[key]

        return response


