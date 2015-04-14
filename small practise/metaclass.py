class LengthMetaclass(type):

    def __len__(self):
    	return 9
       # return self.clslength()

class A(object):
    __metaclass__ = LengthMetaclass

print len(A)

#http://stackoverflow.com/questions/7642434/is-there-a-way-to-implement-methods-like-len-or-eq-as-classmethods
'''
So the python __func__ in-place functions are actually using metaclass
normally some classes have __len__ or __iter__ or __repr__ and __str__ (traditionarily )
it's all based on their "base" "type" class (if metaclass is not specified.)
'''


1. different Lnorms
2. supervised algorithm: SVM
3. unsupervised algorithm: k-means, EM, dimension reduction, principle component analysis
4. gradient decent algorithm (measurement algorithm, cost functions)
4. Neural Networks
5. procedure to approache a machine learnning task
6. sentiment analysis & entity recognition (be honest)
7. Sigmoid functions!

Done:
sigmoid basics
supervised, unsupervised learnning 









Un Jardin Sur Le Toit 
Un Jardin Sur Le Nil Eau de
Un Jardin en Méditerranée  

Search analytics: find out what are people trying to do and how to measure them
log files = pictures