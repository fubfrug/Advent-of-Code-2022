from itertools import groupby

print("Answer 1: {}\nAnswer 2: {}".format(*list(map(lambda initial_list: [initial_list[0], sum(initial_list[:3])], [sorted([sum(int(calorie) for calorie in list(elf)) for match, elf in groupby([line.strip() for line in open("input.txt").readlines()], lambda seperator: seperator.strip() == "") if not match], reverse=True)]))[0]))
