def generate_hashtag(s):
    if s == "" or len(s) > 140: return False
    else:
        s = s.title()
        s = s.replace(" ", "")
        return "#"+s