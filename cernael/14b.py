def solve(lines):
    rock, sand = set(), 0
    bottom = 0
    for l in lines:
        l = l.split(' -> ')
        for i in range(1, len(l)):
            (sx, sy), (ex, ey) = l[i-1].split(','), l[i].split(',')
            xs, ys = sorted([int(sx), int(ex)]), sorted([int(sy), int(ey)])
            [rock.add((x,y)) for x in range(xs[0], xs[1]+1) for y in range(ys[0], ys[1]+1)]
            bottom = max(bottom, int(sy), int(ey))
    [rock.add((x,bottom+2)) for x in range(500-bottom-10, 500+bottom+10)]
    #return bottom
    while True:
        x, y = 500, 0
        while True:
            if (x, y+1) not in (rock):
                y += 1
            elif (x-1, y+1) not in (rock):
                y += 1
                x -=1
            elif (x+1, y+1) not in (rock):
                y += 1
                x +=1
            else:
                rock.add((x,y))
                sand += 1
                if (x,y) == (500,0):
                    return sand
                break


if __name__ == '__main__':
    lines = []
    with open('14.txt') as f:
        for line in f.readlines():
            line = line.strip()
            lines.append(line)
    print(solve(lines))
