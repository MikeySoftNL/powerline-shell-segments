from ..utils import BasicSegment
import os


class Segment(BasicSegment):
    def add_to_powerline(self):
        aws_profile = os.environ.get("AWS_PROFILE") or \
            os.environ.get("AWS_DEFAULT_PROFILE")
        aws_region = os.environ.get("AWS_REGION") or \
            os.environ.get("AWS_DEFAULT_REGION")
        if aws_profile:
            aws_text = "{} | \uf454 {}".format(os.path.basename(aws_profile),aws_region)
            self.powerline.append(" \ue7ad %s " % aws_text,
                                  self.powerline.theme.AWS_PROFILE_FG,
                                  self.powerline.theme.AWS_PROFILE_BG)
