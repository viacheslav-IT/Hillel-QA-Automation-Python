class Rhombus:
    def __setattr__(self, name, value):
        if name == "side_a":
            if value <= 0:
                raise ValueError("The len of the side should be more than 0")
            super().__setattr__(name, value)

        elif name == "angle_a":
            if not (0 < value < 180):
                raise ValueError("The angle A should be in (0, 180)")
            super().__setattr__("angle_a", value)
            super().__setattr__("angle_b", 180 - value)

        elif name == "angle_b":
            if not (0 < value < 180):
                raise ValueError("The angle B should be in (0, 180)")
            super().__setattr__("angle_b", value)
            super().__setattr__("angle_a", 180 - value)

        else:
            super().__setattr__(name, value)