from os.path import isfile
import pytest
from src.state import ia

@pytest.mark.skip(reason = 'Primary 2018')
def test_pase_ia_sos_csv_primary_2018():
    '''To verify that candi candidates can be constructed from the IA Secretary of State website'''
    # Download pdf from the IA Secretary of State website
    ia.get_sos_dot_iowa_dot_gov_pdf()
    assert(isfile('temp/ia_temp.pdf'))
    # Convert the pdf to csv
    ia.convert_sos_dot_iowa_dot_gov_pdf()
    assert(isfile('temp/ia_temp.csv'))
    # Construct candidates
    candidates = ia.parse_sos_dot_iowa_dot_gov_csv()
    # Verify candidate with prepopulated office
    abby_finkenauer = candidates[1]
    assert(abby_finkenauer.full_name == 'Abby Finkenauer')
    assert(abby_finkenauer.first_name == 'Abby')
    assert(abby_finkenauer.last_name == 'Finkenauer')
    assert(abby_finkenauer.office == 'United States Representative')
    assert(abby_finkenauer.district == 1)
    assert(abby_finkenauer.date_filed == '3/13/2018')
    assert(abby_finkenauer.party == 'Democratic')
    assert(abby_finkenauer.mailing_address == 'PO Box 598, Dubuque, IA 52004')
    assert(abby_finkenauer.work_phone == '319-382-6671')
    assert(abby_finkenauer.email == 'abby@abbyfinkenauer.com')