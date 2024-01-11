from sqlalchemy import create_engine, orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime
import datetime
from sqlalchemy.orm import sessionmaker


# -------------------------sqlite3-------------------------
engine = create_engine('sqlite:///sqlalchemy_sqlite3.db?check_same_thread=False',
                       # echo=True
                       )


Base = orm.declarative_base()

Session = sessionmaker(bind=engine)

# 創建session對象
session = Session()


class UserHomeWork(Base):
    __tablename__ = 'user_homework'

    id = Column(Integer, primary_key=True)
    student_name = Column(String(64), nullable=False, index=True)
    age = Column(Integer, nullable=False)
    homework_account = Column(Integer, nullable=False)
    last_update_time = Column(DateTime(timezone='Asia/Chongqing'), default=datetime.datetime.now)

    def __repr__(self):
        return f"{self.__class__.__name__}(學員姓名: {self.student_name} | 學員年齡: {self.age} | " \
               f"作業數量: {self.homework_account} | 最後更新時間: {self.last_update_time})"


if __name__ == '__main__':
    # 創建資料庫
    Base.metadata.create_all(engine, checkfirst=True)

    #  第一次創建表的時候才插入如下數據
    homework_dict = [
        {'student_name': '張三', 'age': 37, 'homework_account': 1},
        {'student_name': '李四', 'age': 33, 'homework_account': 5},
        {'student_name': '王五', 'age': 32, 'homework_account': 10},
    ]

    # 添加數據
    for homework in homework_dict:
        homework_obj = UserHomeWork(**homework)
        session.add(homework_obj)

    # 提交
    session.commit()
