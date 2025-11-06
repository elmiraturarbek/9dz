class TV:
    def turn_on(self):
        print("TV is turned on.")

    def turn_off(self):
        print("TV is turned off.")

    def set_channel(self, channel):
        print(f"TV channel set to {channel}.")


class AudioSystem:
    def turn_on(self):
        print("Audio system is turned on.")

    def set_volume(self, level):
        print(f"Audio volume set to {level}.")

    def turn_off(self):
        print("Audio system is turned off.")


class DVDPlayer:
    def play(self):
        print("DVD is now playing.")

    def pause(self):
        print("DVD is paused.")

    def stop(self):
        print("DVD stopped.")


class GameConsole:
    def turn_on(self):
        print("Game console is turned on.")

    def start_game(self, game_name):
        print(f"Starting the game '{game_name}'.")


class HomeTheaterFacade:
    def __init__(self, tv, audio, dvd, console):
        self.tv = tv
        self.audio = audio
        self.dvd = dvd
        self.console = console

    def watch_movie(self):
        print("\n--- Preparing to watch a movie ---")
        self.tv.turn_on()
        self.tv.set_channel("HDMI 1")
        self.audio.turn_on()
        self.audio.set_volume(30)
        self.dvd.play()
        print("Movie mode is ON.\n")

    def stop_movie(self):
        print("\n--- Stopping the movie ---")
        self.dvd.stop()
        self.audio.turn_off()
        self.tv.turn_off()
        print("Movie mode is OFF.\n")

    def play_game(self, game_name):
        print("\n--- Starting a video game ---")
        self.tv.turn_on()
        self.tv.set_channel("HDMI 2")
        self.audio.turn_on()
        self.audio.set_volume(40)
        self.console.turn_on()
        self.console.start_game(game_name)
        print("Game mode is ON.\n")

    def listen_music(self):
        print("\n--- Listening to music ---")
        self.tv.turn_on()
        self.tv.set_channel("AUDIO")
        self.audio.turn_on()
        self.audio.set_volume(20)
        print("Music mode is ON.\n")

    def turn_off_all(self):
        print("\n--- Turning off all systems ---")
        self.dvd.stop()
        self.audio.turn_off()
        self.tv.turn_off()
        print("All systems are turned off.\n")


if __name__ == "__main__":
    tv = TV()
    audio = AudioSystem()
    dvd = DVDPlayer()
    console = GameConsole()

    home_theater = HomeTheaterFacade(tv, audio, dvd, console)

    home_theater.watch_movie()
    home_theater.stop_movie()

    home_theater.play_game("The Witcher 3")
    home_theater.listen_music()
    home_theater.turn_off_all()
