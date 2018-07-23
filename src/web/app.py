import flask
import pymongo

# Create app
app = flask.Flask(__name__)

# Open MongoDB connection
mongo_client = pymongo.MongoClient()
candi = mongo_client.candi
candidates = candi.candidates

# Helpers
def json_candidates(cursor):
    '''Helper function to transform candidates MongoDB cursor into json'''
    json = []
    for candidate in cursor:
        del(candidate['_id'])
        json.append(candidate)
    return json

def get_query():
    query = {}
    query['state'] = flask.request.args.get('state', default = 'ALL')
    query['office'] = flask.request.args.get('office', default = 'ALL')
    query['party'] = flask.request.args.get('party', default = 'ALL')
    query = {key: value for key, value in query.items() if value != 'ALL'}
    return query

# Routes
@app.route('/')
def index():
    '''Index'''
    return flask.render_template('index.html')

@app.route('/explorer/')
def explorer():
    '''API explorer'''
    return flask.render_template('explorer.html')

# API
@app.route('/api/candidate/')
def get_candidates():
    '''Return all candidates for a given query'''
    return flask.jsonify(json_candidates(candidates.find(get_query())))

@app.route('/api/office/')
def get_offices():
    '''Returns all offices for a given query'''
    return flask.jsonify(candidates.distinct('office', query = get_query()))

@app.route('/api/party/')
def get_parties():
    '''Returns all parties for a given query'''
    return flask.jsonify(candidates.distinct('party', query = get_query()))

# Run
if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')
