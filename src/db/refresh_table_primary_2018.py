# A script to create a new candidate table for the 2018 primaries
import pymongo
from src import state
# Open MongoDB connection
mongo_client = pymongo.MongoClient()
# Drop old database
mongo_client.drop_database('candi')
# Create new database
candi = mongo_client.candi
primary_2018 = candi.primary_2018
# Add candidates to database
def add(get_candidates):
    for candidate in get_candidates():
        primary_2018.insert_one(candidate.json)
add(get_candidates = state.get_ks_candidates_primary_2018)
add(get_candidates = state.get_ia_candidates_primary_2018)