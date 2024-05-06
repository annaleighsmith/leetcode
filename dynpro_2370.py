
def solve(s, k):
    ideal_lengths = [0]*123 # 123 is max ascii value of a lowercase letter
    max_length = 0
    for char in s:
        ascii_value = ord(char) # ord() returns the ascii value of a character
        print(f"char, val: {char}, {ascii_value}")
        slice_start = ascii_value - k # k is max allowabled difference
        slice_end = ascii_value + k + 1 # +1 bc slciing is exclusive
        print(f"{slice_start} : {slice_end}")
        print(ideal_lengths[slice_start : slice_end])
        ideal_lengths[ascii_value] = 1 + max(ideal_lengths[slice_start : slice_end])
        max_length = max(max_length, ideal_lengths[ascii_value])
    return max_length

s = "acfgbd"
k = 2

print(s)
print(k)

solve(s, k)
    # opts = output + get_all_substrings(input_string[1:])
    #     opts = list(dict.fromkeys(opts))
    #     res_all = []
    #     for i, o in enumerate(opts):
    #         combos = list(zip(o, o[1:]))
    #         c1_val = char_position(combos[0])
    #         c2_val = char_position(combos[1])
    #         if c1_value >= c2_value:
    #             res = c1_value - c2_value
    #         else:
    #             res = c2_value - c1_value 
    #         res_all.append(res)
    #     
    #     list(zip(opts,res_all))
