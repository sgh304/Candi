import flask
import pymongo

# Create app
app = flask.Flask(__name__)

# Open MongoDB connection
mongo_client = pymongo.MongoClient()
candi = mongo_client.candi
candidates = candi.candidates

# Test route
@app.route('/')
def index():
    return 'Hello world'

def json_candidates(cursor):
    '''Helper function to transform candidates MongoDB cursor into json'''
    json = []
    for candidate in cursor:
        del(candidate['_id'])
        json.append(candidate)
    return json

# State candidates
@app.route('/<state>/')
def state(state):
    state = state.upper()
    return flask.jsonify(json_candidates(candidates.find({'state': state})))

# Run
if __name__ == '__main__':
    app.run(debug = True)