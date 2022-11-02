from __future__ import annotations
from datetime import datetime

from typing import List, Any, TYPE_CHECKING
if TYPE_CHECKING:
    from student import Student


class Course:
    """
            A class used to represent a Course of a student

            ...

            Attributes
            ----------
            title : str
                show full name of student
            start_date : datetime
                the address of student
            end_date : datetime
                the phone number of student
            description : str
                email of student
            lectures: list[str]
                the id of student
            assignments: list[str]
                 average mark of students during course
            limit: int
                return all list of students on course
            """

    def __init__(self, title: str, start_date: int, end_date: int, description: str,
                 lectures: list[str], limit: int):
        self.title = title
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.lectures = lectures
        self.assignments = []
        self.limit = limit
        self.students = []

    def add_student(self, student: Student) -> None:
        """Add student on a course

                Args:
                    student(Student): select a student for a course

                Returns:
                    Nothing
                """

        try:
            student.enroll(course=self)
        except ValueError:
            print(f"Student {student.full_name} already enrolled")
            course_progress = CourseProgress(title=self.title)
            student.course_progress.append(course_progress)
            self.students.append(student)

    def remove_student(self, student: Student) -> None:

        """Remove student from a course

                Args:
                    student: (Student): date due to which we want to take marks.

                Returns:
                    Dictionary "marks" with structure: "task": "mark.
        """

        for i, st in enumerate(self.students):
            if student.id == st.id:
                self.students.pop(i)
                student.unenroll(self)
                break


class CourseProgress:
    """
                A class used to represent a CourseProgress of a student

                ...

                Attributes
                ----------
                received_marks : dict
                    marks the student get during the course
                visited_lectures : int
                    lectures that the student attended
                completed_assignments : dict
                    the phone number of student
                notes : dict[str]

                """

    def __init__(self, title: str, completed_assignments: dict):
        self.title = title
        self.received_marks = {"marks": 1}
        self.visited_lectures = 0
        self.completed_assignments = completed_assignments
        self.notes = {}

    def get_progress_to_date(self, date: datetime) -> list:

        """

        """

        grades = []
        for task_date, task in self.completed_assignments.items():
            if task_date < date:
                grades.append(task["mark"])
        return grades

    @staticmethod
    def get_final_mark(self) -> float:

        """Return student a final mark

                Args:
                    student(Student): take a student to grade

                Returns:
                    Float average mark
                """
        values = self.received_marks.values()
        amount_of_marks = self.received_marks
        return sum(values) / len(amount_of_marks)

    def fill_notes(self, note: str) -> None:
        """Fill the notes

                Args:
                    note(str): take a note

                Returns:
                    Nothing
        """
        self.notes[datetime.now()] = note

    def remove_note(self, note: datetime) -> None:
        """Fill the notes

                        Args:
                            note(str): take a note

                        Returns:
                            Nothing
                """
        self.notes[datetime.now()] = note

