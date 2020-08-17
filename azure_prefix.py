from ..utils import BasicSegment
import os


class Segment(BasicSegment):
    def add_to_powerline(self):
        azure_prefix = os.environ.get("AZURE_ACCOUNT_PREFIX")
        if azure_prefix:
            self.powerline.append(" \ufd03 %s " % azure_prefix,
                self.powerline.theme.AZ_PREFIX_FG,
                self.powerline.theme.AZ_PREFIX_BG)
