from ..utils import BasicSegment
import os
import json
import dateutil.parser
import datetime

class Segment(BasicSegment):
  def add_to_powerline(self):
    CRED_GLYPH_EXPIRED = "\uf83d"
    CRED_GLYPH_VALID = "\uf83e"
    AZURE_GLYPH = "\ufd03"
    home = os.path.expanduser("~")
    token_data = None
    if os.path.isfile("%s/.azure/accessTokens.json" % home):
      with open("%s/.azure/accessTokens.json" % home, encoding='utf-8-sig') as f:
        token_data = json.load(f)

    # Opening azureProfile JSON file
    if os.path.isfile("%s/.azure/azureProfile.json" % home):
      with open("%s/.azure/azureProfile.json" % home, encoding='utf-8-sig') as f:
            data = json.load(f)

      if "subscriptions" in data:
        for x in data["subscriptions"]:
          if x["isDefault"] == True:
            azAccount=x

      token_expires = None
      if token_data:
        for token in token_data:
          if token["_authority"] == "https://login.microsoftonline.com/%s" % azAccount["tenantId"]:
            token_expires = token["expiresOn"]

      creds_valid = None
      two_hours_ago = datetime.datetime.today() - datetime.timedelta(hours=2)
      expires_time = ""
      if token_expires:
        expires = datetime.datetime.strptime( dateutil.parser.parse(token_expires).strftime('%Y/%m/%d %H:%M:%S'), "%Y/%m/%d %H:%M:%S")
        expires_time = "{} {}".format(CRED_GLYPH_VALID,expires.strftime("%H:%M:%S"))
        CurrentDate = datetime.datetime.now()

        creds_valid = expires > CurrentDate

      ## Don't show segment when Credentials are expired for 2 hours
      if (azAccount and expires > two_hours_ago):
        if creds_valid:
          self.powerline.append(" {} {} {}".format(AZURE_GLYPH, azAccount["name"], expires_time),
            self.powerline.theme.AZ_PREFIX_FG,
            self.powerline.theme.AZ_PREFIX_BG)
        else:
          self.powerline.append(" {} {} {}".format(AZURE_GLYPH, azAccount["name"], expires > two_hours_ago),
            self.powerline.theme.AZ_PREFIX_EXP_FG,
            self.powerline.theme.AZ_PREFIX_EXP_BG)
