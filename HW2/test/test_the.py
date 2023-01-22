class TestThe:
    def __init__(self, the) -> None:
        self.the = the
    def testthe(self):
        self.oo(self.the)
        return True
    def oo(self,t):
        print(self.o(t))
        return t
    def o(self,t):
        if type(t)!=dict:
            return str(t)
        
        def fun(k,v):
            if(str(k).find('_')!=0):
                v = self.o(v)
                return ":" + str(k) + " " + self.o(v)
            
            else:
                return False
        array = []
        for key in t:
            output = fun(key, t[key])
            if output:
                array.append(output)
            array.sort()
        return "{" + " ".join(str(val) for val in array) + "}"


'''


function oo(t) print(o(t)); return t end --> t; print `t` then return it
function o(t,isKeys,     fun) --> s; convert `t` to a string. sort named keys. 
  if type(t)~="table" then return tostring(t) end
  fun= function(k,v) if not tostring(k):find"^_" then return fmt(":%s %s",o(k),o(v)) end end
  return "{"..table.concat(#t>0 and not isKeys and map(t,o) or sort(kap(t,fun))," ").."}" end


'''