file = open("source.txt", "r")
lines = file.readlines()
file.close()
count = 0
# part 1
# for line in lines:
#     nums = []
#     for char in line:
#         if char.isdigit():
#             nums.append(char)
#         # count += nums[0]
#     if len(nums) == 1:
#         nums.append(nums[0])
#     if len(nums) > 1:
#         nums = [nums[0], nums[-1]]
#     count += int("".join(nums))
# print(count)

# part 2
count = 0
mappings = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
i = 0
for line in lines:
    print("****")
    print(line)
    nums = []
    i = 0
    while i < len(line):
        if line[i].isdigit():
            nums.append(line[i])
            i += 1

        else:
            for number, digit in mappings.items():
                if line[i : i + len(number)] == number:
                    nums.append(str(digit))
                    i += len(number)
                    break
            else:
                i += 1
    # print(nums)
    if len(nums) == 1:
        nums.append(nums[0])
    else:
        nums = [nums[0], nums[-1]]
    print(int("".join(nums)))
    count += int("".join(nums))
print(count)
# 55648 is too low?
