import random
import math

from src.num import NUM

the = {"bootstrap":512, "conf":0.05, "cliff":0.4, "cohen":.35, "Fmt": "{:.2f}", "width":40}


def cliffsDelta(ns1,ns2):
    if len(ns1) > 128:
        ns1 = samples(ns1,128)
    if len(ns2) > 128:
        ns2 = samples(ns2,128)
    n,gt,lt = 0,0,0
    for x in ns1:
        for y in ns2:
            n = n + 1
            if x > y:
                gt = gt + 1
            if x < y:
                lt = lt + 1
    return abs(lt - gt)/n <= the['cliff']

def samples(t, n=None):
	u = []
	for i in range((len(t) or n)):
		u.append(t[random.randint(0,len(t)-1)])
	return u


def gaussian(mu, sd):
	mu,sd = mu or 0, sd or 1
	sq,pi,log,cos,r = math.sqrt, math.pi, math.log, math.cos, random.random
	return mu + sd * sq(-2*log(r())) * cos(2*pi*r())


def delta(i, other):
	e, y, z = 1E-32, i, other
	return abs(y.mu - z.mu) / ((e + y.sd**2/y.n + z.sd**2/z.n)**0.5)

def bootstrap(y0,z0):
	x,y,z,yhat,zhat = NUM(), NUM(), NUM(), [], []

	for y1 in y0:
		x.add(y1)
		y.add(y1)
	for z1 in z0:
		x.add(z1)
		z.add(z1)
	
	xmu, ymu, zmu = x.mu, y.mu, z.mu

	for y1 in y0:
		yhat.append(y1 - ymu + xmu)
	
	for z1 in z0:
		zhat.append(z1 - zmu + xmu)
	
	tobs = delta(y,z)

	n = 0

	for _ in range(1,the["bootstrap"]+1):
		firstSample = NUM()
		secondSample = NUM()
		for y in samples(yhat):
			firstSample.add(y)
		for z in samples(zhat):
			secondSample.add(z)
		
		if delta(firstSample, secondSample) > tobs:
			n = n + 1
	

	return n / the["bootstrap"] >= the["conf"]

def RX(t,s):
	t = sorted(t)
	return {"name" : s or "", "rank":0, "n":len(t), "show":"", "has":t}

def mid(t):
	t = t["has"] and t["has"] or t
	n = (len(t)-1)//2
	return (t[n] +t[n+1])/2 if len(t)%2==0 else t[n+1]

def merge(rx1, rx2):
	rx3 = RX({}, rx1["name"])
	rx3["has"] = sorted(rx1["has"] + rx2["has"])
	rx3["n"] = len(rx3["has"])
	return rx3

def div(t):
  t= t['has'] and t['has'] or t
  return (t[ len(t)*9//10 ] - t[ len(t)*1//10 ])/2.56

def tiles(rxs):
	huge = float('inf')
	lo = huge
	hi = float('-inf')

	for rx in rxs:
		lo, hi = min(lo, rx["has"][0]), max(hi, rx["has"][len(rx["has"])-1])
	
	for rx in rxs:
		t,u = rx["has"],[]
		def of(x, most):
			return int(max(0, min(most, x)))

		def at(x):
			return t[of(len(t)*x//1, len(t))]
		
		def pos(x):
			return math.floor(of(the['width']*(x-lo)/(hi-lo+1E-32)//1, the['width']))
		
		for i in range(0,the["width"]+1):
			u.append(" ")
		
		a,b,c,d,e= at(.1), at(.3), at(.5), at(.7), at(.9) 
		A,B,C,D,E= pos(a), pos(b), pos(c), pos(d), pos(e)
		for i in range(A,B+1):
			u[i]="-"
		for i in range(D,E+1):
			u[i]="-"
	
		u[the["width"]//2] = "|"
		u[C] = "*"
		vals = []
		for i in [a,b,c,d,e]:
			vals.append(the['Fmt'].format(i))
		rx['show'] = ''.join(u) + str(vals)
	return rxs



def scottKnott(rxs):
	def merges(i,j):
		out = RX([],rxs[i]["name"])
		for k in range(i,j+1):
			out = merge(out, rxs[j])
		return out

	def same(lo, cut, hi):
		l  = merges(lo, cut)
		r = merges(cut+1, hi)
		return cliffsDelta(l["has"], r["has"]) and bootstrap(l["has"], r["has"])

	def recurse(lo,hi, rank):
		b4 = merges(lo,hi)
		best = 0
		cut = None
		for j in range(lo,hi+1):
			if j<hi :
				l = merges(lo, j)
				r = merges(j+1, hi)
				now = (l["n"]*(mid(l) - mid(b4))**2 + r["n"]*(mid(r) - mid(b4))**2) / (l["n"] + r["n"])
				if now > best:
					if abs(mid(l) - mid(r)) >= cohen:
						cut, best = j, now
		
		if cut and not same(lo,cut,hi):
			rank = recurse(lo, cut, rank) + 1
			rank = recurse(cut+1, hi, rank)
		else:
			for i in range(lo, hi+1):
				rxs[i]["rank"] = rank
		
		return rank
	rxs = sorted(rxs, key=lambda x: mid(x))
	cohen = div(merges(0,len(rxs)-1)) * the['cohen']
	recurse(0, len(rxs)-1, 1)
	return rxs