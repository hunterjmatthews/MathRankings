## Scripts
* ### __ams-fellow-scraper.py__

  - A Python based web scraper that scrapes AMS's [fellow page](http://www.ams.org/cgi-bin/fellows/fellows.cgi) for award winners. 
  It then updates the file `ams-fellows.csv` which contains the name of the fellow, their university affiliation, and the year they were elected.
 
* ### __fields-medal-scraper.py__

  - A Python based web scraper that scrapes [Math Union](https://www.mathunion.org/imu-awards/fields-medal) for award winners.
  It then updates the file `fields-medal.csv` which contains the name of the recipient, and the year in which the medal was
  awarded.

* ### __math-authors-scraper.py__

  - A Python based web scraper that scrapes [MathSciNet]() collecting all authors from A-Z. It then stores this data in the file `math-authors.csv` and deletes any duplicates.
