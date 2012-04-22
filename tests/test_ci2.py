#!/usr/bin/env python

from lmfit import Parameters, Minimizer, coinf, coinf_2d, minimize
import numpy as np
try:
    import pylab
    HASPYLAB = True
except ImportError:
    HASPYLAB = False

np.random.seed(1)

p_true = Parameters()
p_true.add('amp', value=14.0)
p_true.add('decay', value=0.010)
p_true.add('amp2', value=-10.0)
p_true.add('decay2', value=0.050)


def residual(pars, x, data=None):
    amp = pars['amp'].value
    decay = pars['decay'].value
    amp2 = pars['amp2'].value
    decay2 = pars['decay2'].value


    model = amp*np.exp(-x*decay)+amp2*np.exp(-x*decay2)
    if data is None:
        return model
    return (model - data)

n = 200
xmin = 0.
xmax = 250.0
noise = np.random.normal(scale=0.7215, size=n)
x     = np.linspace(xmin, xmax, n)
data  = residual(p_true, x) + noise

fit_params = Parameters()
fit_params.add('amp', value=14.0)
fit_params.add('decay', value=0.010)
fit_params.add('amp2', value=-10.0)
fit_params.add('decay2', value=0.050)

out = minimize(residual, fit_params, args=(x,), kws={'data':data})
out.leastsq()
ci, trace=coinf(out, trace=True)



pylab.plot(x,data)
pylab.figure()
names=fit_params.keys()
pylab.hot()
from scipy.interpolate import interp1d
for i in range(4):
    for j in range(4):
        pylab.subplot(4,4,16-j*4-i)
        if i!=j:
            x,y,m=coinf_2d(out,names[i],names[j],20,20)
            #print x,y,m
            pylab.contourf(x,y,m,20)

            pylab.xlabel(names[i])
            pylab.ylabel(names[j])
            
            x=trace[names[i]][names[i]]            
            y=trace[names[i]][names[j]]
            pr=trace[names[i]]['prob']
            s=np.argsort(x)
            pylab.scatter(x[s],y[s],c=pr[s],s=30,lw=1)
        else:
            x=trace[names[i]][names[i]]            
            y=trace[names[i]]['prob']
            
            t,s=np.unique(x,True)                       
            f=interp1d(t,y[s],'slinear')
            xn=np.linspace(x.min(),x.max(),50)
            pylab.plot(xn,f(xn),'g',lw=1)
            pylab.xlabel(names[i])
            pylab.ylabel('prob')
        #print "jo"
#pylab.colorbar()
pylab.show()


    



