def convert(num):
    mapping = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    return ' '.join(mapping[int(d)] for d in str(num))