from openpiv.tools import imread

def test_load():
    """ Unit testing of correct loading of the image """
    _ = imread('./test1/exp1_001_b.bmp')
    assert _[0,0] == 8
    
    im2 = imread('./test1/exp1_001_c.bmp')
    assert im2.shape == (369,511)
    
    # at least one failing test 
    try:
        _ = imread('test1/non_existing_image.bmp')
    except FileNotFoundError:
        print('correct testing of a non existing file')   
    