import matplotlib.font_manager

fonts = matplotlib.font_manager.findSystemFonts()
for font in fonts:
    family = matplotlib.font_manager.FontProperties(fname=font).get_family()
    print(family)
    print(matplotlib.font_manager.FontProperties(fname=font).get_name())
