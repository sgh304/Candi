import bs4
import pytest
from src.state import ks

def test_kssos_dot_org_response_url():
    '''To verify that the kssos.org candidate response is from the correct url. It has a nasty habit of
    redirecting to the kssos.org homepage if the request is off.'''
    url = ks.get_kssos_dot_org_response().url
    assert(url == 'http://www.kssos.org/elections/elections_upcoming_candidate_display.asp')

def test_kssos_dot_org_response_table():
    '''To verify that the kssos.org candidate response has a table. If the request is off, the
    page will render without any actual candidates.'''
    content = ks.get_kssos_dot_org_response().content
    soup = bs4.BeautifulSoup(content, 'html.parser')
    tables = soup.find_all('table')
    assert(len(tables) == 1)

@pytest.mark.skip(reason = 'Primary 2018')
def test_get_ks_candidates_primary_2018():
    '''To verify that Candidates are properly constructed from the kssos.org website's table.'''
    candidates = ks.get_ks_candidates_primary_2018()
    # Verify standard candidate
    vernon_j_fields = candidates[4]
    assert(vernon_j_fields.full_name == 'Vernon J. Fields')
    assert(vernon_j_fields.first_name == 'Vernon')
    assert(vernon_j_fields.last_name == 'Fields')
    # Verify a standardized office
    assert(vernon_j_fields.office == 'United States Representative')
    assert(vernon_j_fields.district == '2')
    assert(vernon_j_fields.date_filed == '2/14/2017')
    assert(vernon_j_fields.party == 'Republican')
    assert(vernon_j_fields.home_address == '15424 Pin Oak Drive, Basehor, KS, 66007')
    assert(vernon_j_fields.mailing_address == '1106 North 155th Street, Ste A, Basehor, KS, 66007')
    assert(vernon_j_fields.work_phone == '(800) 401-2395')
    assert(vernon_j_fields.email == 'info@vernonjfields.com')
    assert(vernon_j_fields.website == 'vernonjfields.com')
    # Verify candidate running for an office where district is irrelevant
    arden_andersen = candidates[24]
    assert(arden_andersen.full_name == 'Arden Andersen  / Dale Cowsert')
    assert(arden_andersen.district == 'N/A')
    # Verify candidate without home address or mailing address properly constructed
    doug_mays = candidates[7]
    assert(doug_mays.full_name == 'Doug Mays')
    assert(doug_mays.home_address == 'N/A')
    assert(doug_mays.mailing_address == 'N/A')
    # Verify candidate without phone numbers, email, or web address
    roger_marshall = candidates[1]
    assert(roger_marshall.full_name == 'Roger Marshall')
    assert(roger_marshall.home_phone == 'N/A')
    assert(roger_marshall.work_phone == 'N/A')
    assert(roger_marshall.cell_phone == 'N/A')
    assert(roger_marshall.email == 'N/A')
    assert(roger_marshall.website == 'N/A')