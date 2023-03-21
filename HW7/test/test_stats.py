from src.stats import *
from src.num import NUM
from src.sym import SYM


def test_ok(n=1):
    random.seed(n)

def test_sample():
    for i in range(1,10+1): 
        print("",''.join(samples(["a","b","c","d","e"])))


def test_num():
    n = NUM()
    for i in range(1,10+1):
        n.add(i)
    print("",n.n,n.mu,n.sd)

def test_gaussian():
    t = []
    n = NUM()
    for i in range(1,10000+1):
        gauss = gaussian(10,2)
        t.append(gauss)
        n.add(gauss)
    print("",n.n,n.mu,n.sd)

def test_bootstrap():
    a, b = [], []

    for i in range(1,101):
        a.append(gaussian(10,1))
    print("","mu","sd","cliffs","boot","both")
    print("","--","--","------","----","----")
    for mu in range(100, 111, 1):
        mu /= 10.0
        b= []
        for i in range(1,101):
            b.append(gaussian(mu,1))
        cl = cliffsDelta(a,b)
        bs = bootstrap(a,b)
        print("",mu,1,cl,bs,cl and bs)

def test_basic():
    print("\t\ttruee", bootstrap( {8, 7, 6, 2, 5, 8, 7, 3}, 
                                {8, 7, 6, 2, 5, 8, 7, 3}),
              cliffsDelta( {8, 7, 6, 2, 5, 8, 7, 3}, 
                           {8, 7, 6, 2, 5, 8, 7, 3}))
    print("\t\tfalse", bootstrap(  {8, 7, 6, 2, 5, 8, 7, 3},  
                                 {9, 9, 7, 8, 10, 9, 6}),
             cliffsDelta( {8, 7, 6, 2, 5, 8, 7, 3},  
                          {9, 9, 7, 8, 10, 9, 6})) 
    print("\t\tfalse", 
                    bootstrap({0.34, 0.49, 0.51, 0.6,   .34,  .49,  .51, .6}, 
                               {0.6,  0.7,  0.8,  0.9,   .6,   .7,   .8,  .9}),
                  cliffsDelta({0.34, 0.49, 0.51, 0.6,   .34,  .49,  .51, .6}, 
                              {0.6,  0.7,  0.8,  0.9,   .6,   .7,   .8,  .9})
   )



def test_pre():
    print("\neg3")
    d = 1
    for i in range(1,11):
        t1 = []
        t2 = []
        for j in range(1,33):
            t1.append(gaussian(10,1))
            t2.append(gaussian(d*10,1))
        val = True if d<1.1 else False
        print("\t",d,val, bootstrap(t1,t2), bootstrap(t1,t1))
        d = round(d + 0.05,2)


def test_five():
  for rx in tiles(scottKnott(
         [RX([0.34,0.49,0.51,0.6,.34,.49,.51,.6],"rx1"),
         RX([0.6,0.7,0.8,0.9,.6,.7,.8,.9],"rx2"),
         RX([0.15,0.25,0.4,0.35,0.15,0.25,0.4,0.35],"rx3"),
         RX([0.6,0.7,0.8,0.9,0.6,0.7,0.8,0.9],"rx4"),
         RX([0.1,0.2,0.3,0.4,0.1,0.2,0.3,0.4],"rx5")])):
    print(rx['name'],rx['rank'],rx['show'])

def test_six():
  for rx in tiles(scottKnott(
        [RX({101,100,99,101,99.5,101,100,99,101,99.5},"rx1"),
         RX({101,100,99,101,100,101,100,99,101,100},"rx2"),
         RX({101,100,99.5,101,99,101,100,99.5,101,99},"rx3"),
         RX({101,100,99,101,100,101,100,99,101,100},"rx4")])):
    print(rx['name'],rx['rank'],rx['show'])

def test_sk():
    rxs,a,b,c,d,e,f,g,h,j,k=[],[],[],[],[],[],[],[],[],[],[]
    for i in range(1,1001):
        a.append(gaussian(10,1))
    for i in range(1,1001):
        b.append(gaussian(10.1,1))
    for i in range(1,1001):
        c.append(gaussian(20,1))
    for i in range(1,1001):
        d.append(gaussian(30,1))
    for i in range(1,1001):
        e.append(gaussian(30.1,1))
    for i in range(1,1001):
        f.append(gaussian(10,1))
    for i in range(1,1001):
        g.append(gaussian(10,1))
    for i in range(1,1001):
        h.append(gaussian(40,1))
    for i in range(1,1001):
        j.append(gaussian(40,3))
    for i in range(1,1001):
        k.append(gaussian(10,1))
    
    for k,v in enumerate([a,b,c,d,e,f,g,h,j,k]):
        rxs.append(RX(v, "rx"+str(k+1)))
    
    for rx in tiles(scottKnott(rxs)):
        print("",rx["rank"],rx["name"],rx["show"])

def test_tiles():
    rxs,a,b,c,d,e,f,g,h,j,k=[],[],[],[],[],[],[],[],[],[],[]
    for i in range(1,1001):
        a.append(gaussian(10,1))
    for i in range(1,1001):
        b.append(gaussian(10.1,1))
    for i in range(1,1001):
        c.append(gaussian(20,1))
    for i in range(1,1001):
        d.append(gaussian(30,1))
    for i in range(1,1001):
        e.append(gaussian(30.1,1))
    for i in range(1,1001):
        f.append(gaussian(10,1))
    for i in range(1,1001):
        g.append(gaussian(10,1))
    for i in range(1,1001):
        h.append(gaussian(40,1))
    for i in range(1,1001):
        j.append(gaussian(40,3))
    for i in range(1,1001):
        k.append(gaussian(10,1))
    
    for k,v in enumerate([a,b,c,d,e,f,g,h,j,k]):
        rxs.append(RX(v, "rx"+str(k+1)))

    rxs = sorted(rxs, key=lambda x: mid(x))
    for rx in tiles(rxs):
        print("",rx['name'],rx['show'])