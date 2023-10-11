def make_readable(seconds):
    if seconds == 0:
        return "now"

    years, seconds = divmod(seconds, 31536000)
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    components = []

    if years > 0:
        components.append(f'{years} year{"s" if years > 1 else ""}')

    if days > 0:
        components.append(f'{days} day{"s" if days > 1 else ""}')

    if hours > 0:
        components.append(f'{hours} hour{"s" if hours > 1 else ""}')

    if minutes > 0:
        components.append(f'{minutes} minute{"s" if minutes > 1 else ""}')

    if seconds > 0:
        components.append(f'{seconds} second{"s" if seconds > 1 else ""}')

    if len(components) > 1:
        last_component = components.pop()
        return ", ".join(components) + f" and {last_component}"
    else:
        return components[0]
