<div id="top"></div>


<h3 align="center">Futbin popular scraper</h3>

  <p align="center">
    A Python scraper for futbin </p>
</div>


<!-- ABOUT THE PROJECT -->
## About The Project

<h4 align="center">Screenshot of futbin.com.</h4>

[![Product Name Screen Shot][product-screenshot]](images/futbin_screenshot.png)

<h4 align="center">Screenshot of the collected data in the 'Players.json' file.</h4>

[![Product Name Screen Shot][product-screenshot]](images/json_screenshot.png)

The project is a Python3 script to scrape the top 100 players on futbin.
The main.py scrapes the player-id (pid) of the current top 100 players on futbin. 
The scraped pid is used in a GET request to get al the data of the player with the pid. 
The requested data is parsed and saved in players.json file. 

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python3](https://www.python.org/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get started you need to pip install bs4 to scrape the page and lxml to parse the data.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* bs4
  ```sh
  pip install bs4
  ```
* lxml
  ```sh
  pip install lxml
  ```
<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

To use the project, you just run the main.py. The code will show how many players are left in the terminal. When all the players have been scraped and saved the terminal will show "Players have been added to the 'Players.json' file!"

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [] Make the project into a CLI
- [] Let the user decided how many players they want to fetch
    - [] Only fetch the top 10
    - [] Let the user decide how many they want via input


<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTACT
## Contact

Name - [@twitter_handle](https://twitter.com/twitter_handle) - email@email_client.com

Project Link: [https://github.com/github_username/repo_name](https://github.com/github_username/repo_name)

<p align="right">(<a href="#top">back to top</a>)</p> -->
