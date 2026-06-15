class Sword:
    def __init__(self, sword_type):
        self.sword_type = sword_type

    def __add__(self, other):
        sword_type = self.sword_type + other.sword_type
        if sword_type == 'bronzebronze':
            return Sword("iron")
        if sword_type == 'ironiron':
            return Sword("steel")
        raise Exception("cannot craft")
