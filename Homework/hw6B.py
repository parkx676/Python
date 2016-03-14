## Stacking Balls
## Juhwan Park (3917664)

def pyramid(h):
    if h < 0:
        return pyramid(-h)
    elif 0 <= h < 2:
        return h
    else:
        return (h * h) + pyramid(h - 1)
