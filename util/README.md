* __ams-fellow-scraper.py__

  A Python based web scraper that scrapes AMS's [fellow page](http://www.ams.org/cgi-bin/fellows/fellows.cgi) for award winners. 
  It then updates the file `ams-fellows.csv` which contains the name of the fellow, their university affiliation, and the year they were elected.
  This is done automatically once per month using GitHub actions to ensure the most accurate results.
 
* __fields-medal-scraper.py__

  A Python based web scraper that scrapes [Math Union](https://www.mathunion.org/imu-awards/fields-medal) for award winners.
  It then updates the file `fields-medal.csv` which contains the name of the recipient, and the year in which the medal was
  awarded. This is done automatically once every four years on the opening of the International Congress of Mathematicians. 
