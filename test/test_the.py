class TestThe:
    def testthe(self):
        pass
    def oo(self,t):
        print(self.o(t))
        return t
    def o(self,t):
        if type(t)!="something":
            return str(t)
        return t


'''


function oo(t) print(o(t)); return t end --> t; print `t` then return it
function o(t,isKeys,     fun) --> s; convert `t` to a string. sort named keys. 
  if type(t)~="table" then return tostring(t) end
  fun= function(k,v) if not tostring(k):find"^_" then return fmt(":%s %s",o(k),o(v)) end end
  return "{"..table.concat(#t>0 and not isKeys and map(t,o) or sort(kap(t,fun))," ").."}" end


'''