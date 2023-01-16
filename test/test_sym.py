from src.sym import SYM

class TestSym:

    def testsym(self):

        inp = ["a","a","a","a","b","b","c"]
        sym = SYM()

        for i in inp:
            sym.add(i)
        return "a" == sym.mid() and round(sym.div(),3) == 1.379

# testSym = TestSym()

# print(testSym.testsym())