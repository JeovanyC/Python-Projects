from plates import isValid

def testValid():
    assert isValid("AHBG21") == True

def testZeroStart():
    assert isValid("ABCD01") == False

def testLenght():
    assert isValid("ABSDASDAFDFAWSS34355656789045") == False
    
def testPontuation():
    assert isValid("ABC-D1") == False
