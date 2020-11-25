from wave_editor import *

def test_flip():
    assert flip_data([[1,2],[0,1],[-5,5]])== [[-5,5],[0,1],[1,2]]
    assert flip_data([[]]) == [[]]
    assert flip_data([[1,2]]) == [[1,2]]


def test_negate():
    assert negate_data([[1,2],[0,1],[-5,5]])== [[-1,-2],[0,-1],[5,-5]]
    assert negate_data([[-32768,32767],[0,0]])== [[32767,-32767],[0,0]]
    assert negate_data([[32767,-32768],[0,0]])== [[-32767,32767],[0,0]]
    assert negate_data([[]]) == [[]]
    assert negate_data([[1,2]]) == [[-1,-2]]
    assert negate_data([[1,2],[2,3],[3,4],[4,5]]) == [[-1,-2],[-2,-3],[-3,-4],[-4,-5]]
    assert negate_data([[-1,2],[2,-3],[-3,4],[-4,-5]]) == [[1,-2],[-2,3],[3,-4],[4,5]]
    assert negate_data([[-1,-2],[-2,-3],[-3,-4],[-4,-5]]) == [[1,2],[2,3],[3,4],[4,5]]


def test_speed_up():
    assert speed_up_data([[1,2],[0,1],[-5,5]])== [[1,2],[-5,5]]
    assert speed_up_data([[1,2],[-5,5]])== [[1,2]]
    assert speed_up_data([[1,2],[-5,5],[0,0],[-32767,32767]])== [[1,2],[0,0]]
    assert speed_up_data([[]]) == [[]]
    assert speed_up_data([[1,2]]) == [[1,2]]
    assert speed_up_data([[1,1],[2,2],[3,3],[4,4],[5,5]]) == [[1,1],[3,3],[5,5]]

def test_pairs_average():
    assert pairs_average([[1,2],[0,1],[-5,5]],0) == [0,1]
    assert pairs_average([[1,2],[0,2],[-5,5]],0) == [0,2]
    assert pairs_average([[0,0],[0,2],[-5,5]],0) == [0,1]
    assert pairs_average([[0,0],[0,2],[-5,5],[-2,0],[0,2],[-5,5]],1) == [-2,3]
def test_speed_down_data():
    assert speed_down_data([[1,2],[2,1]]) == [[1,2],[1,1],[2,1]]
    assert speed_down_data([[1,2],[2,1],[-5,5]]) == [[1,2],[1,1],[2,1],[-1,3],[-5,5]]
    assert speed_down_data([[]]) == [[]]
    assert speed_down_data([[1,2]]) == [[1,2]]
    assert speed_down_data([[10,10],[20,30],[30,50],[40,60]]) == [[10,10],[15,20],[20,30],[25,40],[30,50],[35,55],[40,60]]
def test_volume_up():
    assert volume_up_data([[5,0],[32222,32767],[-32222,-32767]])== [[6,0],[32767,32767],[-32768,-32768]]
    assert volume_up_data([[27305,27306],[-27305,-27306]])== [[32766,32767],[-32766,-32767]]
    assert volume_up_data([[-32760,-100],[-55,-55],[0,0],[4,-2017],[32767,10002]]) == [[-32768,-120],[-66,-66],[0,0],[4,-2420],[32767,12002]]
    assert volume_up_data([[]]) == [[]]
    assert volume_up_data([[1,10]]) == [[1,12]]
    assert volume_up_data([[1,27306]]) == [[1,32767]]
def test_trio_average():
    assert trio_average([[1,1],[7,7],[20,20]],2) == [9,9]
    assert trio_average([[-1,1],[-7,7],[-20,20]],2) == [-9,9]
    assert trio_average([[7,7],[20,20],[9,9]],2) == [12,12]
    assert trio_average([[7,7],[20,20],[9,9],[20,20],[9,9],[20,20],[9,9]],2) == [12,12]
def test_low_pass():
    assert low_pass_filter_data([[1,1],[7,7],[20,20],[9,9],[-12,-12]]) == [[4,4],[9,9],[12,12],[5,5],[-1,-1]]
    assert low_pass_filter_data([[-3333,6],[8,12],[0,0],[0,-8]]) == [[-1662,9],[-1108,6],[2,1],[0,-4]]
    assert low_pass_filter_data([[-3333,6]]) == [[-3333,6]]
    assert low_pass_filter_data([[]]) == [[]]
