import numpy
from .lstsqr import lstsqr
from .logitl import LOGITL
def vp(n, x, y, w, nk, il, yb, sw, az, tb, cm):

    if il == 0:
        gof = lstsqr(n, x, y, w, nk, yb, sw, tb, cm)
        return gof, tb
    LOGITL0 = LOGITL()
    az, tb, sc = LOGITL0.logitl(n, x, y, w, nk, il, az, tb, cm)
    t = 0.0
    
    (m,) = numpy.where(tb[1,1:] != 0.0)
    m = m+1
    k = range(1,len(m)+1)
    #print 'vp'
    for i in range(1, n+1):
        a = az + numpy.inner(tb[1,m], sc[i,k])
        pp = 1.0/(1.0 + numpy.exp(-a))
        t = t + w[i]*(y[i]-pp)**2
    gof = t/sw
    return gof, tb
