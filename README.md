# Mapping Ontario maple syrup

This project is an attempt to scrape the address list of members of the Ontario Maple Syrup Producers Association
that are registered as offering direct sales to the public, and display the results on a map.

The data comes from the OMSPA website: http://www.ontariomaple.com/ and is scraped using Scrapy - http://scrapy.org/

Result: https://batchgeo.com/map/ontariomaple

### Current issues
* Isolating the address on the producers' list is not straightforward. Currently, the script locates the postal
code and uses it for mapping, which can lead to unprecise results.
* Because of the above issue, the whole blob of text for each producer is currently displayed in the info box. This
will be addressed once I get a clean fix on the address.
* BatchGeo only allows up to 250 results per map for free, so it's currently capping the list before displaying.
I'm not sure this project warrants a pro subscription, so for now I just have to live with that limit.

### How to
1. Make sure you have Scrapy installed. On most Python installations, it's as easy as typing `pip install scrapy`
1. Download this repository
1. Navigate to the project root directory (where the file *scrapy.cfg* is
located) and run `scrapy crawl maple -o YOURFILE.csv` 
 * You can replace .csv with e.g. .json to get a JSON file instead. Fun!
1. Upload the resulting csv to BatchGeo or do other fun stuff with the data
