from pynput.mouse import Button, Controller
import keyboard
import random
import time

mouse = Controller()
EXIT_KEY = "ctrl"
WAIT_TIME = 5

interval = 0
delta = 0
eat = 1440


def click_and_wait(seconds):
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(seconds)


def consume():
    mouse.press(Button.right)
    time.sleep(3)
    mouse.release(Button.right)


def ask_interval():
    try:
        global interval
        interval = float(input("Enter the interval between clicks in SECONDS: "))
    except ValueError:
        ask_interval()


def ask_delta():
    try:
        global delta
        delta = float(input("Enter the maximum delta between clicks in SECONDS: "))
    except ValueError:
        ask_delta()


def ask_eat_timer():
    try:
        global eat
        eat = float(input("How frequently should the player try to eat in MINUTES: "))
    except ValueError:
        ask_eat_timer()


def autoclicker_core(seconds, diff, eat_timer):
    total_time_passed = 0
    while not keyboard.is_pressed(EXIT_KEY):
        if total_time_passed >= eat_timer * 60:
            print("\nEating...\n")
            consume()
            total_time_passed = 0
        wait = round(random.uniform(seconds - diff, seconds + diff), 3)
        click_and_wait(wait)
        print(f"Interval: {wait}")
        total_time_passed += wait


mode = input("[S]tatic or [R]andom? ").lower()
while mode not in ["s", "r"]:
    mode = input("Enter the initial of desired mode: ")

if mode == "s":
    ask_interval()
    ask_eat_timer()
else:
    ask_interval()
    ask_delta()
    ask_eat_timer()

print(f"Hold [{EXIT_KEY}] to stop.\n"
      f"Focus on the desired window. Clicking in ", end="")
for i in range(WAIT_TIME, 0, -1):
    if i == 1:
        print(f"{i}\n")
    else:
        print(f"{i} ", end="")
    time.sleep(1)

autoclicker_core(interval, delta, eat)
print("\nProcess stopped successfully.")
input("Press [Enter] to close program.")
