# 로그인 성공

id_pw = ["programmer01", "15789"]
db = [["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]

def solution(id_pw, db):
    id = [mini_db[0] for mini_db in db]
    if id_pw[0] in id:
        i = id.index(id_pw[0])
        pw = db[i][1]
        if id_pw[1] == pw:
            result = 'login'
        else:
            result = 'wrong pw'
    else:
        result = 'fail'
    return result

print(solution(id_pw,db))