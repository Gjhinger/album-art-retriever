# album-art-retriever v0.1

Motivated by my old CD Collection when I was a kid, I wanted to build a script to load album art from the web.
I utilized the Spotify API through the SpotiPy Python library to achieve this.
After completion, I wanted to make it a little more complicated, so I set out to make a version of the script with a GUI via tkinter.

## Files

* albumartcl.py - Command line script to load webpage with album art from Spotify
* albumartgui.py - Loads the album art within a frame in tkinter upon clicking the load image button and typing in an album name in the entry field

## To Do's

* Comment GUI Code and convert to classes for easier readability
* Use PyInstaller to create exe and add to releases

## Built With

* [SpotiPy](https://spotipy.readthedocs.io/en/2.16.1/)
* [tkinter](https://docs.python.org/3/library/tkinter.html)

## Acknowledgements

* vegaseat, for providing sample code on how to convert a url image into one useable by Tkinter (https://www.daniweb.com/programming/software-development/code/493005/display-an-image-from-the-web-tkinter)
