from ..utils import BasicSegment
import os


class Segment(BasicSegment):
    def add_to_powerline(self):
        AWS_GLYPH = "󰸏"
        REGION_GLYPH = ""
        aws_profile = os.environ.get("AWS_PROFILE") or \
            os.environ.get("AWS_DEFAULT_PROFILE")
        aws_region = os.environ.get("AWS_REGION") or \
            os.environ.get("AWS_DEFAULT_REGION")
        if aws_profile:
            if aws_region == None:
                aws_text = "{}".format(os.path.basename(aws_profile))
            else:
                aws_text = "{} | {} {}".format(os.path.basename(aws_profile),REGION_GLYPH,aws_region)
            self.powerline.append(f" {AWS_GLYPH} {aws_text} ",
                                  self.powerline.theme.AWS_PROFILE_FG,
                                  self.powerline.theme.AWS_PROFILE_BG)
