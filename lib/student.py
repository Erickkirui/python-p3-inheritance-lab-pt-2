import io
import sys


class Student:
    def hello(self):
        print("Hey there! I'm so excited to learn stuff.")

    def raise_hand(self):
        print("Pick me!")


class ChattyStudent(Student):
    def hello(self):
        super().hello()
        print("How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died...")

    def raise_hand(self):
        for _ in range(10):
            print("Pick me!")


class TestStudent:
    '''Class Student in student.py'''

    def test_says_hello(self):
        '''says a brief greeting.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        student = Student()
        student.hello()
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Hey there! I'm so excited to learn stuff.\n"

    def test_raises_hand(self):
        '''respectfully tries to get the teacher's attention.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        student = Student()
        student.raise_hand()
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Pick me!\n"


class TestChattyStudent:
    '''Class ChattyStudent in student.py'''

    def test_says_hello(self):
        '''says a brief greeting, then tries to spoil a TV show.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        chatty_student = ChattyStudent()
        chatty_student.hello()
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Hey there! I'm so excited to learn stuff.\nHow are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died...\n"

    def test_raises_hand(self):
        '''respectfully tries to get the teacher's attention ten times.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        chatty_student = ChattyStudent()
        chatty_student.raise_hand()
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Pick me!\n" * 10
