from GameFrame import RoomObject
from Objects.Title import Title
class Title(RoomObject):
    """
    The object for displaying the title
    """
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        # set image
        image = self.load_image("Title.png")
        self.set_image(image,800,350)

        # add title object
        self.add_room_object(Title(self, 240, 200))