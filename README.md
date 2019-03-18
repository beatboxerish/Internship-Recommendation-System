# Internship Recommendation Project with LetsIntern Data
 
## About :

This is my capstone project for the Data Science Nanodegree. In this project, I have built a hybrid recommendation system which uses a combination of knowledge and content based models to make recommendations and a command line interface application that can be used to scrape data and make recommendations on it. I also made a mini-series of blog posts on Medium discussing how I went about completing my project and discussing the code to some extent. The data has been scraped from https://www.letsintern.com. 
Some important points about my project:

* The problem definition was defined as : **Making an Internship recommendation system where the data will be scraped off from an internship portal/website and the end deliverable will be a command line app/interface.**

* There was no evaluation metric as there was no way of knowing the response to my recommendations. Thus the recommendations were to be tested by eye by judging how relevant and serendipitous they were.

* There was a small analysis of the data that was conducted. I tried to answered the following questions:
1. What are the most common types of category of internships ?
2. For each category of internship, find the area/state/city where the max no. of internships are offered.
3. What are the most in demand skills ? 
4. Which skills are most required for each category ?
5. Find which category has the maximum no. of unpaid internships ?

The answers along with visualizations can be found in the analysis jupyter notebook in Notebooks/.

* There were some things though that could have improved my project :
1. Found a better metric/method to test my recommendation system. It would have been good to some concrete results about the performance of my recommendation model.
2. Had more knowledge about NLP techniques to make a better content-based model. There are probably many more techniques that can be used to summarize data and find relationships between different pieces of text.
3. Scrape data from more sites to increase the data I had in order to better analyze my data and make more interesting recommendations.

This was a long and tiring but fun project. It took me a lot of time and a lot of mistakes to complete everything. I rewrote and refactored code a lot to make it easy to go about and use. Even the blog posts took me a lot of time. But in the end, I guess it was worth it. I was able to make a command line app to make really good recommendations. The code used can also be very easily extended into a web app and be used to make recommendations to users with a graphical interface.

Here are the links to the blog posts:
1. Introduction - https://medium.com/@ishannangia/building-an-internship-recommendation-system-i-introduction-8ab428131483
2. Scraping - https://medium.com/@ishannangia/building-an-internship-recommendation-system-ii-scraping-a7276ff30e1a
3. Cleaning - https://medium.com/@ishannangia/an-internship-recommendation-system-iii-cleaning-2721b5416a70
4. Recommendations - https://medium.com/@ishannangia/an-internship-recommendation-system-iv-recommendations-7cbd8c8d355e 

## Outline of the Project :
    
1. **Collecting Data:** Data was to be collected through scraping using python’s BeautifulSoup library. The website data was to be scraped from https://www.letsintern.com.

2. **Cleaning Data:** Data collected was to be cleaned and prepared to be used for making a recommendation model. This would also include preparing it for some basic data analysis.

3. **Analyzing Data:** The cleaned data was to be used to answer some questions that would provide an interesting understanding of internship trends. (There is no post for this though an entire notebook has been dedicated to this. Please check the analysis.ipynb notebook in Notebooks.)

4. **Making Recommendations:** A recommendation model was to be made and improved so that the internships recommended would not only be relevant to the internship that a user looked at, but also unique and serendipitous. A command line app was also to be made to allow easy usage of the scripts.

## Usage :

This section describes the usage of the command line application. Please make sure that you are in the main directory of this repo and not in any sub directory before running the below commands. Use `cd` to change the current directory.

**1. Scraping the data**

Basic Usage:`python scripts/app.py --scrape` (scrapes data off https://www.letsintern.com and saves it in the current directory. Takes some time to complete.) 

Options:
* Specifying location to save data: `python scripts/app.py --scrape --store_loc 'location/with/complete/name.csv'`

**2. Making recommendations**

Basic Usage:`python scripts/app.py --recs --load_loc 'path/to/load/scraped/data/from.csv'` 

Options:
* Specifying location to save data: `python scripts/app.py --recs --load_loc 'path/to/load/scraped/data/from.csv' --store_loc 'location/with/complete/name.csv'`

You can also scrape and make recommendations in one go. You would type `python scripts/app.py --recs --scrape` for that. The `--store_loc` argument can be used similarly as above.

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
7. argparse
