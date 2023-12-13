# Infinite Campus Parent API

This is an async wrapper for the [Infinite Campus API](https://canvas.instructure.com/doc/api/).  There are a few types of objects this will retrieve based on the assumption that you are a parent with students enrolled with Canvas.  

The types of objects that can be returned include:

- Students
- Courses
- Assignments
- Terms

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
