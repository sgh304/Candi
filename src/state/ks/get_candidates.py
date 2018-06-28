import requests
import bs4

def get_kssos_dot_org_response():
    '''Gets the HTML response from the candidate listing page on the KS Secretary of State's website.'''
    url = 'http://www.kssos.org/elections/elections_upcoming_candidate_display.asp'
    # Referer header is necessary to get the listing page to load correctly
    headers = {'Referer': 'http://www.kssos.org/elections/elections_upcoming_candidate.asp'}
    # elecid can be set to different values. '25' is the ID for the 2018 Primaries
    # flag is necessary to get the listing page to load correctly
    data = {'elecid': '25', 'flag': 'yes'}
    return requests.post(url = url, headers = headers, data = data)

def get_ks_candidates():
    '''Parses the candidate listing page on the KS Secretary of State's website to construct a list of
    candidates using the standardized candi model.'''
    content = get_kssos_dot_org_response().content
    soup = bs4.BeautifulSoup(content, 'html.parser')
    tds = soup.find_all('td')
    names = [td.getText().strip() for td in tds[::25]]
    print(names)
    #print(tds[::10])

get_ks_candidates()