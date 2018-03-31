# ========================================
# [] File Name : processor.py
#
# [] Creation Date : March 2018
#
# [] Created By : Ali Gholami (aligholami7596@gmail.com)
# ========================================
"""
    Advanced System Information Toolbox Python Library.
"""
import platform
import psutil

class Processor:

    def __init__(self):
        pass

    @staticmethod
    def get_name(self):
        """
        :return: Processor's name
        """
        return platform.processor()

    @staticmethod
    def get_code_name(self):
        """
        :return: Processor's code name
        """
        return platform.processor()

    @staticmethod
    def get_num_cores(self):
        """
        :return: Number of processor cores
        """
        return psutil.cpu_count()

    @staticmethod
    def get_freq(self):
        """
        :return: The cpu frequency.
        """
        return psutil.cpu_freq()


