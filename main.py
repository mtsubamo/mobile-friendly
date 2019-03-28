#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Simple command-line example for Custom Search.

Command-line application that does a search.
"""

__author__ = 'jcgregorio@google.com (Joe Gregorio)'

import pprint
import sys
import json
import time
import _mobilefriendly
import _search

def config(path):
  json_file = open(path, 'r')
  return json.load(json_file)

def main(c, st):
  # Build a service object for interacting with the API. Visit
  # the Google APIs Console <http://code.google.com/apis/console>
  # to get an API key for your own application.
  ak = c['apiKey']
  cx = c['cx']
  sn = c['searchNum']
  sc = int(sn/10)

  domain = _search.get_search(st, ak, cx, sc)
  time.sleep(5)

  for url in domain:
    result = _mobilefriendly.friendly_result(ak, url)
    time.sleep(10)

    if result == None:
      continue
    if result['testStatus']['status'] != 'COMPLETE':
      continue

    print(url)
    print(result)
    print('')

if __name__ == '__main__':
  c = config("./config.json")
  st = ' '.join(sys.argv[1:])

  main(c, st)
