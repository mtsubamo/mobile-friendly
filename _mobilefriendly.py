"""Example of Python client calling Search Console URL Testing Tools API."""
import urllib
import urllib.request, urllib.error
import time
import json

def _get_result(url, data):
  try:
    result = urllib.request.urlopen(url=url, data=data).read()
    return result
  except:
    return None

def friendly_result(key, url):
  request_url = 'http://www.google.com/'
  service_url = 'https://searchconsole.googleapis.com/v1/urlTestingTools/mobileFriendlyTest:run'
  params = {
      'url': url,
      'key': key,
  }
  data = urllib.parse.urlencode(params).encode("utf-8")
  result = _get_result(service_url, data)

  if result == None:
    print('------ debug --------')
    print('mobilefriendly api error, url: %s' % url)
    print('---------------------')
    return None
  d_content = result.decode("utf-8")
  return json.loads(d_content)
