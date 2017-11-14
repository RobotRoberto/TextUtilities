# -*- coding: utf-8 -*-
import cPickle as pickle

def write_to_pickle(filename, list_of_sentences):
    f = open("%s.pickle"%filename, "wb")
    pickle.dump(list_of_sentences, f)
    f.close()
    print "The data was saved to %s.pickle. The file contains %d lines."%(filename, len(list_of_sentences))