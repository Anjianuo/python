def get_path(t):
    if t < 135 and t > 0:
        x = t
        y = 108
        return [x, y]
    elif t < 363:
        x = 137
        y = t - 137 + 108
        return [x, y]
    elif t < 430:
        x = 70 + 430 - t
        y = 334
        return [x, y]
    elif t < 563:
        x = 70
        y = t - 430 + 334
        return [x, y]
    elif t < 815:
        x = t - 563 + 70
        y = 467
        return [x, y]
    elif t < 1174:
        x = 322
        y = -(t - 815) + 467
        return [x, y]
    elif t < 1705:
        x = t - 1174 + 322
        y = 108
        return [x, y]
    elif t < 1997:
        x = 853
        y = t - 1705 + 108
        return [x, y]
    elif t < 2149:
        x = -(t - 1997) + 853
        y = 400
        return [x, y]
    elif t < 2286:
        x = 701
        y = -(t - 2149) + 400
        return [x, y]
    elif t < 2434:
        x = -(t - 2286) + 701
        y = 263
        return [x, y]
    elif t < 2755:
        x = 553
        y = t - 2434 + 263
        return [x, y]
    else:
        return [-200, -200]  # 意思是不在路径上