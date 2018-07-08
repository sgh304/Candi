from src.state.ks import get_ks_candidates
from datetime import datetime

state = input('Enter state to get a candidate backup for: ')

if state == 'ks':
    with open('backup/ks.txt', 'w') as backup:
        backup.write('# KS backup created at ' + str(datetime.today()) + '\n')
        backup.write(str([candidate.__dict__ for candidate in get_ks_candidates()]))