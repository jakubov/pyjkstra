from unittest import TestCase
from commands import getstatusoutput as run


class Pep8TestCase(TestCase):

    def test_pep8(self):
        process = run('pep8 --ignore=E128,E501,E125 --exclude=*.pyc  *')
        if process[0] != 0:
            print process[1]
            raise Exception('PEP8 failed')
