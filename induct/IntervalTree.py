#!/usr/bin/python
#
# author:
# 
# date: 
# description:
#

class IntervalTree:
    count = 1
    
    def __init__(self):
        self.idx = "r{}".format(IntervalTree.count)
        self.name = ""
        self.interval = None
        self.childNodes = []
        self.alignment = []
        
        IntervalTree.count += 1
    
    def sortChildNodes(self):
        ##self.childNodes.sort(key=lambda t: t.interval.)
        pass

    def induceIrtgRules(self, sentence):
        pass

    def funql(self):
        def helper(tree):
            if len(tree.childNodes) == 0:
                return tree.name
            else:
                return "{}({})".format(tree.name, ",".join(helper(t) for t in tree.childNodes))
        return helper(self).replace("+"," ").replace("0","\"0\"")

    def derivation(self):
        if len(self.childNodes) == 0:
            return self.idx
        else:
            return "{}({})".format(self.idx, ",".join(t.derivation() for t in self.childNodes))

    def __str__(self):
        interval = "[{},{}]".format(self.interval.start,self.interval.end)
        if self.childNodes:
            return "{}{}({})".format(self.name,interval, ",".join(str(t) for t in self.childNodes))
        else:
            return "{}{}".format(self.name,interval)

    __repr__ = __str__

class Interval:
    def __init__(self, start=None, end=None):
        if (start == None) or (end == None):
            self.start = 0
            self.end = 0
            self.interval = [[]]
        else:
            self.start = start
            self.end   = end
            self.interval = [range(start, end)]
    
    def __iter__(self):
        for interval in self.interval:
            for element in interval:
                yield element

    def subset(self, start, end):
        pass

    def addPlaceholder(self):
        self.interval.append([])
    
    def first(self):
        return filter(lambda x: x>= 0, self.flatten())[0]
    
    def last(self):
        return self.interval[-1][-1]
    
    def without(self, other):
        erg = Interval(self.start,self.end)
        erg.interval = self.interval[:]
        
        if len(other.interval) == 0 or (len(other.interval) == 1 and len(other.interval[0]) == 0):
            return erg
        
        start, end = other.first(), other.last()
        pos = -1
        for idx,intv in enumerate(erg.interval):
            if (start in intv) and (end in intv):
                pos = idx
                break
        else:
            return erg
        
        startpos, endpos = erg.interval[pos].index(start), erg.interval[pos].index(end)
        # what if startpos == 0 or endpos == len(erg.interval) ???
        before = erg.interval[:pos]   + ([erg.interval[pos][:startpos]] if erg.interval[pos][:startpos] else [])
        after  = erg.interval[pos+1:] + ([erg.interval[pos][endpos+1:]] if erg.interval[pos][endpos+1:] else [])
        
        erg.interval = before + [[]] + after

        return erg
    
    def flatten(self):
        res = []
        for xs in self.interval:
            if not xs:
                res.append(-1)
            else:
                res.extend(xs)
        return res
    
    def __str__(self):
        #return "[{}]".format(",".join(map(str,self.interval)))
        return str(self.interval)
    __repr__ = __str__
