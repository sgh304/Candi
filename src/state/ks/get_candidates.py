from bs4 import BeautifulSoup
from requests import post
from src.candidate import Candidate

def get_kssos_dot_org_response():
    '''Gets the HTML response from the candidate listing page on the KS Secretary of State's website.'''
    url = 'http://www.kssos.org/elections/elections_upcoming_candidate_display.asp'
    # Referer header is necessary to get the listing page to load correctly
    headers = {'Referer': 'http://www.kssos.org/elections/elections_upcoming_candidate.asp'}
    # elecid can be set to different values. '25' is the ID for the 2018 Primaries
    # flag is necessary to get the listing page to load correctly
    data = {'elecid': '25', 'flag': 'yes'}
    return post(url = url, headers = headers, data = data)

def get_ks_candidates():
    '''Parses the candidate listing page on the KS Secretary of State's website to construct a list of
    candidates using the standardized candi model.'''
    # Get table from the KS Secretary of State's website and parse it into a list of rows with stripped strings
    content = get_kssos_dot_org_response().content
    soup = BeautifulSoup(content, 'html.parser')
    tds = soup.find_all('td')
    rows = [tds[i:i+25] for i in range(0, len(tds), 25)]
    cleaned_rows = [[col.getText().strip() for col in row] for row in rows]
    # Convert each row into a Candidate object
    candidates = []
    for row in cleaned_rows:
        def get(col, error = '', default = 'N/A'):
            '''Returns the data at a cleaned row, unless the data is equal to error, in which case default
            is returned.'''
            data = row[col]
            if data == error:
                return default
            return data
        # Personal information
        full_name = get(col = 0)
        first_name = get(col = 7)
        last_name = get(col = 9)
        # Office
        state = 'KS'
        office = get(col = 1)
        district = get(col = 2, error = '0')
        position = get(col = 3, error = '0')
        division = get(col = 4, error = '0')
        date_filed = get(col = 22)
        # Party affiliation
        party = get(col = 5)
        # Contact information
        home_address = get(col = 11)
        if home_address != 'N/A':
            # Add state and zip to home address
            home_address += ', ' + get(col = 12) + ', KS, ' + get(col = 13)
        mailing_address = get(col = 14)
        if mailing_address != 'N/A':
            # Add state and zip to mailing address
            mailing_address += ', ' + get(col = 15) + ', KS, ' + get(col = 16)
        home_phone = get(col = 17, error = '(000) 000-0000')
        work_phone = get(col = 18, error = '(000) 000-0000')
        cell_phone = get(col = 19, error = '(000) 000-0000')
        email = get(col = 20)
        website = get(col = 21)
        # Construct Candidate
        candidate = Candidate(full_name = full_name, first_name = first_name, last_name = last_name, state = state,
            office = office, district = district, position = position, division = division, date_filed = date_filed,
            party = party, home_address = home_address, mailing_address = mailing_address, home_phone = home_phone,
            work_phone = work_phone, cell_phone = cell_phone, email = email, website = website)
        candidates.append(candidate)
    return candidates