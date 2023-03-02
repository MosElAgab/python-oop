from src.high_scores import HighScoreTable

def test_returns_scores_list_and_a_limit():
    expected = []
    result = HighScoreTable(3)
    print(f'result => {result.scores}')
    assert expected == result.scores

    expected = 3
    result = HighScoreTable(3)
    print(f'result => {result.limit}')
    assert expected == result.limit

def test_returns_an_updated_scores_list():
    high_scores = HighScoreTable(3)
    high_scores.update({'player':'Cat', 'score':95})

    expected = [{'player':'Cat', 'score':95}]
    result = high_scores.scores
    print(f'result => {result}')
    assert expected == result

    high_scores.update({'player':'Verity', 'score':150})
    expected = [{'player':'Cat', 'score':95}, {'player':'Verity', 'score':150}]
    result = high_scores.scores
    print(f'result => {result}')
    assert expected == result

def test_updates_the_score_list_upto_the_limit():
    high_scores = HighScoreTable(2)
    high_scores.update({'player':'Cat', 'score':95})
    high_scores.update({'player':'Verity', 'score':150})
    high_scores.update({'player':'James', 'score':20})
    expected = [{'player':'Cat', 'score':95}, {'player':'Verity', 'score':150}]
    
    result = high_scores.scores
    print(f'result => {result}')
    assert expected == result

def test_updates_the_score_list_with_the_higher_score_player():
    high_scores = HighScoreTable(2)
    high_scores.update({'player':'Cat', 'score':95})
    high_scores.update({'player':'Verity', 'score':150})
    high_scores.update({'player':'James', 'score':20})
    high_scores.update({'player':'Dan', 'score':250})

    expected = {'player':'Dan', 'score':250}    
    result = high_scores.scores
    assert expected in result

    # expected = [{'player':'Dan', 'score':250}, {'player':'Verity', 'score':150}]
    # print(f'result => {result}')
    # assert expected == result

def test_updates_the_score_list_with_the_higher_score_player():
    high_scores = HighScoreTable(2)
    high_scores.update({'player':'Cat', 'score':95})
    high_scores.update({'player':'Verity', 'score':150})
    high_scores.update({'player':'James', 'score':20})
    high_scores.update({'player':'Dan', 'score':250})

    expected = {'player':'Dan', 'score':250}    
    result = high_scores.scores
    assert expected in result

def test_works_out_the_average_of_highest_scores():
    high_scores = HighScoreTable(2)
    high_scores.update({'player':'Cat', 'score':95})
    high_scores.update({'player':'Verity', 'score':150})
    high_scores.update({'player':'James', 'score':20})
    high_scores.update({'player':'Dan', 'score':250})

    expected = 200 
    result = high_scores.average_score()
    assert expected == result

def test_returns_a_dictionary_of_the_highest_scorer():
    high_scores = HighScoreTable(2)
    high_scores.update({'player':'Cat', 'score':95})
    high_scores.update({'player':'Verity', 'score':150})
    high_scores.update({'player':'James', 'score':20})
    high_scores.update({'player':'Dan', 'score':250})

    expected = {'player':'Dan', 'score':250} 
    result = high_scores.highest_scorer()
    assert expected == result

def test_removes_all_the_scores_from_the_list_returns_and_empty_list():
    high_scores = HighScoreTable(2)
    high_scores.update({'player':'Cat', 'score':95})
    high_scores.update({'player':'Verity', 'score':150})
    high_scores.update({'player':'James', 'score':20})
    high_scores.update({'player':'Dan', 'score':250})
    high_scores.reset()

    expected = [] 
    result = high_scores.scores
    assert expected == result