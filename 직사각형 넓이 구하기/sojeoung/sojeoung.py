# 직사각형 넓이 구하기

def solution(dots):
    x = [dot[0] for dot in dots]
    y = [dot[1] for dot in dots]

    return (max(x)-min(x))*(max(y)-min(y))

dots = [[-1, -1], [1, 1], [1, -1], [-1, 1]]
print(solution(dots))