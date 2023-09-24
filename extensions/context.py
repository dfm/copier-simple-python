# Copyright 2023 Dan Foreman-Mackey
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


import re
import unicodedata

import requests
from copier_templates_extensions import ContextHook


class GetLicense(ContextHook):
    def hook(self, context):
        license_name = context.get("copyright_license", None)
        if not license_name:
            return {}

        r = requests.get(f"https://api.github.com/licenses/{license_name}")
        r.raise_for_status()
        license = r.json().get("body", "")
        if not license:
            return {}

        return {"copyright_license_text": license}


class FormatProjectName(ContextHook):
    def hook(self, context):
        project_name = context.get("project_name", None)
        if not project_name:
            return {}

        return {"python_project_name": slugify(project_name)}


def slugify(value, allow_unicode=False):
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize("NFKC", value)
    else:
        value = (
            unicodedata.normalize("NFKD", value)
            .encode("ascii", "ignore")
            .decode("ascii")
        )
    value = re.sub(r"[^\w\s-]", "", value.lower())
    return re.sub(r"[-\s]+", "-", value).strip("-_")
