class Character:
    def __init__(self):
        self.height = None
        self.hair_color = None
        self.eye_color = None
        self.side = None
        self.deeds = []


class CharacterBuilder:
    def set_height(self, height):
        pass

    def set_hair_color(self, color):
        pass

    def set_eye_color(self, color):
        pass

    def add_deed(self, deed):
        pass

    def get_result(self):
        pass


class HeroBuilder(CharacterBuilder):
    def __init__(self):
        self.character = Character()
        self.character.side = "Good"

    def set_height(self, height):
        self.character.height = height
        return self

    def set_hair_color(self, color):
        self.character.hair_color = color
        return self

    def set_eye_color(self, color):
        self.character.eye_color = color
        return self

    def add_deed(self, deed):
        self.character.deeds.append("Good deed: " + deed)
        return self

    def get_result(self):
        return self.character


class EnemyBuilder(CharacterBuilder):
    def __init__(self):
        self.character = Character()
        self.character.side = "Evil"

    def set_height(self, height):
        self.character.height = height
        return self

    def set_hair_color(self, color):
        self.character.hair_color = color
        return self

    def set_eye_color(self, color):
        self.character.eye_color = color
        return self

    def add_deed(self, deed):
        self.character.deeds.append("Evil deed: " + deed)
        return self

    def get_result(self):
        return self.character


class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct_epic_character(self, height, hair, eye, deed):
        return (self.builder
                .set_height(height)
                .set_hair_color(hair)
                .set_eye_color(eye)
                .add_deed(deed)
                .get_result())


if __name__ == "__main__":
    hero_builder = HeroBuilder()
    director = Director(hero_builder)
    hero = director.construct_epic_character(180, "Blonde", "Blue", "Saved the world")

    enemy_builder = EnemyBuilder()
    director.builder = enemy_builder
    enemy = director.construct_epic_character(195, "Bald", "Red", "Stole the sun")

    print(hero.side + " character created with hair: " + hero.hair_color + ". Deeds: " + str(hero.deeds))
    print(enemy.side + " character created with hair: " + enemy.hair_color + ". Deeds: " + str(enemy.deeds))