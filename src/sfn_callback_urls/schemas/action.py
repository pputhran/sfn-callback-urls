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

response_schema = {
    "type": "object",
    "properties": {
        "json": {
            "type": "object"
        },
        "html": {
            "type": "string"
        },
        "text": {
            "type": "string"
        },
        "redirect": {
            "type": "string",
            "format": "uri"
        }
    }
}

schema = {
    "type": "object",
    "properties": {
        "type": {
            "type": "string",
            "enum": ["success", "failure", "heartbeat"]
        },
        "response": response_schema
    },
    "required": ["type"],
    "allOf": [
        {
            "if": {
                "properties": { "type": { "const": "success" } }
            },
            "then": {
                "properties": {
                    "output": {}
                },
                "required": ["output"]
            }
            
        },
        {
            "if": {
                "properties": { "type": { "const": "failure" } }
            },
            "then": {
                "properties": {
                    "error": {
                        "type": "string"
                    },
                    "cause": {
                        "type": "string"
                    }
                }
            }
        }
    ]
}
