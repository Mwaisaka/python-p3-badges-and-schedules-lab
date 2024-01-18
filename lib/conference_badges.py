def badge_maker(name):
    badge=f"Hello, my name is {name}."
    return badge

def batch_badge_creator(names):
    badges=[badge_maker(name) for name in names]
    return badges

def assign_rooms(names):
    assign_rooms=[f"Hello, {name}! You'll be assigned to room {x}!" for x, name in enumerate(names,start=1)]
    return assign_rooms 

def printer(names):
    badges=batch_badge_creator(names)
    rooms=assign_rooms(names)
    for badge in badges:
        print(badge)
    for room in rooms:
        print(room)
