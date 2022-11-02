from __future__ import annotations

from typing import List, Any, TYPE_CHECKING
if TYPE_CHECKING:
    from course import Course


class Student:
    """
        A class used to represent a Student

        ...

        Attributes
        ----------
        full_name : str
            show full name of student
        address : str
            the address of student
        phone_number : str
            the phone number of student
        email : str
            email of student
        id: int
            the id of student
        average_mark: float
             average mark of students during course
        """

    def __init__(self, full_name: str, address: str, phone_number: str, email: str, student_id: int):
        self.full_name = full_name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.id = student_id
        self.average_mark = 0
        self.course_progress = []
        self.courses = []

    @staticmethod
    def taken_course(self) -> list:

        """Take the student on a course

        Args:
            No arguments

        Returns:
                List of course
        """

        return self.courses

    def enroll(self, course: Course) -> None:

        """Enroll student course

        Args:
            course: (Course): the course we want to enroll student

        Returns:
             Nothing
        """

        if course not in self.courses:
            self.courses.append(course)
            print(f"{self.id} has enrolled to {course.title}")
        else:
            raise ValueError("Course has already added")

    def unenroll(self, course: Course) -> None:

        """Unenroll student

        Args:
            course: (Course): the course we want to unenroll the student

        Returns:
            Nothing
        """

        for i, c in enumerate(self.courses):
            if course.title == c.title:
                self.courses.pop(i)
                break


class Professor:
    """
            A class used to represent a Professor

            ...

            Attributes
            ----------
            name : str
                show  name of professor
            address : str
                the address of professor
            phone_number : str
                the phone number of professor
            email : str
                email of professor
           salary: float
               salary of professor
            """

    def __init__(self, name: str, address: str, phone_number: int, email: str, salary: float):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.salary = salary

    @staticmethod
    def check_assignment(assignment: dict) -> None:

        """Check assignment of student

            Args:
                assignment:dict : the assignment we must check

            Returns:
                    Nothing
                """

        if assignment.get("is done"):
            assignment["mark"] = 5
