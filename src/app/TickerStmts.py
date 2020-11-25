def insert_ticker_data_stmt(): 
    sql = "INSERT INTO `macro_ops`.`ticker_data` (`rank`,`close`,`dollar_change`,`percent_change`,`volume`,`tsi`,`ticker_id` , `created_date`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"
    return sql


def insert_ticker_stmt(): 
    sql = "INSERT INTO `macro_ops`.`ticker`(`ticker`,`created_date`) VALUES (%s,%s);"
    return sql


def insert_log_stmt():
    sql = "INSERT INTO `macro_ops`.`insert_log` (`created_date`,`created_time`) VALUES (%s,%s);"
    return sql


def dupe_check_stmt():
    sql = "SELECT created_date FROM insert_log WHERE created_date = %s;"
    return sql


def get_ticker_data_stmt():
    sql = "SELECT id FROM ticker WHERE ticker = %s;"
    return sql
