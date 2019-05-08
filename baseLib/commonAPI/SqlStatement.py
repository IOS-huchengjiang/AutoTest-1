# -*- coding:utf-8 -*-
#autor :huchengjiang

def transfer_requestSql(request_id):
    transfer_requestSql = 'select status,request_type from merchant_transfer_request where request_id = \'%s\' order by id desc' %request_id
    return transfer_requestSql
def account_bal_frz_recordSql():
    account_bal_frz_recordSql = 'select status,sum from account_bal_frz_record where account_id=\'220000000000000893\' order by row_create_time desc'
    return account_bal_frz_recordSql

def account_balance_change_historySql():
    account_balance_change_historySql = 'select op_type,fund from ACCOUNT_BALANCE_CHANGE_HISTORY where account_id=\'220000000000000893\' order by id desc'
    return account_balance_change_historySql

def trade_recordSql(request_id):
    trade_recordSql = 'select status,id from trade_record where order_id = \'%s\' order by id desc' %request_id
    return trade_recordSql

def actual_separate_account_recordSql(trade_id):
    actual_separate_account_recordSql = 'select trade_id from actual_separate_account_record where trade_id = \'%s\' order by id desc' %trade_id
    return actual_separate_account_recordSql