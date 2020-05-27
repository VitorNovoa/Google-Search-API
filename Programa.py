from googleapiclient.discovery import build
import pprint

my_api_key = "AIzaSyBMdqtYmoGUKG7CAAesoA2uf44xXniaBuI"
my_cse_id = "003648109669665253691:n8owgmggnj3"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

results = google_search('estou com sono', my_api_key, my_cse_id, num=2)

for resultado in results:
    '''pprint.pprint(result)'''

    titulo = resultado['title']
    link = resultado['formattedUrl']
    descricao = resultado['snippet']
    print (titulo)
    print (link)
    print (descricao)



''' pip install google-api-python-client '''