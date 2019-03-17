# importing argparse
import argparse

# defining arguments for command line interface
parser = argparse.ArgumentParser(description='Scrape, clean and make recommendations on internship data')
parser.add_argument('--scrape',help = 'scrape data from the web', action = 'store_true')
parser.add_argument('--clean',help = 'clean and prepare data for making recommendations',action = 'store_true')
parser.add_argument('--recs',help = 'make recommendations of similarity matrix',action = 'store_true')
parser.add_argument('--load_loc',help= 'enter path to load data to be used from')
parser.add_argument('--load_loc_sim',help= 'enter path to load similarity matrix from')
parser.add_argument('--store_loc',help='enter path to store output')
parser.add_argument('--store_loc_sim', help = 'enter path to store similarity matrix if using only --clean')
parser.add_argument('-n', help = 'no. of recommendation you want' )
parser.add_argument('-i', help = 'ith user id to be used')

args = parser.parse_args()

# import libs
import pandas as pd
import clean, recommendation, scrape
import sys

# making everything work

# this first case in for when just python scripts/app.py has been entered along with -i and -n
# we run everything one by one and later at the end of this script save the output
if len(sys.argv) ==  5:
    if args.n:
        df = scrape.scrape()
        df = clean.clean_prep_data(df)
        sim = clean.return_sim(df)
        df = recommendation.make_recs(sim,df,args.i, args.n)

# if load_loc has been entered then we load the data regardless of the other arguments
if args.load_loc:
    df = pd.read_csv(args.load_loc)

# if --scrape then scrape the data
if args.scrape:
    if args.load_loc: # give a warning to tell the user that loading a data doesnt make sense when specifying scrape
        print('warning: you have specified load_loc argument but that wont be used when you have specified scrape too')
    print('scraping data')
    df = scrape.scrape()
    if args.store_loc: # store the data regardless of other args if store_loc has been specified
        df.to_csv(args.store_loc)

# if --clean then clean the data
if args.clean:
    if not args.scrape:
        if not args.load_loc: # if load_loc hasnt been given and scrape also wasnt specified then there is no data with us to clean
            print('please specify load_loc to load in the dataset to be cleaned')
            quit()
    print('cleaning data')
    df = clean.clean_prep_data(df)
    sim = clean.return_sim(df)
    if args.store_loc: # store the clean dataset regardless of other args
        df.to_csv(args.store_loc)
        if not args.recs: # store sim only if recommendations are not to be made. If --recs: then we will be using sim there so no need to store
            sim.to_csv(args.store_loc_sim)

# if --recs then make recommendations
if args.recs:
    if not args.scrape:
        if not args.load_loc: # same logic as in clean
            print('please specify load_loc to load in the dataset to be made recommendations for')
            quit()
    if args.load_loc_sim: # read similarity matrix if location given
            sim = pd.read_csv(args.load_loc_sim)
    elif not args.clean: # if --clean hasnt been specified too then we need similarity matrix to be loaded 
        print('use --load_loc_sim please')
        quit()
    print('making recommendations')
    df = recommendation.make_recs(sim, df, args.i, args.n)
    if args.store_loc:
        df.to_csv(args.store_loc)

# save data if store_loc not specified
if not args.store_loc:
    try:
        df.to_csv('saved_df.csv')
        if args.clean:
            if not args.recs:
                sim.to_csv('saved_sim.csv')
        print('data has been saved in this directory')
    except:
        print('You havent specified the right arguments. Pls check python scripts/app.py -h')

