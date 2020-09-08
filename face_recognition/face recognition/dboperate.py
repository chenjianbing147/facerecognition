import numpy as np
import pymysql


class DBOperate:

    def __init__(self):
        # 数据库连接
        """
            host:数据库地址
            user：数据库用户名
            password：数据库密码
            database：数据库名称
            charset: 数据库编码
        """
        self.conn = pymysql.connect(host="localhost", user="root", password="binggege1997", database="facerecognition",
                                    charset="utf8mb4")

    def student_register(self, student_name, student_id, face_vector):
        cursor = self.conn.cursor()
        sql = "insert into students (name, studentID, facevector) values ('%s','%s','%s')" % (
            student_name, student_id, face_vector)
        cursor.execute(sql)
        self.conn.commit()
        cursor.close()

    def get_face_vector(self):
        cursor = self.conn.cursor()
        sql = "select name,studentID,facevector from students"
        cursor.execute(sql)
        result = cursor.fetchall()
        student_list = []
        vector_list = []
        cursor.close()
        for v in result:
            v = list(v)
            v[2] = np.array(eval(str(v[2])[2:-1]))
            student_list.append(v[0:2])
            vector_list.append(v[2])
        return student_list, vector_list

    def punch_in(self, t, student_id):
        cursor = self.conn.cursor()
        sql = "update students set last_punch_in='%s'where studentID='%s'" % (t, student_id)
        cursor.execute(sql)
        self.conn.commit()
        cursor.close()

