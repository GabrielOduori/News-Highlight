# News Highlight

###  By Gabriel Oduori

## Description
News Highlights is a web application that displays a list of various news sources for instance Al Jazeera, CNN et cetera. When a user selects a source, the website takes the user to topican news from the source selected. The user can then click on the news article preview and will be taken to the source page of the article. It achieves this by using the The web app is build by consuming data from News API (https://newsapi.org/).

You can view the site at: 

## User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I would like to:
* See various news sources on the landing page 
* Select the ones they prefer
* See the top news articles from that news source
* See the image, description and time the news article was created
* Click on an article and read it fully from the news source

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display news sources | **On page load** | List of various news sources is displayed per category |
| Display articles from a news source | **Click a news source** | Redirected to a page with a list of articles from the source |
| Display the preview of an article | **View Articles** | Each article displays an image, title, description and publication date |
| Read an entire article | **Click an article** | Redirected to the news source's site to read the entire article |

## SetUp / Installation Requirements
### Prerequisites
* python3.7
* Flask 1.0
* virtualenv

### Cloning
* In your terminal:
        
        $ git clone https://github.com/GabrielOduori/News-Highlight
        $ cd News-Highlight

## Running the Application
* Creating the virtual environment

        $ python3 -m pip install --user virtualenv ( on a Mac)
        $ python3 -m virtualenv env
        $ source env/bin/activate
        $(For other operating systems, see https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)
        
* Installing Flask and other Modules

while in the virtalenvironment install all the requirements by running 
$ pip install -r requirements.txt

        
* Setting up the API Key
        
        You have to generate own API key to run the application. This is done:
        
        * Visit https://newsapi.org/ and register for an API key.
        * In the root directory of the project folder create a file: start.sh in the following format:
        
                export NEWS_API_KEY='<Your-Api-Key>'
                python3.7 manage.py server
                
        * Replace the API Key you received from News Api with <Your-Api-Key>.
        
* To run the application, in your terminal:

        $ chmod a+x start.sh
        $ ./start.sh
        
## Testing the Application
* To run the tests for the class files:

        $ python3.7 manage.py tests
        
## Technologies Used
* Python3.7
* Flask

## License information

News Highlight is Copyright 2019 Gabriel ODUORI.

News Highlight is a free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. Password Lockeris distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with GitHub Search. If not, see http://www.gnu.org/licenses.

## Contact

gabriel.oduori@gmail.com

