cierpliwosc = raw_input("jaka jest twoja cieprliwosc? w skali 1-100")
if (cierpliwosc.isdigit()):
    if (int(cierpliwosc) > 100):
        print 'nie zdechniesz szybko'
    else:
        print 'GL & HF'
else:
    print "czytac nie potrafisz?"




