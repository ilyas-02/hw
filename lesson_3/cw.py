class Dino:

    def __init__(self, dino_name):
        self.dino_name = dino_name

    def get_dino_name(self):
        pass


class Shark:

    def __init__(self, shark_name):
        self.shark_name = shark_name

    def _get_shark_name(self):
        pass


class Mixin(Dino, Shark):
    pass


class Mix(Mixin):
    pass