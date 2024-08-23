class Slideshow:
    def __init__(self, slides):
        self.slides = slides
        self.current = 1

    def view_next_slide(self):
        self.current += 1

    def play(self):
        while self.current <= self.slides:
            print('Slide', self.current)
            self.view_next_slide()

slideshow = Slideshow(5)
slideshow.play()