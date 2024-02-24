import pyglet
from pyglet.window import key

# Initialing some stuff
window = pyglet.window.Window(fullscreen=True)
keys = key.KeyStateHandler()
window.push_handlers(keys)
# Loading files
kitten = pyglet.image.load('src/img/PLAYER1.png')
sprite1 = pyglet.sprite.Sprite(img=kitten)
sprite1.y = 0
sprite1.x = 200
dog = pyglet.image.load('src/img/PLAYER2.png')
sprite2 = pyglet.sprite.Sprite(img=dog)
sprite2.y = 0
sprite2.x = 2000
ball = pyglet.image.load('src/img/Ball.png')
sprite3 =pyglet.sprite.Sprite(img=ball)
music = pyglet.media.load('src/aud/BackgroundMusic.wav')
correct = pyglet.media.load('src/aud/1.wav', streaming=False)
hit = pyglet.media.load('src/aud/2.wav', streaming=False)
player = pyglet.media.Player()
pyglet.font.add_file('src/font/PS2P.ttf')
player.queue(music) # These lines are responsible for playing the music
player.play()
# Variables
sprite3.y = 1000
sprite3.x = 500
ballmovx = 10
ballmovy = 10
p1counter = 3
p2counter = 3
mainrunner = True

# Setting up text
p1lives = pyglet.text.Label(f'Player1 | {p1counter}',
                          font_name='Press Start 2P',
                          font_size=36,
                          x=window.width//9, y=window.height-50,
                          anchor_x='center', anchor_y='center')
p2lives = pyglet.text.Label(f'Player2 | {p2counter}',
                          font_name='Press Start 2P',
                          font_size=36,
                          x=window.width//1.12, y=window.height-50,
                          anchor_x='center', anchor_y='center')
won = pyglet.text.Label(f'',
                          font_name='Press Start 2P',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
# Blitting the sprites
@window.event
def on_draw():
    window.clear()
    sprite1.draw()
    sprite2.draw()
    sprite3.draw()
    p1lives.draw()
    p2lives.draw()
    won.draw()
# If escape is pressed close window 
def on_key_press(symbol, modifiers):
    if symbol == key.ESCAPE:
        window.close()
# Update Loop
def update(dt):
    global ballmovx, ballmovy, p1counter, p2counter, mainrunner

    # Winning and losing
    if p1counter == 0:
        mainrunner = False
        won.text = f'Player2 WON'
        pyglet.clock.schedule_once(exit_game, 1)
    elif p2counter == 0:
        mainrunner = False
        won.text = f'Player1 WON'
        pyglet.clock.schedule_once(exit_game, 1)


    # Main event loop
    if mainrunner:
        # Movement
        if keys[key.W]:
            sprite1.y += 12 * (dt * 70) # 12; 70 = Magic Number
        if keys[key.S]:
            sprite1.y -= 12 * (dt * 70) # 12; 70 = Magic Number
        if keys[key.UP]:
            sprite2.y += 12 * (dt * 70) # 12; 70 = Magic Number
        if keys[key.DOWN]:
            sprite2.y -= 12 * (dt * 70) # 12; 70 = Magic Number
        if sprite1.y < 0:
            sprite1.y = 0
        # Collisons Wall
        if sprite1.y > window.height - sprite1.height:
            sprite1.y = window.height - sprite1.height
        if sprite2.y < 0:
            sprite2.y = 0
        if sprite2.y > window.height - sprite1.height:
            sprite2.y = window.height - sprite1.height
        if sprite3.y > (window.height - sprite3.height) or sprite3.y < 0:
            ballmovy = ballmovy * -1
        if sprite3.x > (window.width - sprite3.width):
            ballmovx = ballmovx * -1
            p2counter -= 1
            p2lives.text = f'Player2 | {p2counter}'
            hit.play()
        if sprite3.x < 0:
            ballmovx = ballmovx * -1
            p1counter -= 1
            p1lives.text = f'Player1 | {p1counter}'
            hit.play()
        # Collisions players
        if (sprite3.x < sprite1.x + sprite1.width and 
            sprite3.x + sprite3.width > sprite1.x and 
            sprite3.y < sprite1.y + sprite1.height and 
            sprite3.y + sprite3.height > sprite1.y
        ):
            ballmovx = ballmovx * -1
            correct.play()
        if (sprite3.x < sprite2.x + sprite2.width and 
            sprite3.x + sprite3.width > sprite2.x and 
            sprite3.y < sprite2.y + sprite2.height and 
            sprite3.y + sprite3.height > sprite2.y
        ):
            ballmovx = ballmovx * -1
            ballmovy = ballmovy * -1
            correct.play()
        # Updating ball movement
        sprite3.x += ballmovx * (dt * 70) # 70 = Magic Number
        sprite3.y += ballmovy * (dt * 70) # 70 = Magic Number

# Exits game function
def exit_game(dt):
    pyglet.app.exit()   

# Calls main loop
pyglet.clock.schedule_interval(update, 1/60)  
pyglet.app.run()