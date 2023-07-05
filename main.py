# importing pyglet module
import pyglet

# I am not 100% sure, but what you can try is creating a pyglet.sprite.Sprite and passing
# the player.texture into it.
# Draw the sprite, then when you want, resize the sprite
# using sprite.scale_x and sprite.scale_y It should work.

# make sure that pyglet finds the ffmpeg dll's
pyglet.options['search_local_libs'] = True

if not pyglet.media.have_ffmpeg():
    print('Cannot playback videos as FFMPEG is not found. Exiting application.')

# width of window
width = 1500

# height of window
height = 800

# caption i.e title of the window
title = "Pyglet video player"

# creating a window
window = pyglet.window.Window(width, height, title, resizable=True)

# video path
vidPath = "bunny.mp4"

# creating a media player object
player = pyglet.media.Player()

# creating a source object
source = pyglet.media.StreamingSource()

# load the media from the source
MediaLoad = pyglet.media.load(vidPath)

# add this media in the queue
player.queue(MediaLoad)

# play the video
player.play()


# on draw event
@window.event
def on_draw():
    # clear the window
    window.clear()

    # if player source exist
    # and video format exist
    if player.source and player.source.video_format:
        # get the texture of video and
        # make surface to display on the screen
        player.get_texture().blit(20, 50)


# key press event
@window.event
def on_key_press(symbol, modifier):
    # key "p" get press
    if symbol == pyglet.window.key.P:
        # printing the message
        print("Key : P is pressed")

        # pause the video
        player.pause()

        # printing message
        print("Video is paused")

    # key "r" get press
    if symbol == pyglet.window.key.R:
        # printing the message
        print("Key : R is pressed")

        # resume the video
        player.play()

        # printing message
        print("Video is resumed")


# run the pyglet application
pyglet.app.run()