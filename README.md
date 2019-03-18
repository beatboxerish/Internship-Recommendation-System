# Internship Recommendation Project with LetsIntern Data
 
## About :

This is my capstone project for the Data Science Nanodegree. In this project, I have built a hybrid recommendation system which uses a combination of knowledge and content based models to make recommendations and a command line interface application that can be used to scrape data and make recommendations on it. I also made a mini-series of blog posts on Medium discussing how I went about completing my project and discussing the code to some extent. The data has been scraped from https://www.letsintern.com. 

Here are the links to the blog posts:
1. 
2. 
3. 
4. 

## Usage :

This section describes the usage of the command line application. Please make sure that you are in the main directory of this repo and not in any sub directory before running the below commands. Use `cd` to change the current directory.

**1. Scraping the data**

Basic Usage:`python scripts/app.py --scrape` (scrapes data off https://www.letsintern.com and saves it in the current directory. Takes some time to complete.) 

Options:
* Specifing location to save data: `python scripts/app.py --scrape --store_loc 'location/with/complete/name.csv'`

**2. Making recommendations**

Basic Usage:`python scripts/app.py --recs --load_loc 'path/to/load/scraped/data/from.csv'` 

Options:
* Specifing location to save data: `python scripts/app.py --recs --load_loc 'path/to/load/scraped/data/from.csv' --store_loc 'location/with/complete/name.csv'`

You can also scrape and make recommendations in one go. You would type `python --recs --scrape` for that. The `--store_loc` argument can be used similarly as above.

Type `python scripts/app.y -h` in your terminal for more help on the arguments.

## Files/Folders :

Note that there is additional information provided for each file in its respective folder. 

1. Notebooks - This folder contains all the jupyter notebooks used in this project. These can be used to explore the data or see how I proceeded with processing the data and making the final model.

2. data\_for\_notebook - This folder contains all the datasets used in the notebooks. 

3. scripts - This folder is the most important folder and contains all the code from code for scraping data to code for cleaning and making recommendations. It also contains the final app.py file which can be used as described in the above section.

4. .gitignore - This file contains the files that have to be ignored by git. You can leave this as it is and not care about it. 

## Libraries Required :
1. sklearn
2. NLTK
3. bs4
4. pandas
5. numpy 
6. matplotlib

