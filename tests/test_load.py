from openpiv import imread
def test_load():
    """ Unit testing of correct loading of the image """
    assert imread('../test1/exp1_001_b.bmp')
    assert imread('../test2/exp1_001_c.bmp')
    
    # at least one failing test 
    assert imread('../test1/non_existing_image.bmp')
    