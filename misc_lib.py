# -*- coding: utf-8 -*-
""" 
This code is copied from:
http://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
example use : import misc_lib as ml
              for i in range(totalIteration)  
                ml.printProgress(i, totalIteration, prefix = 'Progress', suffix
                                ='Complete', barLength = 50)
"""
import sys

# Print iterations progress
def printProgress (iteration, total, prefix = '', suffix = '', decimals = 1,
                   barLength = 100):
    formatStr       = "{0:." + str(decimals) + "f}"
    percents        = formatStr.format(100 * (iteration / float(total)))
    filledLength    = int(round(barLength * iteration / float(total)))
    bar             = '█' * filledLength + '-' * (barLength - filledLength)
    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percents, '%',
                                                suffix)),
    sys.stdout.flush()
    if iteration == total:
        sys.stdout.write('\n')
        sys.stdout.flush()
