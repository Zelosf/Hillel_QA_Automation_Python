class Romb:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, key, value):
        if key == 'side_a':
            if value <= 0:
                raise ValueError("Довжина сторони повинна бути більше 0.")
            super().__setattr__(key, value)

        elif key == 'angle_a':
            if not (0 < value < 180):
                raise ValueError("Кут повинен бути в межах від 0 до 180.")
            super().__setattr__(key, value)
            super().__setattr__('angle_b', 180 - value)

        elif key == 'angle_b':
            raise AttributeError("angle_b встановлюється автоматично, змінювати його напряму не можна.")

        else:
            super().__setattr__(key, value)

    def __str__(self):
        return f"Ромб: side = {self.side_a}, angle_a = {self.angle_a}°, angle_b = {self.angle_b}°"


romb1 = Romb(side_a=10, angle_a=60)
print(romb1)
