from ..utils import BasicSegment
import os


class Segment(BasicSegment):
    def add_to_powerline(self):
        ENV_GLYPH = "\ue62e"
        ENVIRONMENT = os.environ.get("ENVIRONMENT") or \
            os.environ.get("ENVIRONMENT")
        if ENVIRONMENT:
            self.powerline.append(" {} {} ".format(ENV_GLYPH, ENVIRONMENT) ,
                self.powerline.theme.ENV_FG,
                self.powerline.theme.ENV_BG)
