import tkinter as tk
import io
from urllib.request import urlopen
from PIL import Image, ImageTk
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

window = tk.Tk()
frm_input = tk.Frame()
lbl_aname = tk.Label(master=frm_input, text="Album Name")
ent_aname = tk.Entry(master=frm_input)
btn_dl = tk.Button(master=frm_input, text="Download")
lbl_aname.pack()
ent_aname.pack()
btn_dl.pack()

pic_url = "https://i.scdn.co/image/ab67616d0000b273b298538481c52f7e217ed000"
frm_art = tk.Frame(relief=tk.SUNKEN, borderwidth=5, height=500, width=500)
# open web page read into memory stream
my_page = urlopen(pic_url)
# create image file object
my_picture = io.BytesIO(my_page.read())
# PIL to open .jpg, .png, etc.
pil_img = Image.open(my_picture)
# Convert to Tkinter usable image
tk_image = ImageTk.PhotoImage(pil_img)

lbl_art = tk.Label(master=frm_art, image=tk_image)
lbl_art.pack(fill=tk.BOTH, expand=True)


# Create an event handler
def handle_dl(event):
    cid = 'Client ID'
    secret = 'Secret ID'
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    results = spotify.search(q='album:' + ent_aname.get(), type='album')
    items = results['albums']['items']
    if len(items) > 0:
        album = items[0]
        print(album['name'], album['images'][0]['url'])
        pic_url = album['images'][0]['url']
        # open web page read into memory stream
        my_page = urlopen(str(pic_url))
        # create image file object
        my_picture = io.BytesIO(my_page.read())
        # PIL to open .jpg, .png, etc.
        pil_img = Image.open(my_picture)
        # Convert to Tkinter usable image
        tk_image2 = ImageTk.PhotoImage(pil_img)
        lbl_art.configure(image = tk_image2)
        lbl_art.image = tk_image2
        lbl_art.pack(fill=tk.BOTH, expand=True)


btn_dl.bind("<Button-1>", handle_dl)

frm_art.pack(side=tk.RIGHT)
frm_input.pack(side=tk.LEFT)

window.mainloop()
