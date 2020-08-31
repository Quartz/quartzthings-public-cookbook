# Things team Cookbook

These are examples of how the Quartz things team has done certain tasks to execute our stories. There is more than one way to skin a cat, and there is more than one way to do most of the things we do. We are also not necassarily the best providers of instructions for certain tasks, so some of our recipes may link out to others'.

## Recipes

- How to do basic data tasks
    - [In Python](./basic-data-tasks/basic-data-tasks-python.ipynb)
    - In R

- Scraping data from a website
    - Dynamic
    	- Example: [Use Selenium to get data from trademap.org](./scrape-and-clean-trademap-data/)
    - Static
- Using satellite imagery
    - [Merging and reordering bands](./reordering-bands-and-merging-satellite-imagery_cl-gdal.md)
    - [Processing imagery from Landsat](./processing-landsat-images.md)
- [Using the US Census trade api to download data](./downloading-us-trade-data-from-the-us-census-api-in-r.ipynb)
- [Making tSNE diagrams](./making-tsne-diagrams/Readme.md)
- [Analyzing weighted survey data](./weighted-survey-analysis/weighted-survey-analysis.ipynb)
- [How to create an environment variable](./how-to-create-an-environment-variable.md)

## Contributing

Contributing to the cookbook can take many forms. You can:
- Link to a good tutorial
- Link to another repo
- Write a tutorial as a Markdown file
- Provide examples and snippets in a notebook file

For links, simply add the link under a heading above with the title of the tutorial and the language it uses (if any)

For tutorials in markdown and examples in notebooks commit them to the `cookbook-examples` folder. Choose descriptive file names such as `making-a-chropleth-map_javascript.ipynb` or `scraping-a-dynamic-website_python.ipynb` if it's a markdown file inside of a folder name the file `Readme.md` so that Github displays it by default.
