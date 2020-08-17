from ..utils import BasicSegment
import os, re


class Segment(BasicSegment):
    def add_to_powerline(self):
        k8s_glyph="\u2388"
        eks = os.environ.get("KUBECONFIG") 
        if eks:
            try:
                f = open(os.environ.get("KUBECONFIG"), "r")
                cluster=re.search('(?<=name: ).*',f.read(), re.IGNORECASE).group()
                self.powerline.append(" {} {} ".format(k8s_glyph,cluster),
                                  self.powerline.theme.EKS_FG,
                                  self.powerline.theme.EKS_BG)
            except:
                cluster=""
            
