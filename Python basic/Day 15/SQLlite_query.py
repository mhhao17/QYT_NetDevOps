from SQLlite_ORM import UserHomeWork, session
# 查詢
user_notify = """
請輸入查詢選項:
輸入 1: 查詢整個數據庫
輸入 2: 根據學員姓名查詢
輸入 3: 根據學員年齡查詢
輸入 4: 根據作業數量查詢
輸入 0: 退出
"""

while True:
    print(user_notify)
    user_input = input('請輸入查詢選項: ')
    if user_input == '0':
        break
    elif user_input == '1':
        homework = session.query(UserHomeWork).all()
        for homework in homework:
            output_format = f"學員姓名: {homework.student_name} | 學員年齡: {homework.age} | " \
                            f"作業數量: {homework.homework_account} | 最後更新時間: {homework.last_update_time}"
            print(output_format)
    elif user_input == '2':
        user_name = input('請輸入學員姓名: ')
        if not user_name:
            continue
        homework = session.query(UserHomeWork).filter_by(student_name=user_name).first()
        if not homework:
            print('學員信息未找到!')
        else:
            output_format = f"學員姓名: {homework.student_name} | 學員年齡: {homework.age} | " \
                            f"作業數量: {homework.homework_account} | 最後更新時間: {homework.last_update_time}"
            print(output_format)
    elif user_input == '3':
        user_age = input('搜索大於輸入年齡的學員,請輸入學員年齡: ')
        if not user_age:
            continue
        homework = session.query(UserHomeWork).filter(UserHomeWork.age > user_age).all()
        if not homework:
            print('學員信息未找到!')
        else:
            for homework in homework:
                output_format = f"學員姓名: {homework.student_name} | 學員年齡: {homework.age} | " \
                                f"作業數量: {homework.homework_account} | 最後更新時間: {homework.last_update_time}"
                print(output_format)
    elif user_input == '4':
        user_homework = input('搜索大於輸入作業數的學員,請輸入作業數量: ')
        if not user_homework:
            continue
        homework = session.query(UserHomeWork).filter(UserHomeWork.homework_account > user_homework).all()
        if not homework:
            print('學員信息未找到!')
        else:
            for homework in homework:
                output_format = f"學員姓名: {homework.student_name} | 學員年齡: {homework.age} | " \
                                f"作業數量: {homework.homework_account} | 最後更新時間: {homework.last_update_time}"
                print(output_format)
    else:
        print('輸入有誤,請重新輸入!')


