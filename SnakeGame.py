import pygame
import sys


SCREEN_SIZE = (800, 600)

SNAKE_ICON = "unnamed.jpg"

GAME_TITLE = "Snake"

INITIAL_GAME_SPEED = 10

BACKGROUND_COLOR = (0, 0, 0)


def initialize_pygame():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    icon = pygame.image.load(SNAKE_ICON)
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()
    return screen, clock


def initialize_game_state():
    game_state = {
        "program_running": True,
        "game_running": False,
        "game_paused": False,
        "game_speed": INITIAL_GAME_SPEED,
        "game_score": 0
    }
    return game_state


def perform_shutdown():
    pygame.quit()
    sys.exit()

def get_events():
    events = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            events.append("quit")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                events.append("up")
            elif event.key == pygame.K_s:
                events.append("down")
            elif event.key == pygame.K_a:
                events.append("left")
            elif event.key == pygame.K_d:
                events.append("right")
            elif event.key == pygame.K_RETURN:
                events.append("enter")
            elif event.key == pygame.K_SPACE:
                events.append("space")
            elif event.key == pygame.K_ESCAPE:
                events.append("escape")
    return events

def update_game_state(events, game_state):
    if "quit" in events:
        game_state["program_running"] = False
    elif not game_state["game_running"]:
        if "escape" in events:
            game_state["program_running"] = False
        elif "enter" in events:
            initialize_new_game(game_state)
            game_state["game_running"] = True
    elif game_state["game_paused"]:
        if "escape" in events:
            game_state["game_running"] = False
        elif "space" in events:
            game_state["game_paused"] = False
        else:
            if "escape" in events or "space" in events:
                game_state["game_paused"] = True
            if "w" in events:
                pass
            if "s" in events:
                pass
            if "a" in events:
                pass
            if "d" in events:
                pass


def initialize_new_game(game_state):
    game_state["game_paused"] = False
    game_state["score"] = 0

def update_screen(screen, game_state):
    screen.fill((BACKGROUND_COLOR))
    pygame.display.flip()


def main():
    screen, clock = initialize_pygame()
    game_state = initialize_game_state()
    while game_state["program_running"]:
        clock.tick(game_state["game_speed"])
        events = get_events()
        print(events)
        update_game_state(events,game_state)
        update_screen(screen, game_state)
    perform_shutdown()

main()

# pygame.init()
# xscreen = pygame.display.set_mode((640, 480))
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#
#         xscreen.fill((0, 0, 0))
#         pygame.display.flip()
