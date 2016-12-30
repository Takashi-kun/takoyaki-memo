# -*- coding: utf-8 -*-

from flask import request
from flask_restful import Resource

from api_model import ApiModel

class ApiController(Resource):

    def __init__(self):
        self.api_model = ApiModel()

    def get(self, memo_id):
        response = self.api_model.api_get(memo_id)
        return response, response['code']

    def post(self, memo_id=None):
        json_data = request.get_json(force=True)
        response = self.api_model.api_post(memo_id, json_data['context'])
        return response, response['code']
