import toga


class HelloWorld(toga.App):
    def startup(self):
        """Construct and show the Toga application."""
        self.main_window = toga.MainWindow()
        self.main_window.show()


def main():
    return HelloWorld()
