# Copyright 2019 MISHMASH I O OOD
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import os
import time
import json

import jwt


class MishmashWrongCredentialsException(Exception):
    pass


class MishmashUnauthorizedException(Exception):
    pass


class MishmashAuth():


    def __init__(self, mishmash_api_endpoint="mishmash-server"):

        config_data = self.get_configuration()

        self.__private_key = config_data["private_key"]
        self.__private_key_id = config_data["private_key_id"]
        self.__client_email = config_data["client_email"]
        self.__client_id = config_data["client_id"]

        self.__api_endpoint = mishmash_api_endpoint

        self.__bearer_token = None

    def signed_token(self):

        iat = time.time()
        exp = iat + 6 #0 * 60  # signed_token is valid 1 hour

        headers = {
            'kid': self.__private_key_id
        }

        payload = {
            'iss': self.__client_email,
            'sub': self.__client_email,
            'aud': self.__api_endpoint,
            'iat': iat,
            'exp': exp
        }

        return jwt.encode(payload,
                          self.__private_key,
                          headers=headers,
                          algorithm='RS256')

    def get_configuration(self):
        config_file_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")

        if not config_file_path:
            raise MishmashWrongCredentialsException("please set GOOGLE_APPLICATION_CREDENTIALS")

        with open(config_file_path, "r") as f:
            return json.load(f)

    def is_bearer_token_expired(self):
        try:
            decode_token = jwt.decode(self.__bearer_token, options={
                                      "verify_signature": False})
        except:
            raise MishmashWrongCredentialsException

        if decode_token["exp"] - time.time() < 0:
            return True

        return False

    def get_or_create_bearer_token(self):

        if self.__bearer_token is None:
            self.__bearer_token = self.signed_token()
            return self.__bearer_token

        if self.is_bearer_token_expired():
            self.__bearer_token = self.signed_token()
            return self.__bearer_token

        return self.__bearer_token

    @property
    def authorization_header(self):
        return f"Bearer {self.bearer_token}"

    @property
    def bearer_token(self):
     
        bearer_token = self.get_or_create_bearer_token()

        if not bearer_token:
            raise MishmashUnauthorizedException("invalid bearer token")
            
        return bearer_token

    @property
    def app_id(self):
        return self.__client_id