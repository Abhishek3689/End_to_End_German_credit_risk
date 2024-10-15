import os
import sys


def get_error_message(message,error_inf:sys):
    _,_,tb=error_inf.exc_info()
    filename=tb.tb_frame.f_code.co_filename
    line_no=tb.tb_lineno
    return f"Excetion is found in script [{filename}] at linenumber [{line_no}] with message [{message}]"

class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message=get_error_message(message=error_message,error_inf=error_details)

    def __str__(self):
        return self.error_message
    