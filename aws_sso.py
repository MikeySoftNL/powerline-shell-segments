from ..utils import BasicSegment
import os
import json
import glob
import re
import datetime
import dateutil.parser

home = os.path.expanduser("~")
aws_sso_folder = f'{home}/.aws/sso/cache'
CRED_GLYPH_EXPIRED = "\uf83d"
CRED_GLYPH_VALID = "\uf83e"

files = glob.glob(f'{aws_sso_folder}/*.json')
tokens = []
tokens_valid = []
for file in files:
  if not 'botocore-client' in file:
    f = open(file)
    content = json.load(f)
    f.close()

    try:
      if 'startUrl' and 'expiresAt' in content :
        url = content["startUrl"]
        host = re.search('(?<=//).*(?=[/])',url)
        account = host.group(0).split(".")[0]
        expiresAt = content["expiresAt"]
        expires = datetime.datetime.strptime( dateutil.parser.parse(expiresAt).strftime('%Y/%m/%d %H:%M:%S'), "%Y/%m/%d %H:%M:%S")
        expires_time = expires.strftime("%H:%M:%S")
        CurrentDate = datetime.datetime.now()

        creds_valid = expires > CurrentDate
        tokens_valid.append(creds_valid)

        GLYPH = CRED_GLYPH_VALID if creds_valid else CRED_GLYPH_EXPIRED
        tokens.append(f'{account}:{GLYPH} {expires_time}')
    except Exception as e:
      print(e)

text = " | ".join(tokens)
class Segment(BasicSegment):
    def add_to_powerline(self):
      if False in tokens_valid and True in tokens_valid:
        self.powerline.append(" \ue7ad %s " % text,
                          self.powerline.theme.AWS_CRED_VALID_FG,
                          self.powerline.theme.AWS_CRED_HALFVALID_BG)
      elif True in tokens_valid:
        self.powerline.append(" \ue7ad %s " % text,
                          self.powerline.theme.AWS_CRED_VALID_FG,
                          self.powerline.theme.AWS_CRED_VALID_BG)
      else:
        self.powerline.append(" \ue7ad %s " % text,
                          self.powerline.theme.AWS_CRED_EXP_FG,
                          self.powerline.theme.AWS_CRED_EXP_BG)
