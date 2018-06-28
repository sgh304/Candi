from src.candidate import Candidate

def test_candidate_creation():
    candidate = Candidate(first_name = 'Barack', last_name = 'Obama')
    assert(candidate.first_name == 'Barack')
    assert(candidate.last_name == 'Obama')