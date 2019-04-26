import sys
import os
import unittest

is_test = (len(sys.argv) == 2 and sys.argv[1] == '--test')
if len(sys.argv) != 5 and not is_test:
    print('usage: python task1.py [startedDir] [filesCount] [threshold] [endDir]')
    print()
    print('[startedDir] - started directory')
    print('[filesCount] - count of files')
    print('[threshold] - threshold size of file in byte')
    print('[endDir] - directory, where all files that don\'t pass threshold will be copied')
    print()
    print('To run tests: python task1.py --test')
    exit(1)


def handle(started_dir, files_count, threshold, end_dir):
    counter = 0
    for r, d, f in os.walk(started_dir):
        for file in f:
            fp = os.path.join(r, file)
            if os.path.getsize(fp) <= int(threshold) and counter < int(files_count):
                counter += 1
            else:
                os.rename(fp, os.path.join(end_dir, file))


if not is_test:
    handle(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])


class MyTest(unittest.TestCase):
    def test(self):
        startedDir = '/Users/admin/PycharmProjects/tasks/test'
        filesCount = 2
        threshold = 1
        endDir = '/Users/admin/PycharmProjects/tasks/testOutput'
        emptyFilesCount = 4
        fullFilesCount = 3

        print('Create ' + str(emptyFilesCount) + ' empty files and '
              + str(fullFilesCount) + ' files with text in directory: ' + startedDir)
        self.createFilesInDir(startedDir, emptyFilesCount, fullFilesCount)

        print('Run method')
        handle(startedDir, filesCount, threshold, endDir)

        try:
            print('Run tests')
            self.assertEqual(self.lenOfFilesInDir(startedDir), filesCount)
            self.assertEqual(self.lenOfFilesInDir(endDir), emptyFilesCount + fullFilesCount - filesCount)
            print('Tests run successfully')
        finally:
            print('Clean up')
            # self.removeAllFilesFromDirectory(startedDir)
            # self.removeAllFilesFromDirectory(endDir)

    @staticmethod
    def createFilesInDir(directory, empty_files, full_files):
        for i in range(0, empty_files):
            text_file = open(directory + "/someEmpty" + str(i) + ".txt", "w")
            text_file.write('')
            text_file.close()
        for i in range(0, full_files):
            text_file = open(directory + "/someFull" + str(i) + ".txt", "w")
            text_file.write('some text that has size more than 1 byte')
            text_file.close()

    @staticmethod
    def removeAllFilesFromDirectory(directory):
        for the_file in os.listdir(directory):
            file_path = os.path.join(directory, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(e)

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
