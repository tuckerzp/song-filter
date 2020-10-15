# Song Filter
Program to help speed up screening of music by checking for blacklisted words
within a song. Lyrics are obtained from online lyrics sites like Genius.

### Please note:
This program does **NOT** guarantee that a song is clean, it only finds songs that
go against FCC guidelines.

## Installation
Installing is fairly straight forward. All that is required is python 3, pyyaml and
beautiful soup 4.

```bash
pip install beautifulsoup4
```

```bash
pip install lyricsgenius
```

## Usage
All you need to run is to make a .txt file! See the sample.txt for help.\
\
The format is:\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AuthorName---SongTitle\
\
Then pass the program your txt file and it will run. For example:

```bash
python main.py sample.txt
```




## TODO
1. Add ability to cross check other sites
 
