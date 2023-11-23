from ..utils import BasicSegment
import os
import re
import dateutil.parser
import datetime

class Segment(BasicSegment):
    def add_to_powerline(self):
        CRED_GLYPH_EXPIRED = "󰌾"
        CRED_GLYPH_VALID = "󰌿"
        contents = None
        home = os.path.expanduser("~")
        if os.path.isfile("%s/.aws/credentials" % home):
            f= open("%s/.aws/credentials" % home ,"r")
            contents = f.read()

            expires = None
            expiration = []
            creds_valid = []

            for ex in re.findall('(?<=x_security_token_expires =)(.*)', contents):
                token_expires = ex.strip()
                expires = datetime.datetime.strptime( dateutil.parser.parse(token_expires).strftime('%Y/%m/%d %H:%M:%S'), "%Y/%m/%d %H:%M:%S")
                expiration.append(dateutil.parser.parse(token_expires).strftime('%H:%M'))
                CurrentDate = datetime.datetime.now()

                creds_valid.append(expires > CurrentDate)

            if False in creds_valid and True in creds_valid:
                i = 0
                cred_text = []
                while i < len(creds_valid):
                  if creds_valid[i]:
                    cred_text.append("\033[1;32;74m %s" % expiration[i])
                  else:
                    cred_text.append("\033[1;31;74m %s" % expiration[i])
                  i += 1
                cred_text = " {} {} ".format(CRED_GLYPH_VALID," |".join(cred_text))
                self.powerline.append(" \ue7ad %s " % cred_text,
                    self.powerline.theme.AWS_CRED_VALID_FG,
                    self.powerline.theme.AWS_CRED_HALFVALID_BG)
            elif True in creds_valid:
                cred_text = " {} {} ".format(CRED_GLYPH_VALID, " | ".join(expiration))
                self.powerline.append(" \ue7ad %s " % cred_text,
                    self.powerline.theme.AWS_CRED_VALID_FG,
                    self.powerline.theme.AWS_CRED_VALID_BG)
            else:
                cred_text = " {} {} ".format(CRED_GLYPH_EXPIRED, " | ".join(expiration))
                self.powerline.append(" \ue7ad %s " % cred_text,
                    self.powerline.theme.AWS_CRED_EXP_FG,
                    self.powerline.theme.AWS_CRED_EXP_BG)
