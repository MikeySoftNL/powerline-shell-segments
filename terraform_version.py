from ..utils import BasicSegment
import os
import subprocess
import re

tf_version = None
try:
    subprocess.call(["terraform"], stdout=open(os.devnull, 'wb'))
    tf_version = subprocess.Popen(["terraform version"], stdout=subprocess.PIPE, shell=True)
    (out, err) = tf_version.communicate()
except FileNotFoundError:
    # handle file not found error.
    print()

class Segment(BasicSegment):
    def add_to_powerline(self):
        if tf_version:
            version=re.search('(?<=Terraform v).*', out.decode('utf-8')) #e7a3

            if version.group():
                self.powerline.append(" \uf292 v%s " % version.group(),
                        self.powerline.theme.TF_PROFILE_FG,
                        self.powerline.theme.TF_PROFILE_BG)
