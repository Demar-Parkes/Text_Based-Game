def bag(items):
    backpack = [x for x in items.split(',')]
    if len(backpack) > 5:
        return 'Maximum should be 5'
    elif len(backpack) < 5:
        return 'Enter 5 items'
    else:
        return sorted(backpack)

_bag = input('Enter items seperate by commas: ')

print(bag(_bag))