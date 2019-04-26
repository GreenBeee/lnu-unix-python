import shutil
import sys
import os
import unittest

is_test = (len(sys.argv) == 2 and sys.argv[1] == '--test')
if len(sys.argv) != 2 and not is_test:
    print('usage: python task2.py [startedDir]')
    print()
    print('[startedDir] - started directory')
    print()
    print('To run tests: python task1.py --test')
    exit(1)


def handle(started_dir):
    maxNumber = 0
    maxName = started_dir
    for r, d, f in os.walk(started_dir):
        for dir in d:
            directoryCount = countAllDirectoriesinDirectory(os.path.join(r, dir))
            if maxNumber < directoryCount:
                maxNumber = directoryCount
                maxName = os.path.join(r, dir)

    print('Directory with most subdirectories (' + str(maxNumber) + ') is ' + maxName)
    return {maxName, maxNumber}


def countAllDirectoriesinDirectory(directory):
    counter = 0
    for the_file in os.listdir(directory):
        file_path = os.path.join(directory, the_file)
        if os.path.isdir(file_path):
            counter += 1
    return counter


if not is_test:
    handle(sys.argv[1])


class MyTest(unittest.TestCase):
    def test(self):
        startedDir = '/Users/admin/PycharmProjects/tasks/testSecondTaskForTest'
        os.mkdir(startedDir)

        print('Create different subdirectories in directory: ' + startedDir)
        maxNameExpected, maxNumberExpected = self.createFilesInDir(startedDir)

        print('Run method')
        maxName, maxNumber = handle(startedDir)

        try:
            print('Run tests')
            self.assertEqual(maxNameExpected, maxName)
            self.assertEqual(maxNumberExpected, maxNumber)
            print('Tests run successfully')
        finally:
            print('Clean up')
            self.removeAllFilesFromDirectory(startedDir)

    @staticmethod
    def createFilesInDir(directory):
        sub_1 = directory + '/sub1'
        sub_2 = directory + '/sub2'
        sub_3 = directory + '/sub3'
        sub_4 = sub_1 + '/sub4'
        sub_5 = sub_1 + '/sub5'
        sub_6 = sub_2 + '/sub6'
        sub_7 = sub_3 + '/sub7'
        sub_8 = sub_3 + '/sub8'
        sub_9 = sub_3 + '/sub9'
        sub_10 = sub_3 + '/sub10'
        sub_11 = sub_4 + '/sub11'
        sub_12 = sub_4 + '/sub12'

        os.mkdir(sub_1)
        os.mkdir(sub_2)
        os.mkdir(sub_3)
        os.mkdir(sub_4)
        os.mkdir(sub_5)
        os.mkdir(sub_6)
        os.mkdir(sub_7)
        os.mkdir(sub_8)
        os.mkdir(sub_9)
        os.mkdir(sub_10)
        os.mkdir(sub_11)
        os.mkdir(sub_12)
        return {sub_3, 4}

    @staticmethod
    def removeAllFilesFromDirectory(directory):
        shutil.rmtree(directory)

    @staticmethod
    def lenOfFilesInDir(directory):
        counter = 0
        for r, d, f in os.walk(directory):
            for file in f:
                counter += 1
        return counter


if is_test:
    mytest = MyTest()
    mytest.test()
