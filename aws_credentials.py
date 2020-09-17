from ..utils import BasicSegment
import os
import re
import dateutil.parser
import datetime 

class Segment(BasicSegment):
    def add_to_powerline(self):
        CRED_GLYPH_EXPIRED = "\uf83d"
        CRED_GLYPH_VALID = "\uf83e"
        home = os.path.expanduser("~")
        f= open("%s/.aws/credentials" % home ,"r")
        contents = f.read()

        x_security_token_expires = re.search('(?<=x_security_token_expires =)(.*)', contents)

        if x_security_token_expires:
            token_expires = x_security_token_expires.groups()[0].strip()
            expires = datetime.datetime.strptime( dateutil.parser.parse(token_expires).strftime('%Y/%m/%d %H:%M:%S'), "%Y/%m/%d %H:%M:%S")
            CurrentDate = datetime.datetime.now()

            creds_valid = expires > CurrentDate

        if creds_valid:
            cred_text = " {} {} ".format(CRED_GLYPH_VALID, expires)
            self.powerline.append(" \ue7ad %s " % cred_text,
                self.powerline.theme.AWS_CRED_VALID_FG,
                self.powerline.theme.AWS_CRED_VALID_BG)
        else:
            cred_text = " {} {} ".format(CRED_GLYPH_EXPIRED, expires)
            self.powerline.append(" \ue7ad %s " % cred_text,
                self.powerline.theme.AWS_CRED_EXP_FG,
                self.powerline.theme.AWS_CRED_EXP_BG)
