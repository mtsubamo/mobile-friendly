from googleapiclient.discovery import build

def get_search(st, ak, cx, sc):
  service = build("customsearch", "v1",
          developerKey=ak)

  domain = []
  for _c in range(sc):
    # The number of search results at one time is 10
    start = _c * 10
    res = service.cse().list(
        q=st,
        cx=cx,
        start=start+1
      ).execute()

    if not 'items' in res:
      break
    for _i in res['items']:
      # Maybe it might be different key
      d = _i['formattedUrl']
      if not d in domain:
        domain.append(d)

  return domain
