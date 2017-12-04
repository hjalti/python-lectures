from pathlib import Path

dir_structure = (
    'test', (
        ('dir1', ()),
        ('dir2', (
            ('dir21', ()),
            ('dir22', (
                ('dir221', ()),
                ('file221.txt', None),
            )),
            ('dir23', ()),
            ('file21.txt', None),
        )),
        ('dir3', ()),
        ('dir4', (
            ('dir41', (
                ('dir411', ()),
                ('file411.txt', None),
                ('file412.txt', None),
            )),
            ('dir42', (
                ('dir421', ()),
                ('file421.txt', None),
            )),
            ('dir43', ()),
            ('file41.txt', None),
        )),
        ('dir5', ()),
        ('file1.txt', None),
        ('file2.txt', None),
        ('file3.txt', None),
    ),
)

def make_structure(struct, root):
    name, children = struct
    if children is None:
        (root / name).touch()
    else:
        new_dir = root / name
        new_dir.mkdir()
        for st in children:
            make_structure(st, new_dir)

make_structure(dir_structure, Path('.'))
