from pixel2path.px2ph import Px2Ph


options = {
    'filepath': 'pxpath5x9/',
    'characters': 'ABCDEFGHIJ',
    'grid': [5,9],
    'w': 10,
}

font = Px2Ph(**options)
font.rel_path('D')
