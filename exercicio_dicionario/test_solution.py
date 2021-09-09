from solution import primeiras_ocorrencias


class TestSolution:
    def test_abracadabra(self):
        entry = 'abracadabra'
        response = primeiras_ocorrencias(entry)
        hit = {'a': 0, 'b': 1, 'r': 2, 'c': 4, 'd': 6}
        assert hit == response

    def test_unique_letters(self):
        entry = 'qwerty'
        response = primeiras_ocorrencias(entry)
        hit = {'q': 0, 'w': 1, 'e': 2, 'r': 3, 't': 4, 'y': 5}
        assert hit == response

    def test_single_letter(self):
        entry = 'x'
        response = primeiras_ocorrencias(entry)
        hit = {'x': 0}
        assert hit == response

    def test_empty(self):
        entry = ''
        response = primeiras_ocorrencias(entry)
        hit = {}
        assert hit == response

    def test_repeat_letter(self):
        entry = 'xxx'
        response = primeiras_ocorrencias(entry)
        hit = {'x': 0}
        assert hit == response

    def test_special_symbol(self):
        entry = '$?@?"='
        response = primeiras_ocorrencias(entry)
        hit = {'$': 0, '?': 1, '@': 2, '"': 4, '=': 5}
        assert hit == response

    def test_space(self):
        entry = 'asd  fgh '
        response = primeiras_ocorrencias(entry)
        hit = {'a': 0, 's': 1, 'd': 2, ' ': 3, 'f': 5, 'g': 6, 'h':7}
        assert hit == response