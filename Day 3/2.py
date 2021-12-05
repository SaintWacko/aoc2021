def main():
    with open('input', 'r') as file:
        lines = file.read().splitlines()
        oxy = lines[:]
        co = lines[:]
        for idx in range(len(lines[0])):
            mcv = '1' if [x[idx] for x in oxy].count('1') >= len(oxy) / 2 else '0'
            oxy = [o for o in oxy if o[idx] == mcv]
            if len(oxy) == 1:
                oxy = oxy[0]
                break
        print(oxy)
        for idx in range(len(lines[0])):
            lcv = '0' if [x[idx] for x in co].count('0') <= len(co) / 2 else '1'
            co = [o for o in co if o[idx] == lcv]
            if len(co) == 1:
                co = co[0]
                break
        print(co)
        return int(oxy, 2) * int(co, 2)


if __name__ == "__main__":
    print(main())
