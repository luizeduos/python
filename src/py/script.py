from browser import document, html, timer, window

canvas = document["pongCanvas"]
context = canvas.getContext("2d")

class Paddle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.score = 0

    def draw(self):
        context.fillStyle = self.color
        context.fillRect(self.x, self.y, self.width, self.height)

    def move(self, dy):
        if 0 <= self.y + dy <= canvas.height - self.height:
            self.y += dy

class Ball:
    def __init__(self, x, y, radius, color, dx, dy):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.dx = dx
        self.dy = dy

    def draw(self):
        context.beginPath()
        context.arc(self.x, self.y, self.radius, 0, 2 * 3.14)
        context.fillStyle = self.color
        context.fill()
        context.closePath()

    def move(self):
        self.x += self.dx
        self.y += self.dy

        if self.y <= 0 or self.y >= canvas.height:
            self.dy = -self.dy

        if self.x <= 0 or self.x >= canvas.width:
            self.dx = -self.dx

player1 = Paddle(20, canvas.height // 2 - 60, 10, 120, "white")
player2 = Paddle(canvas.width - 30, canvas.height // 2 - 60, 10, 120, "white")
ball = Ball(canvas.width // 2, canvas.height // 2, 10, "white", 4, 4)

def draw():
    context.clearRect(0, 0, canvas.width, canvas.height)
    player1.draw()
    player2.draw()
    ball.draw()

def update():
    ball.move()
    # Simple AI for player2
    if ball.y > player2.y + player2.height / 2:
        player2.move(6)
    elif ball.y < player2.y + player2.height / 2:
        player2.move(-6)
    # Check collision with paddles
    if (ball.x - ball.radius < player1.x + player1.width and
        player1.y < ball.y < player1.y + player1.height):
        ball.dx = -ball.dx
    if (ball.x + ball.radius > player2.x and
        player2.y < ball.y < player2.y + player2.height):
        ball.dx = -ball.dx
    draw()

def move_player1(event):
    if event.key == "ArrowUp":
        player1.move(-20)
    elif event.key == "ArrowDown":
        player1.move(20)

document.bind("keydown", move_player1)
timer.set_interval(update, 30)