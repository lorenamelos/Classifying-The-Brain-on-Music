labels = {
    0: "Ambient Music",
    1: "Country Music",
    2: "Heavy Metal",
    3: "Rock 'n Roll",
    4: "Classical Symphonic"
}

def int_to_music_label(integers: list[int]) -> list[str]:
    return [labels.get(integer) for integer in integers]


