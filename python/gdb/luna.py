  # pip install freegames

# import modules
import turtle as t
from freegames import square, vector


# Player 1 Controls - Move Left: 'a', Move Right: 'd'
# Player 2 Controls - Move Left: 'j', Move Right: 'l'

# Set window title, color and icon
t.title("Tron")
root = t.Screen()._root
root.iconbitmap("logo-ico.ico")
t.bgcolor('#1a1a1a')


player_1xy = vector(-100, 0)
player_1aim = vector(4, 0)
player_1body = set()

player_2xy = vector(100, 0)
player_2aim = vector(-4, 0)
player_2body = set()

#   Functions
# Return True if head inside screen
def inside(head):
    return -200 < head.x < 200 and -200 < head.y < 200

# Advance players and draw game
def draw():
    player_1xy.move(player_1aim)
    player_1head = player_1xy.copy()

    player_2xy.move(player_2aim)
    player_2head = player_2xy.copy()

    if not inside(player_1head) or player_1head in player_2body:
        print('Player BLUE wins!')
        return

    if not inside(player_2head) or player_2head in player_1body:
        print('Player RED wins!')
        return

    player_1body.add(player_1head)
    player_2body.add(player_2head)

    square(player_1xy.x, player_1xy.y, 3, '#ff0000')
    square(player_2xy.x, player_2xy.y, 3, '#00ccff')
    t.update()
    t.ontimer(draw, 50)

t.setup(420, 420, 370, 0)
t.hideturtle()
t.tracer(False)
t.listen()

# Set Keyboard Controls
t.onkey(lambda: player_1aim.rotate(90), 'a')
t.onkey(lambda: player_1aim.rotate(-90), 'd')
t.onkey(lambda: player_2aim.rotate(90), 'j')
t.onkey(lambda: player_2aim.rotate(-90), 'l')
draw()
t.done()