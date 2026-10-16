"""Load the chapter modules."""


def install(chapter, roman, italic, claims):
    from manuscript.parts import part_a, part_b, part_c, part_d

    part_a.add(chapter, roman, italic, claims)
    part_b.add(chapter, roman, italic, claims)
    part_c.add(chapter, roman, italic, claims)
    part_d.add(chapter, roman, italic, claims)
