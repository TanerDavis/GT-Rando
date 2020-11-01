"""
    DARK AND ICE by Zarby
    https://pastebin.com/PVucvGyy


    [3:19 PM] PsychoManiac: The routine at $80:B631 loads the collision tiles
    [3:20 PM] PsychoManiac: There are two layers, the lower layers is saved for when something is removed from the upper layer
    [3:20 PM] PsychoManiac: This routine also calls $82:C235, which loads the exits for the screen you are

"""






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

            # Item
                hex(0x140) : "Item P1 check : 2 if has 2 items, else 0",
                hex(0x142) : "Item P1 selected : left = 0, right = 2",
                hex(0x143) : "Item1 ID : infos.itemids()",
                hex(0x142) : "Item2 ID : infos.itemids()",
                hex(0x15A) : "Item1 display",
                hex(0x15B) : "Item1 display",
                hex(0x15D) : "Item2 display",
                hex(0x15C) : "Item2 display",


            # P1
                # Related to P1
                hex(0x11D) : "P1 Hearts",
                hex(0x157) : "P1 Lives",
                hex(0x110) : "Xpos P1 (2b)",
                hex(0x113) : "Ypos P1 (2b)",

            hex(0x1144) : "Doors unlocked",
            hex(0x1145) : "Doors unlocked",  # Perhaps 1146? Will have to test further
            hex(0x140B) : "Level's Item : infos.items(2)",
                # Note : the items are always -2. 
                # For example : the bell will be 10 (or A).

            # Credits
                hex(0x1414F) : "Credits : Speed of the THE END Credits",
                hex(0x14137) : "Credits : Where the THE END should stop if password used",




            # Password box
                hex(0x230) : "Password box 1",
                hex(0x231) : "Password box 2",
                hex(0x232) : "Password box 3",
                hex(0x233) : "Password box 4",
                hex(0x234) : "Password box 5",


            # Stored items for the World
                # See range_World_Item()
                    # The idea is that some levels will take the first "letter", some will take the second letters.
                    # For example, if the byte read is 0xAC:
                        # One level that read this specific byte will read A and thus will fetch a Grey Key.
                        # The other level that read the same byte will read C and will fetch the Shovel.
                hex(0x1160) : "World Item 1&2",
                hex(0x1161) : "World Item 3&4",
                hex(0x1162) : "World Item 5&6",
                hex(0x1163) : "World Item 7&8",
                hex(0x1164) : "World Item 9&10",
                hex(0x1165) : "World Item 11&12",
                hex(0x1166) : "World Item 13&14",
                hex(0x1167) : "World Item 15&16",
                hex(0x1168) : "World Item 17&18",
                hex(0x1169) : "World Item 19&20",
                hex(0x116A) : "World Item 21&22"}


        for i in range(0x186b5, 0x186bf+1,2):
            self.infos[hex(i)] = "Dark Room World"
            self.infos[hex(i + 1)] = "Dark Room Level"
        for i in range(0x1c67f, 0x1c692 + 1):
            self.infos[hex(i)] = "Password check"

    def check(self,adress):
        if isinstance(adress,str):
            return adress + " : " + self.infos[adress]
        else:
            return hex(adress) + " : " + self.infos[hex(adress)]

    def seek(self,*seeked):
        print("-----------LIST OF ADRESSES-------------------")
        for i in list(self.infos):
            if all(x in self.infos[i] for x in seeked):
                print(self.check(i))
        print("-----------END OF ADRESSES--------------------")

    def maps(self):
        print("https://www.vgmaps.com/Atlas/SuperNES/index.htm#GoofTroop")

    def password(self,world=None):
        if world == 1:
            print("World 1 : Banana - Red Diamond - Cherry - Banana - Cherry")
        if world == 2:
            print("World 2 : Cherry - Red Diamond - Blue Diamond - Cherry - Banana")
        if world == 3:
            print("World 3 : Red Diamond - Cherry - Blue Diamond - Blue Diamond - Red Diamond")
        if world == 4:
            print("world 4 : Banana - Cherry - Blue Diamond - Red Diamond - Banana")
        elif world is None:
            print("World 1 : Banana - Red Diamond - Cherry - Banana - Cherry")
            print("World 2 : Cherry - Red Diamond - Blue Diamond - Cherry - Banana")
            print("World 3 : Cherry - Blue Diamond - Blue Diamond - Red Diamond")
            print("World 4 : Banana - Cherry - Blue Diamond - Red Diamond - Banana")
        else:
            raise InfosError("World can only be a value of [None-1-2-3-4]")

    def range_dark_rooms(self):
        print("worlds - level")
        for i in range(0x186B5, 0x186BF+1,2):
            print(f'{hex(i)} - {hex(i+1)}')


    def range_password(self, world=None):
        if world is None:
            for worlds in range(1,5):
                offset = 0x1C67F + 5 *(worlds-1)
                print(f'World {worlds} : {hex(offset)} - {hex(offset+1)} - {hex(offset+2)} - {hex(offset+3)} - {hex(offset+4)}')
        elif world in range(1,5):
            offset = 0x1C67F + 5 *(world-1)
            print(f'World {world} : {hex(offset)} - {hex(offset+1)} - {hex(offset+2)} - {hex(offset+3)} - {hex(offset+4)}')
        else:
            raise InfosError("world can only take a value of [None-1-2-3-4]")


    def range_credits(self):
        print(f' Vanilla credits : {hex(0x5F99E)} - {hex(0x5FBFF)}')

    def format_credits_line(self, verbose=False):
        print("[Vspac][Hspac][#][Col][...letters...]")
        if verbose:
            print("Byte 1   : Vspac : Vertical spacing")
            print("Byte 2   : Hspac : Horizontal spacing")
            print("Byte 3   : #     : How many letters to fetch for the line")
            print("Byte 4   : Col   : Color / Properties (see add_credits for more infos)")
            print("Bytes 5+ : The following bytes are the letters")


    def range_World_Item(self, world=None):
        end = {0:0x1164,
               1:0x1165,
               2:0x116A,
               3:0x1163,
               4:0x1168}
        if world in range(5):
            print(f'World {world} range location : {hex(0x1160)} - {hex(end[world])}')
            return
        elif world is None:
            for i in end.keys():
                print(f'World {i} range location : {hex(0x1160)} - {hex(end[i])}')
            return
        else:
            raise InfosError("The world can only be a value of [0-1-2-3-4-None]")


    def values_item_display(self, id=None, adjust=0):
        # The adjust is because the items displayed on the levels are
        # always -2. For example, in inventory, the bell is 12. On the
        # level, it will be 10.

        # note that I've not improved this one since we may not need this one that much.
        items = {"Hookshot" : 2,
        "Candle" : 4,
        "Grey Key" : 6,
        "Gold Key" : 8,
        "Shovel" : 10,
        "Bell" : 12,
        "Bridge" : 14}
        if id is None:
            print("-" * 20)
            for i in items.keys() :
                print(i)
            print("-" * 20)
        else:
            for i in items.keys():
                if id == items[i] -adjust:
                    print(i)
                    return

    def values_items_World(self, value=None):
        # These are the actual values that the game will need to select the items.
        # For placing them in the levels
        values = {0x8: "Hookshot",
                  0x9: "Candle",
                  0xA: "Grey Key",
                  0xB: "Gold Key",
                  0xC: "Shovel",
                  0xD: "Bell",
                  0xE: "Bridge"}
        if value is None:
            for i in values.keys():
                print(f"{hex(i)} - {values[i]}")
        elif value in range(0x8, 0xE +1):
                print(f"{hex(value)} - {values[value]}")
        else:
            raise InfosError(f"value can only take a value in the range of {list(values.keys())}")            

    def values_password(self, value=None):
        values = {0:"Cherry",
                  1:"Banana",
                  2:"Red Gem",
                  3:"Blue Gem",}
        if value is None:
            for i in values.keys():
                print(f'{hex(i)} - {values[i]}')
        elif value in values.keys():
            print(f'{hex(value)} - {values[value]}')
        else:
            raise InfosError(f"Password value can only be a value of {list(values.keys())}")
