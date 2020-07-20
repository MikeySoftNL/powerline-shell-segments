from ..utils import BasicSegment
import os


class Segment(BasicSegment):
    def add_to_powerline(self):
        AWS_GLYPH = "\ue62e"
        aws_profile = os.environ.get("ENVIRONMENT") or \
            os.environ.get("ENVIRONMENT")
        if aws_profile:
            self.powerline.append(" {} {} ".format(AWS_GLYPH, os.path.basename(aws_profile)) ,
                                  118,
                                  56)
