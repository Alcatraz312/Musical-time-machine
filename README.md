# Musical time machine 🎵

![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/Alcatraz312/Musical-time-machine)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

![GitHub top language](https://img.shields.io/github/languages/top/Alcatraz312/Musical-time-machine)

Create Spotify playlists of the top 100 Billboard songs from any year with ease! This Python program leverages web scraping to fetch the Billboard Hot 100 songs of a specified year and then uses a Spotify API (Spotipy) to create a playlist containing these chart-topping tracks.

## Getting Started

### Prerequisites

Before using this program, you'll need the following:

* Python 3.6 or higher installed on your system.
* A Spotify account to create playlists.
* A Spotify Developer App to get API credentials.

### Installation

1. Clone this GitHub repository to your local machine:

```python
git clone https://github.com/Alcatraz312/Musical-time-machine.git
```

2. Change into the project directory:

```python
cd Musical-time-machine
```

3. Install the required python packages using pip:

```python
pip install bs4
```
```python
pip install Spotipy
```
```python
pip install requests
```

## Configuration
To use this program, you need to set up your Spotify API credentials:

1. Create a Spotify Developer App: Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard) and create a new app. Note down the Client ID and Client Secret.

2. Create a file named config.py in the project directory and add the following lines:

```python
SPOTIPY_CLIENT_ID = 'your-client-id'
SPOTIPY_CLIENT_SECRET = 'your-client-secret'
SPOTIPY_REDIRECT_URI = 'http://example.com'
```
Replace 'your-client-id' and 'your-client-secret' with the credentials from your Spotify Developer App.

3. Import client ID, client secret and redirect uri from config.py as following: 
```python
from config import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI
```
4. Authenticate with spotify using ```from spotipy.oauth2 import SpotifyOAuth``` :
```python
auth = SpotifyOAuth(client_id= SPOTIPY_CLIENT_ID,
                    client_secret= SPOTIPY_CLIENT_SECRET,
                    redirect_uri= "http://example.com",
                    scope= "playlist-modify-private",
                    show_dialog= True,
                    username= "Your spotify username")
```

5. Run the code and if successful user should see a spotify web page show up automatically. Click on "Agree", it will redirect the user to the redirect uri given by the user, copy the entire url and paste it in the editor terminal to get the auth token.

![](https://img-c.udemycdn.com/redactor/raw/2020-08-12_15-32-02-17be790a8783bf4fdc4eeff77b497044.png)

6. This will automatically add a file named "token.txt" in the directory. Store this value("token.txt") in the "cache path" parameter of the auth object defined above.

## Usage
1. Run the script by executing the following command:
```python
python Musical-time-machine.py
```
2. The program will prompt you to enter the date for which you want to fetch the Billboard Top 100 songs.

3. The program will fetch the top 100 songs from the specified year on Billboard and create a new playlist in your Spotify account with those songs.

## Contribution
1. Fork the repository and create a new branch for your feature or bug fix.

2. Make your changes, and ensure that your code follows the PEP 8 style guide.

3. Write tests to cover your code if applicable.

4. Create a pull request with a clear description of your changes and why they are needed.

5. Your pull request will be reviewed, and once approved, it will be merged into the main branch.

## license

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Alcatraz312/Musical-time-machine/blob/main/LICENSE.md) file for details.


