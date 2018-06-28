from src.state.ks import get_kssos_dot_org_response
import bs4

def test_kssos_dot_org_response_url():
    '''To verify that the kssos.org candidate response is from the correct url. It has a nasty habit of
    redirecting to the kssos.org homepage if the request is off.'''
    url = get_kssos_dot_org_response().url
    assert(url == 'http://www.kssos.org/elections/elections_upcoming_candidate_display.asp')

def test_kssos_dot_org_response_table():
    '''To verify that the kssos.org candidate response has a table. If the request is off, the
    page will render without any actual candidates.'''
    content = get_kssos_dot_org_response().content
    soup = bs4.BeautifulSoup(content, 'html.parser')
    tables = soup.find_all('table')
    assert(len(tables) == 1)