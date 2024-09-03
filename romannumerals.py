def romantoint(s:str) -> int:
    rtt = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D":500, "M": 1000}

    con = 0

    for i in range(len(s)):
        if i < len(s) - 1 and rtt[s[i]] < rtt[s[i + 1]]:
            con -= rtt[s[i]]
        else:
            con += rtt[s[i]]
    return con

print(romantoint("MCMXCIV"))