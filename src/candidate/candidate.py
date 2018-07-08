class Candidate:
    def __init__(self, full_name = 'N/A', first_name = 'N/A', last_name = 'N/A', office = 'N/A', district = 'N/A', position = 'N/A', division = 'N/A',
        date_filed = 'N/A', party = 'N/A', home_address = 'N/A', mailing_address = 'N/A', home_phone = 'N/A', work_phone = 'N/A', cell_phone = 'N/A',
        email = 'N/A', website = 'N/A'):
        # Personal information
        self.full_name = full_name
        self.first_name = first_name
        self.last_name = last_name
        # Office
        self.office = office
        self.district = district
        self.position = position
        self.division = division
        self.date_filed = date_filed
        # Party affiliation
        self.party = party
        # Contact information
        self.home_address = home_address
        self.mailing_address = mailing_address
        self.home_phone = home_phone
        self.work_phone = work_phone
        self.cell_phone = cell_phone
        self.email = email
        self.website = website