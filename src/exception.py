import sys
from logger import logging
import logging


def fetch_error_msg(error_msg,msg_detail:sys):
    _,_,exc_tb = msg_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
    file_name,exc_tb.tb_lineno,str(error_msg))
    return error_message

class CustomException(Exception):
    def __init__(self,error_msg,msg_detail:sys):
        super().__init__(error_msg)
        self.error_msg = fetch_error_msg(error_msg,msg_detail)

    def __str__(self):
        logging.info(f"Exception {self.error_msg}")
        return self.error_msg
    

# if __name__=="__main__":
#     try:
#         a=5
#         c=a/0
#     except Exception as e:
#         raise CustomException(e,sys)