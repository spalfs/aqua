import matplotlib.pyplot as plot
from random import sample

a = sample(xrange(100),100)
b = sample(xrange(100),100)
c = sample(xrange(100),100)
d = sample(xrange(100),100)
e = sample(xrange(100),100)
f = sample(xrange(100),100)



plot.plot(a)
plot.savefig("static/tt.png")
plot.close()

plot.plot(b,'r')
plot.savefig("static/rt.png")
plot.close()

plot.plot(c,'g')
plot.savefig("static/rh.png")
plot.close()

plot.plot(d,'o')
plot.savefig("static/tp.png")
plot.close()

plot.plot(e,'p')
plot.savefig("static/rl.png")
plot.close()

plot.plot(f,'b')
plot.savefig("static/wl.png")
plot.close()



