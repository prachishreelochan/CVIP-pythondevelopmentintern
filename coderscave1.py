import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x200")

        pygame.init()
        pygame.mixer.init()

        self.playlist = []

        self.create_widgets()

    def create_widgets(self):
        # Playlist Box
        self.playlist_box = tk.Listbox(self.root, selectmode=tk.SINGLE)
        self.playlist_box.pack(fill=tk.BOTH, expand=True)

        # Buttons
        self.add_button = tk.Button(self.root, text="Add", command=self.add_song)
        self.add_button.pack(fill=tk.BOTH, expand=True)

        self.play_button = tk.Button(self.root, text="Play", command=self.play_song)
        self.play_button.pack(fill=tk.BOTH, expand=True)

        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_song)
        self.pause_button.pack(fill=tk.BOTH, expand=True)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_song)
        self.stop_button.pack(fill=tk.BOTH, expand=True)

    def add_song(self):
        song_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
        if song_path:
            song_name = os.path.basename(song_path)
            self.playlist_box.insert(tk.END, song_name)
            self.playlist.append(song_path)

    def play_song(self):
        selected_song_index = self.playlist_box.curselection()
        if selected_song_index:
            selected_song_index = int(selected_song_index[0])
            selected_song = self.playlist[selected_song_index]

            pygame.mixer.music.load(selected_song)
            pygame.mixer.music.play()

    def pause_song(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()

    def stop_song(self):
        pygame.mixer.music.stop()

if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()

