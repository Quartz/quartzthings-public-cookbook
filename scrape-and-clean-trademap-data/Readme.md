# Handle bulk data from trademap.org

This tutorial automates the process of getting products data from International Trade Center through [trademap.org](trademap.org) and processing it to a tidy format.

You only need to automate the process if you find yourself repeatedly clicking the "download" button on the site to an extent that's not cost-efficient.

For US-specific trade figures, you can get more updated data in an automatic way using the US Census trade API. 

## 1. Scrape data with Selenium

It's best to scrape data from trademap.org using [Selenium](https://selenium-python.readthedocs.io/) for three reasons: 

1. [trademap.org](trademap.org) displays data through a dynamic database—meaning the site URL doesn't change when the data display changes. 

2. It doesn't have a captcha!

3. Its ToS doesn't prevent scraping. Make sure you check the terms before scraping data from any website and fill out [the scrape log](https://docs.google.com/forms/d/e/1FAIpQLScA4X3dTne2nCE3omUK6E-vF-oJHpJJ5_i2UkxbjJhxjTML_Q/viewform).

**Note**: Any website that meets these three features can be scraped with Selenium.

### Steps:

1. If you have not used Selenium on your computer, make sure you install the related packages and web driver (to interface with the browser.) You can follow the steps detailed [here](https://selenium-python.readthedocs.io/installation.html). 


2. Get the product IDs (HS codes in most cases) you need in a json array. You will need them to construct the URL query. 

3. Tweak [the python script](cookbook/scrape-and-clean-trademap-data/scrape-data-from-trademap.py) to get the data you need.

**Note**: Using Selenium is basically writing out step-by-step user interactions with the browser in a script. The steps outlined in [the python script](cookbook/scrape-and-clean-trademap-data/scrape-data-from-trademap.py) is specific to the site structure of trademap.org, but you can easily tweak it to fit your needs.

## 2. Read and process data

This is specific to handling excel files downloaded from trademap.org. These excel files are really just HTML pages (xml files) reformatted to an xls format. Here we process these files using the [`xml` R package](https://cran.r-project.org/web/packages/xml2/index.html).

### Steps:

1. If you have multiple excel files, save them to a single directory for easier reading. 
2. Tweak [the R script](cookbook/scrape-and-clean-trademap-data/read-data-from-trademap.R) to output a csv file with tidy data from the multiple excel files.