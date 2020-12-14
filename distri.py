from ..utils import BasicSegment
import csv

RELEASE_DATA = {}

class Segment(BasicSegment):
    def get_glyph(self, argument):
        Ubuntu_glyph = "\uf31c"
        CentOS_glyph = "\uf304"
        RedHat_glyph = "\uf316"
        Debian_glyph = "\uf306"
        Amazon_glyph = "\uf52c"
        Alpine_glyph = "\uf300"
        Linux_glyph  = "\uf17c"

        switcher = {
            "Ubuntu": Ubuntu_glyph,
            "CentOS": CentOS_glyph,
            "RedHat": RedHat_glyph,
            "Debian": Debian_glyph,
            "AmazonLinux": Amazon_glyph,
            "Alpine": Alpine_glyph,
        }
        return switcher.get(argument, Linux_glyph)

    def add_to_powerline(self):
        with open("/etc/os-release") as f:
            reader = csv.reader(f, delimiter="=")
            for row in reader:
                if row:
                    RELEASE_DATA[row[0]] = row[1]

        if RELEASE_DATA["ID"] in ["debian", "raspbian"]:
            with open("/etc/debian_version") as f:
                DEBIAN_VERSION = f.readline().strip()
            major_version = DEBIAN_VERSION.split(".")[0]
            version_split = RELEASE_DATA["VERSION"].split(" ", maxsplit=1)
            if version_split[0] == major_version:
                # Just major version shown, replace it with the full version
                RELEASE_DATA["VERSION"] = " ".join([DEBIAN_VERSION] + version_split[1:])

        # #print("{} {}".format(get_glyph(RELEASE_DATA["NAME"]), RELEASE_DATA["VERSION_ID"]))
        self.powerline.append(
            " {} {} ".format(self.get_glyph(RELEASE_DATA["NAME"]) , RELEASE_DATA["VERSION_ID"]),
            self.segment_def.get("fg_color", self.powerline.theme.LINUX_FG),
            self.segment_def.get("bg_color", self.powerline.theme.LINUX_BG))
