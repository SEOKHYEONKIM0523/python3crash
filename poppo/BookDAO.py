import poppo.dbinfo2 as dbinfo

insertsql = (' insert into book (bkname, author, publisher, pubdate, retail, price, pctoff, mileage)'
             ' values (%s,%s,%s,%s,%s,%s,%s,%s) ')
selectsql = 'select bkno, bkname, author, publisher, price from book'
selectonesql = 'select * from book where bkno =1'
updatesql = (' update book set bkname = %s, author = %s, publisher = %s,'
             'pubdate = %s, retail = %s, pctoff = %s where bkno = %s ')


class BookDAO:
    @staticmethod
    def insert_book(bk):
        """
        입력받은 도서데이터를 book테이블에 저장
        :param bk: 도서데이터
        :return: 저장된 데이터 건수
        """
        cursor, conn = dbinfo.openConn()
        params = [bk.bkname, bk.author, bk.publisher, bk.pubdate, int(bk.retail), int(bk.price), int(bk.pctoff), int(bk.mileage)]
        cursor.execute(insertsql,params)
        conn.commit()

        rowcnt = cursor.rowcount

        dbinfo.closeConn(cursor,conn)
        return rowcnt

    @staticmethod
    def select_book():
        cursor, conn = dbinfo.openConn()

        cursor.execute(selectsql)
        rows = cursor.fetchall()

        dbinfo.closeConn(cursor,conn)

        return rows
    @staticmethod
    def selectone_book():
        pass


    @staticmethod
    def update_book():
        pass


    @staticmethod
    def delete_book():
        pass