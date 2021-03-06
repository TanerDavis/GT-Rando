"""
[9:50 AM] dan jia: how maps are loaded, bank offsets are bank * $8000, ie 3:2300 is 4*$8000+$2300:
no compression it seems, just nested metatiling
0:038d is the function you know about the dma transfers, it processes 8 byte structs
  - 0 - transfer params
  - 1/2 - vram addr divided by 2
  - 3/4 - num bytes
  - 5/6/7 - src addr and bank
  - $1800 is the start of dma transfer structs
  - $40 is the idx to stop at when dma transferring
  - eg for the 1st room, $40 contains #$70, $1860 and $1868 contains:
    - $01, $5000 (bg1 / 2), $0800 (entire screen), 7f:e000 (src of tilemap bytes in wram)
    - $01, $5800 (bg2 / 2), $0800 (entire screen), 7f:e800
0:34c2 is the function for loading a room's tiles
  - uses $b6 (room group), and $b7 (room idx) to get data from 3:0ce7
  - there are 5 room groups, the 1st 5 bytes from above are offsets into data to get room data for each group (2 bytes per room)
  - eg group 0's byte at 3:0ce7 contains 5, room 1 would be an offset of 5+1*2
  - the 2 bytes reference the idx of 2 $40-byte structs for bg1 and bg2 for the room
the $40-byte structs are 8x8 metatiles per screen
  - rows of 8 metatiles are processed at 0:3535
  - individual metatiles (4x4 tiles) are processed and sent to 7f:e000+ at 0:3563 
  - each metatile is composed of 4 more 2x2 metatiles
  - each of those metatiles are composed of 4 tiles
the data is gotten across banks 9 to B
how 16x16 and 8x8 metatiles reference their address source is a bit long to explain, but this should give you some groundwork to do some level editing
[10:23 AM] dan jia: a screen's metatiles get their high byte source from [13]= 9:b700 + room val * $20 ($20 instead of $40, as the high byte for 2 metatiles share the same byte, but different nybbles), low byte is [10]= 9:8000 + room val * $40
individual 4x4 metatiles get their high byte source from (19)=a:c000 + metatile idx * 2 and low byte from (16)=a:8000 + metatile idx * 4 (4 inner tiles), again using the same split high byte nybbles
those inner 4 2x2 metatiles get 4 values from the 4 addresses above in bank B, so 16 values for a 4x4 individual metatile"""

class InfosError(BaseException):
    pass
class infos:
    """
        This class is more of a tool for me. I will store my findings of infos here.
        And if I need to get an info during my coding, I'll simply call this class and then ask it to
        Retrieve the things I need.
    """

    def __init__(self):
        self.infos = {
            # When searching for a keyword, always use a capital for the first letter.
            # general
                hex(0xB6) : "current World (1b)",
                hex(0xB7) : "current Level (1b)",
                hex(0xBD) : "Player count : 1 if 1P, 3 if 2P",
                hex(0xF0) : "Current world 'milliseconds'",
                hex(0xF1) : "Current world seconds",
                hex(0xF2) : "Current world minutes",
                hex(0xF3) : "Current world hours (Max value is 9!)",
                hex(0xF5) : "Total Seconds played",
                hex(0xF6) : "Total Minutes played",
                hex(0xF7) : "Total Hours played",

                hex(0x21C) : "Current(?) boss HP",
                hex(0x21D) : "Current(?) boss HP",

            # P1
                # Related to P1
                hex(0x11D) : "P1 Hearts",
                hex(0x157) : "P1 Lives",
                hex(0x110) : "Xpos P1 (2b)",
                hex(0x113) : "Ypos P1 (2b)",

            hex(0x1144) : "Doors unlocked",
            hex(0x1145) : "Doors unlocked",  # Perhaps 1146? Will have to test further

            # Credits
                hex(0x1414F) : "Credits : Speed of the THE END Credits",
                hex(0x14137) : "Credits : Where the THE END should stop if password used",
        }


    def maps(self):
        print("https://www.vgmaps.com/Atlas/SuperNES/index.htm#GoofTroop")
