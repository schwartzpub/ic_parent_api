# Infinite Campus Parent API

This is an async wrapper for the [Infinite Campus API](https://canvas.instructure.com/doc/api/).  There are a few types of objects this will retrieve based on the assumption that you are a parent with students enrolled with Canvas.  

The types of objects that can be returned include:

- Students
- Courses
- Assignments
- Terms
- **Grades** - Posted and in-progress grades by term
- **Attendance** - Absences and tardies by term
- **Messages** - Inbox messages from teachers/school

This module is provided for use with the Home Assistant custom integration [Infinite Campus](https://github.com/schwartzpub/infinite_campus_hassio) however it could be useful as a standalone module for your own projects as well.

## Installing

To install the module use:

```shell
python3 -m pip install ic-parent-api
```

### Usage

At the login page inspect the page with developer tools and search for the hidden input with the name `appName`. Like in the image below.

![Screenshot 2022-09-16 171957](https://user-images.githubusercontent.com/13734613/190816004-a062b221-0653-4655-9b37-b67211350e6b.jpg)

Example usage to get students, printing first names:

```python
import asyncio
from ic_parent_api import InfiniteCampus

base_url = "https://school.infinitecampus.com"
username = "myusername"
password = "myp4ssw0rd!"
district = "schooldistrict" #known as appName to infinitecampus

async def get_students():
    client = InfiniteCampus(f"{base_url}",f"{username}",f"{password}",f"{district}")
    return await client.students()

students = asyncio.run(get_students())

for student in students:
    print(student.firstname)
```

### Getting Grades

```python
async def get_grades():
    client = InfiniteCampus(f"{base_url}",f"{username}",f"{password}",f"{district}")
    students = await client.students()

    for student in students:
        grades = await client.grades(student.personid)
        for grade in grades:
            for term in grade.terms:
                print(f"\n{term.termname}:")
                for course in term.courses:
                    print(f"  {course.coursename}: {course.grade}")

asyncio.run(get_grades())
```

### Getting Attendance

```python
async def get_attendance():
    client = InfiniteCampus(f"{base_url}",f"{username}",f"{password}",f"{district}")
    students = await client.students()

    for student in students:
        for enrollment in student.enrollments:
            attendance = await client.attendance(enrollment.enrollmentid, student.personid)
            for term in attendance.terms:
                print(f"{term.termname}: {term.totalabsent} absences, {term.totaltardy} tardies")

asyncio.run(get_attendance())
```

### Getting Inbox Messages

```python
async def get_messages():
    client = InfiniteCampus(f"{base_url}",f"{username}",f"{password}",f"{district}")
    messages = await client.messages()

    for msg in messages[:10]:  # First 10 messages
        print(f"{msg.date}: {msg.subject}")
        print(f"  Student: {msg.studentname}")
        print(f"  Course: {msg.coursename}")

        # Get full message content
        detail = await client.message_detail(msg)
        if detail.body_text:
            print(f"  Content: {detail.body_text[:200]}...")

asyncio.run(get_messages())
```
