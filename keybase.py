from ..utils import BasicSegment
import os


class Segment(BasicSegment):
    def add_to_powerline(self):
        KB_GLYPH = "\uf23e"
        KB_TEST=os.path.isdir('/keybase/team/digitalsurvivor/bot/home/.aws')

        if KB_TEST:
            self.powerline.append(" kb {} ".format(KB_GLYPH) ,
                                  239,
                                  46)
        else:
            self.powerline.append(" kb {} ".format(KB_GLYPH) ,
                                  239,
                                  173)
