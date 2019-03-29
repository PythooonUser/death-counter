import time
import keyboard


class DeathCounter(object):
    def __init__(self):
        with open("deaths.dat") as file:
            self.deaths = int(file.read().split()[1])

        keyboard.on_press_key("f1", self.increment)
        keyboard.on_press_key("f2", self.decrement)

    def increment(self, event):
        self.deaths += 1
        self.update_file()

    def decrement(self, event):
        self.deaths -= 1
        self.update_file()

    def update_file(self):
        with open("deaths.dat", mode="w") as file:
            file.write("deaths: " + str(self.deaths))

    def run(self):
        while True:
            try:
                time.sleep(0.25)
            except KeyboardInterrupt:
                return


def main():
    death_counter = DeathCounter()
    death_counter.run()

if __name__ == '__main__':
    main()
