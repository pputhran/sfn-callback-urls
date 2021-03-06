# Copyright 2019 Ben Kehoe
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

class BaseError(Exception):
    TYPE = 'GenericError'
    
    def __init__(self, message):
        self._message = message

    def code(self):
        return self.__class__.__name__
    
    def message(self):
        return self._message

    def __str__(self):
        return f'{self.code()}:{self.message()}'

class RequestError(BaseError):
    TYPE = 'RequestError'

class ParametersDisabledError(RequestError):
    pass

class OutputFormattingError(RequestError):
    pass

class InvalidPayloadError(RequestError):
    pass

class ExpiredPayloadError(RequestError):
    pass

class EncryptionError(RequestError):
    pass

class DecryptionUnsupportedError(RequestError):
    pass

class EncryptionRequiredError(RequestError):
    pass

class MissingApiParametersError(RequestError):
    pass

class InvalidActionError(RequestError):
    pass

class InvalidDateError(RequestError):
    pass

class ActionMismatchedError(RequestError):
    pass

class StepFunctionsError(BaseError):
    TYPE = 'StepFunctionsError'
