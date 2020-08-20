from delphin import ace
from delphin import tsdb
from delphin import itsdb

ts = itsdb.TestSuite('sample-200-py')
with ace.ACEParser('terg-mac.dat', cmdargs = ['--disable-generalization'], full_forest=True) as cpu: 
    ts.process(cpu)


    
