from csv import reader
from requests import get
from tabula import convert_into
from os import mkdir, rmdir
from src.candidate import Candidate

def get_sos_dot_iowa_dot_gov_pdf():
    '''Fetches the pdf with candidates from the IA Secretary of State's website'''
    with get('https://sos.iowa.gov/elections/pdf/candidates/primarycandidatelist.pdf', stream = True) as response:
        with open('temp/ia_temp.pdf', 'wb') as f:
            for chunk in response.iter_content(chunk_size = 1024):
                f.write(chunk)

def convert_sos_dot_iowa_dot_gov_pdf():
    '''Converts the pdf with candidates from the IA Secretary of State's website to csv'''
    convert_into('temp/ia_temp.pdf', 'temp/ia_temp.csv', output_format = 'csv', pages = 'all', stream = True, silent = True)

def parse_sos_dot_iowa_dot_gov_csv():
    '''Parses the csv of IA candidates into a list of candidates using the standardized candi model'''
    candidates = []
    with open('temp/ia_temp.csv', 'r') as f:
        rows = list(reader(f))
        for row in rows:
            # Clean row (fixing tabula-py conversion errors I think)
            row = [row[0]]  + [col for col in row[1:] if col != '']
            # Skip header rows
            if 'For the Office Of...' in row:
                continue
            # Skip no candidate rows
            if 'No Candidate' in row:
                continue
            # Skip weird formatting errors
            if len(row) == 1:
                continue
            # Personal information
            full_name = row[2]
            first_name = full_name.split(' ')[0]
            last_name = full_name.split(' ')[-1]
            # Office
            state = 'IA'
            office = row[0]
            # If office is blank, then fill in from above row
            if office == '':
                office = candidates[-1].office
                district = candidates[-1].district
            # Record districts for applicable offices
            elif 'District' in office.split(' '):
                district = int(office.split(' ')[-1])
                generalized_office = ' '.join(office.split(' ')[:office.split(' ').index('District')])
                office = generalized_office
            else:
                district = 'N/A'
            date_filed = row[6]
            # Party affiliation
            party = row[1]
            # Contact information
            mailing_address = row[3]
            work_phone = row[4]
            email = row[5]
            # Clean email for candidates who didn't provide
            if email == 'Did not provide':
                email = 'N/A'
            # Construct Candidate
            candidates.append(Candidate(full_name = full_name, first_name = first_name, last_name = last_name,
                                        state = state, office = office, district = district, date_filed = date_filed,
                                        party = party, mailing_address = mailing_address, work_phone = work_phone,
                                        email = email))
    return candidates

def get_ia_candidates():
    '''Fetches candidate pdf from the IA Secretary of State's website and parses that
    into a list of candi candidates.'''
    get_sos_dot_iowa_dot_gov_pdf()
    convert_sos_dot_iowa_dot_gov_pdf()
    return parse_sos_dot_iowa_dot_gov_csv()
