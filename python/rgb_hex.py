rgb = lambda r, g, b: "{:02X}{:02X}{:02X}".format(
    max(0, min(255, r)), max(0, min(255, g)), max(0, min(255, b))
)
