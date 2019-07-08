def bouncingBall(h, bounce, window):
    count = 0
    if h>0 and bounce > 0 and bounce < 1:
        while window < h:
            h = h * bounce
            count += 1
            if h > window:
                count += 1
    if count >= 2:
        return count
    else:
        return -1