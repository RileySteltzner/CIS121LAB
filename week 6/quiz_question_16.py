def like_dislike(events):
    state = 'Nothing'
    for action in events:
        if action == state:
            state = "Nothing"
        else:
            state = action
    return state
print(like_dislike(['Dislike', 'Like', 'Dislike']))