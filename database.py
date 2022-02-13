import sqlite3

def create_db():
    with sqlite3.connect("block.db") as con:
        sql_cmd = """
            create table block(
                id integer PRIMARY KEY AUTOINCREMENT,
                team1 text,
                team2 text,
                score text,
                timestamp text,
                hash text
            )
        """
        con.execute(sql_cmd)
def insert_db(params):
    with sqlite3.connect("block.db") as con:
        sql_cmd = """
            insert into block(team1, team2, score, timestamp, hash) values(?, ?, ?, ?, ?);
        """
        con.execute(sql_cmd, params)

def select_db():
    with sqlite3.connect("block.db") as con:
        sql_cmd = """
           select team1, team2, score, timestamp,hash from block
        """
    return con.execute(sql_cmd)


def selecthash_db(params):
    with sqlite3.connect("block.db") as con:
        sql_cmd = """
           select
           hash from block
           where id = ?
        """
    return con.execute(sql_cmd ,[params])
    
def update_db(params):
    with sqlite3.connect("block.db") as con:
        sql_cmd = """
           update block 
            set hash = ?
           where  id = ? 
        """
        con.execute(sql_cmd, params)
        
if __name__ == '__main__':
    create_db()

    
    
