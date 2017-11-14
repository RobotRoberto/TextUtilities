# Short text corpus with focus on humor detection
This repository was created for publication of the datasets useful for humor recognition in one-liners. This repository contains six datasets and the python code used in the process of gathering the datasets. 

## 1. Humorous Jokes (not an actual file)
    Short description: This dataset contains all humorous jokes that were gathered in the webscraping process, which can be used as positive samples for humor recognition tasks. Jokes that had a Jaccard similarity coefficient higher than or equal to 0.9 were removed  in the deduplication process (Deduplication.py). This dataset was used to compile datasets 1.1 and 1.2. The first contains the jokes in this dataset shorter than 140 characters, whereas the latter consists of all jokes longer than 140 letters. Disclaimer: Some of the jokes may be racist, homophobic or insulting in other ways. A manual verification performed on 200 randomly drawn sentences revealed a possible noise of 2% non-humorous samples in the Oneliners dataset

## 1.1. Oneliners

    Filename: short_oneliners
    Filetype: .pickle
    Size: 12046 items
        
## 1.2. Long(er) jokes

    Filename: long_jokes
    Filetype: .pickle
    Size: 5606 items
    
## 2. Reuters Headlines

    Filename: reuters
    Filetype: .pickle
    Size: 13798 items
    Source: Reuters.com
    Short description: This dataset contains headlines published by international press agency Reuters on its own website. The website was accessed at 15-08-2017 and scraped using the file 'web_scraper - Reuters.py'. The headlines that had a Jaccard similarity coefficient higher than or equal to 0.9 in comparison to other headlines in the set were removed in the deduplication process (See: Deduplication.py).

## 3. English Proverbs

    Filename: proverbs
    Filetype: .pickle
    Size: 1019 items
    Sources: http://www.citehr.com/32222-1000-english-proverbs-sayings-love-blind.html, http://www.english-for-students.com/Proverbs.html
    Short description: This dataset contains a large part of existing English proverbs. Deduplication has been applied to remove duplicate proverbs (See: Deduplication.py).

## 4. Wikipedia sentences

    Filename: wikipedia
    Filetype: .pickle
    Size: 12046 items
    Sources: http://www.cs.pomona.edu/~dkauchak/simplification/
    Short description: Visit source URL for information on the data itself. This file contains a random selection of wikipedia sentences from the source file (the unsimplified one, to be specific) that were shorter than - or equal to- 140 characters. The random selection was made by calling the function 'draw_from_list_randomly(short_wiki_sentences, 12046)' from the file "Deduplication.py".

#The Python files:
These files are primarily here so that anyone can repeat the data gathering process and/or better understand it.

## Deduplication.py

This python program can be used to merge two files into one, deleting all (near-) duplicate sentences. It creates a Bag-of-Words representation of the input sentences and calculates the overlap in informative words that remain (jaccard-coefficient). If you only wish to remove duplicate sentences that have an exact match when represented as a bag-of-words, change the threshold from the default 0.9, to 1.0.

## web_scraper - Reuters.py

This program contains only an example, basic web scraper for retrieving sentences from Reuters.com. As each website is designed differently, changes might be necessary to extract data from other websites.

## write_functions.py

This file just contains a ready to go python function for saving a list of strings to a pickle file.
