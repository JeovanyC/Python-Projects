from um import count

def test_basic():
    assert count("um") == 1
    assert count("UM") == 1
    assert count("Um") == 1

def test_punctuation():
    assert count("um,") == 1
    assert count("um.") == 1
    assert count("um!") == 1
    assert count("um?") == 1
    assert count("um...") == 1

def test_multiple():
    assert count("um um um") == 3
    assert count("um, um. Um!") == 3
    assert count("um um um um um") == 5

def test_not_count_inside_words():
    assert count("album") == 0
    assert count("rumo") == 0
    assert count("lume") == 0
    assert count("instrumento") == 0

def test_no_um():
    assert count("gato cachorro elefante") == 0
    assert count("") == 0

def test_mixed():
    assert count("Um dia um homem disse um segredo.") == 3
    assert count("um carro, um cachorro e um gato.") == 3
    assert count("No álbum de fotos, ele viu um carro.") == 1