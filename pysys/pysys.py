import platform


# ========================================
# [] File Name : pysys.py
#
# [] Creation Date : March 2018
#
# [] Created By : Ali Gholami (aligholami7596@gmail.com)
# ========================================
'''
    Python library to extract information from the system.
'''
import platform

class Pysys:

    def os_name(self):
        return platform.system()
    
    def processor_family(self):
        return platform.processor()
    
    def arc(self):
        return platform.machine()

    def full_name(self):
        return platform.uname()
