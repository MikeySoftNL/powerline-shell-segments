from ..utils import BasicSegment
import os


class Segment(BasicSegment):
    def add_to_powerline(self):
        KB_GLYPH = "\uf23e"
        KB_TEST=os.path.isdir('/keybase/team/digitalsurvivor/bot/home/.aws')

        if KB_TEST:
            self.powerline.append(" kb {} ".format(KB_GLYPH) ,
                                  self.powerline.theme.KB_FG,
                                  self.powerline.theme.KBUP_BG)
        else:
            self.powerline.append(" kb {} ".format(KB_GLYPH) ,
                                  self.powerline.theme.KB_FG,
                                  self.powerline.theme.KBDOWN_BG)
