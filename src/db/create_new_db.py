# A script to create a new candidate database

import pymongo
from src import state

# Open MongoDB connection
mongo_client = pymongo.MongoClient()
# Drop old database
mongo_client.drop_database('candi')
# Create new database
candi = mongo_client.candi
candidates = candi.candidates
# Add candidates to database
def add(get_candidates):
    for candidate in get_candidates():
        candidates.insert_one(candidate.json)
add(get_candidates = state.get_ks_candidates)