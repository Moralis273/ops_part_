from model import predict_probability

def test_predict_probability():
    probability=predict_probability(40,300)
    assert isinstance(probability,float)
    assert 0<=probability<=1
    
