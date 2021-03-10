"""
Writing tests for context manager

Take your implementation of the context manager class from Task 1 and write tests for it. Try to cover as many use
cases as you can, positive ones when a file exists and everything works as designed. And also, write tests when your
class raises errors or you have errors in the runtime context suite.
"""
import tempfile
import unittest

from lesson_19.task_1_2.task_1_file import File


class TestFile(unittest.TestCase):
    def setUp(self) -> None:
        self.readfile = tempfile.NamedTemporaryFile()
        self.text = 'This is test file'
        self.write_mode = 'w'
        self.writefile = tempfile.NamedTemporaryFile()
        self.read_mode = 'r'
        self.false_mode = 'l'
        self.__allowed_modes = ('r', 'r+', 'rb', 'w', 'w+', 'wb', 'wb+', 'a', 'a+', 'ab', 'ab+')
        File.counter = 0

    def test_right_mode(self):
        new_file = File(self.writefile.name, self.write_mode)
        new_file.mode = self.write_mode if self.write_mode in self.__allowed_modes else 'r'
        self.assertEqual(new_file.mode, self.write_mode)

    def test_false_mode(self):
        new_file = File(self.writefile.name, self.write_mode)
        new_file.mode = self.false_mode if self.false_mode in self.__allowed_modes else 'r'
        self.assertEqual(new_file.mode, 'r', 'Wrong mode assigned')
        self.assertNotEqual(self.false_mode, new_file.mode, 'Falsy mode should not equal mode.')

    def test_read_file(self):
        with File(self.readfile.name, self.write_mode) as new_file:
            new_file.write(self.text)

        with File(self.readfile.name, self.read_mode) as new_file:
            read_file = new_file.read()
        self.assertIn(self.text, read_file)

    def test_write_to_file(self):
        with File(self.writefile.name, self.write_mode) as file:
            file.truncate()
            file.write(self.text)

        with File(self.writefile.name, self.read_mode) as file:
            read_file = file.read()
        self.assertEqual(self.text, read_file, 'text is not in file')

    def test_closed_file(self):
        with File(self.readfile.name, self.read_mode) as file:
            self.assertFalse(file.closed, 'file is open')
        self.assertTrue(file.closed, 'file is not closed')

    def test_counter(self):
        with File(self.writefile.name, self.write_mode) as new_file:
            self.assertEqual(File.counter, 1, 'only one created instance')

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
