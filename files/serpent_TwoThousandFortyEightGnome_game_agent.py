from serpent.game_agent import GameAgent
import random

class SerpentTwoThousandFortyEightGnomeGameAgent(GameAgent):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.frame_handlers["PLAY"] = self.handle_play

        self.frame_handler_setups["PLAY"] = self.setup_play

        self.analytics_client = None

    def setup_play(self):
        pass

    def handle_play(self, game_frame):
        action_possibilites = ["left", "right", "up", "down"]

        for i, game_frame in enumerate(self.game_frame_buffer.frames):
            self.visual_debugger.store_image_data(
                game_frame.frame,
                game_frame.frame.shape,
                str(i)
            )

        action_choice = random.choice(action_possibilites)
        self.input_controller.tap_key(action_choice)

        print("This turn, I chose to press", action_choice)