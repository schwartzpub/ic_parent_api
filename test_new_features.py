#!/usr/bin/env python3
"""
Test script for new grades, attendance, and messages features.
Uses credentials from ../kids/.env
"""

import asyncio
import sys
import os

# Add src to path so we can import the local modified library
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from dotenv import load_dotenv
from ic_parent_api import InfiniteCampus

# Load credentials from kids folder
load_dotenv('/Users/nateober/kids/.env')


async def test_all_features():
    """Test all new features."""
    client = InfiniteCampus(
        os.getenv("IC_BASE_URL"),
        os.getenv("IC_USERNAME"),
        os.getenv("IC_PASSWORD"),
        os.getenv("IC_DISTRICT")
    )

    print("=" * 60)
    print("Testing ic_parent_api new features")
    print("=" * 60)

    # Test 1: Get students (existing feature)
    print("\n[TEST 1] Getting students...")
    try:
        students = await client.students()
        print(f"  ✓ Found {len(students)} students")
        for s in students:
            print(f"    - {s.firstname} {s.lastname} (ID: {s.personid})")
    except Exception as e:
        print(f"  ✗ Failed: {e}")
        return

    # Test 2: Get grades (new feature)
    print("\n[TEST 2] Getting grades...")
    try:
        for student in students:
            print(f"\n  {student.firstname} {student.lastname}:")
            grades = await client.grades(student.personid)
            if grades:
                for grade in grades:
                    for term in grade.terms:
                        print(f"    {term.termname}:")
                        for course in term.courses[:3]:  # First 3 courses
                            print(f"      {course.coursename}: {course.grade or '--'}")
                        if len(term.courses) > 3:
                            print(f"      ... and {len(term.courses) - 3} more courses")
            else:
                print("    No grades found")
        print("  ✓ Grades test passed")
    except Exception as e:
        print(f"  ✗ Failed: {e}")
        import traceback
        traceback.print_exc()

    # Test 3: Get attendance (new feature)
    print("\n[TEST 3] Getting attendance...")
    try:
        for student in students:
            print(f"\n  {student.firstname} {student.lastname}:")
            for enrollment in student.enrollments:
                attendance = await client.attendance(enrollment.enrollmentid, student.personid)
                for term in attendance.terms:
                    print(f"    {term.termname}: {term.totalabsent} absences, {term.totaltardy} tardies")
        print("  ✓ Attendance test passed")
    except Exception as e:
        print(f"  ✗ Failed: {e}")
        import traceback
        traceback.print_exc()

    # Test 4: Get messages (new feature)
    print("\n[TEST 4] Getting inbox messages...")
    try:
        messages = await client.messages()
        print(f"  Found {len(messages)} messages")
        for msg in messages[:5]:  # First 5 messages
            print(f"\n    {msg.date}: {msg.subject}")
            print(f"      Student: {msg.studentname}")
            if msg.coursename:
                print(f"      Course: {msg.coursename}")
        print("  ✓ Messages test passed")
    except Exception as e:
        print(f"  ✗ Failed: {e}")
        import traceback
        traceback.print_exc()

    # Test 5: Get message detail (new feature)
    print("\n[TEST 5] Getting message detail...")
    try:
        if messages:
            msg = messages[0]
            detail = await client.message_detail(msg)
            if detail.body_text:
                preview = detail.body_text[:200] + "..." if len(detail.body_text) > 200 else detail.body_text
                print(f"  Subject: {detail.subject}")
                print(f"  Content preview: {preview}")
            print("  ✓ Message detail test passed")
        else:
            print("  ⚠ No messages to test detail")
    except Exception as e:
        print(f"  ✗ Failed: {e}")
        import traceback
        traceback.print_exc()

    print("\n" + "=" * 60)
    print("All tests completed!")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(test_all_features())
