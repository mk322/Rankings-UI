from tkinter import *

class Proposal_Box:
    def __init__(self, canvas, reviewer, pos, prop=None, color="white") -> None:
        if prop == None:
            text = reviewer
            self.rectag = (f"{reviewer}", )
            self.textag = (f"{reviewer}text", )
        else:
            self.rectag = (f"{reviewer}", f"{prop}")
            self.textag = (f"{reviewer}text", f"{prop}text")
            text = prop
        self.rect = canvas.create_rectangle(
            pos[0], pos[2], pos[1], pos[3],
            outline="#fb0",
            fill=color,
            tag=self.rectag
        )
        self.text = canvas.create_text((pos[0]+pos[1])//2 ,(pos[2]+pos[3])//2, text=text, tag=self.textag)
    