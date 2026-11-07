from datetime import datetime
from typing import List


class Issue:
    def __init__(self, issue_id, agreement, reporter_id, description):
        self.issue_id = issue_id
        self.agreement = agreement
        self.reporter_id = reporter_id
        self.description = description
        self.date_reported = datetime.now()
        self._is_resolved = False
        self.fine_amount = 0.0
        self.resolution_notes = ""

    @property
    def is_resolved(self):
        return self._is_resolved

    def resolve(self, fine_amount, notes):
        self.fine_amount = fine_amount
        self.resolution_notes = notes
        self._is_resolved = True
        self.agreement.set_status("Resolved by Warden")



# User Role Classes (Inheriting from User)
# Just to test only but thisis temporary and can be removed later
class Person:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
class Student(Person):
    

    def __init__(self, user_id, name, room_number, hostel_id):
        super().__init__(user_id, name)
        self.room_number = room_number
        self.hostel_id = hostel_id
        self.owned_items: List[Item] = []

    def add_owned_item(self, item):
        self.owned_items.append(item)

    def request_item(self, agreement_id, item, period, condition):
        if not item.is_available:
            print(f"[{self.name}] Error: Item '{item.title}' is currently unavailable.")
            return None

        item.set_availability(False)
        agreement = Agreement(agreement_id, item, item.owner_id, self.user_id, period, condition)
        print(f"[{self.name}] Successfully created borrowing request for '{item.title}'.")
        return agreement

    def report_issue(self, issue_id, agreement, description, warden):
        agreement.set_status("Disputed")
        issue = Issue(issue_id, agreement, self.user_id, description)
        print(f"[{self.name}] Issue reported for Agreement {agreement.agreement_id}: '{description}'")
        warden.receive_escalated_issue(issue)
        return issue

class Warden(Person):
    def __init__(self, warden_id, name, contact, hostel_id):
        super().__init__(warden_id, name, contact)
        self.hostel_id = hostel_id
        self.pending_issues: List[Issue] = []

    def assign_room(self, student, room_number):
        student.room_number = room_number
        print(f"[Warden {self.name}] Assigned Room {room_number} to Student {student.name}.")

    def receive_escalated_issue(self, issue):
        self.pending_issues.append(issue)
        print(f"[Warden {self.name}] Received Issue: [{issue.issue_id}] regarding Agreement {issue.agreement.agreement_id}.")

    def calculate_fine(self, issue, days_overdue):
        rate = issue.agreement.condition.damage_fine_per_day
        return days_overdue * rate

    def resolve_issue(self, issue, days_overdue, resolution_notes):
        fine = self.calculate_fine(issue, days_overdue)
        issue.resolve(fine, resolution_notes)
        if issue in self.pending_issues:
            self.pending_issues.remove(issue)
        print(f"[Warden {self.name}] Issue [{issue.issue_id}] resolved. Fine levied: ${fine:.2f}. Notes: {resolution_notes}")


class Hostel:
    def __init__(self, hostel_id, name, total_rooms):
        self.hostel_id = hostel_id
        self.name = name
        self.total_rooms = total_rooms
        self.students: List[Student] = []

    def add_student(self, student):
        self.students.append(student)
        print(f"[{self.name}] Registered student: {student.name}.")

    def remove_student(self, student_id):
        self.students = [s for s in self.students if s.user_id != student_id]
        print(f"[{self.name}] Removed student ID: {student_id}.")
if __name__ == "__main__":


class ItemCategory:
    def __init__(self, category_id, category_name, description):
        self.category_id = category_id
        self.category_name = category_name
        self.description = description

    def get_category_details(self):
        return f"Category: {self.category_name} ({self.description})"

class Item:
    def __init__(self, item_id, title, description, owner_id, category):
        self.item_id = item_id
        self.title = title
        self.description = description
        self.owner_id = owner_id
        self.category = category
        self._is_available = True

    def is_available(self):
        return self._is_available    

    def set_availability(self, status):
        self._is_available = status

    def get_item_details(self):
        status_str = "Available" if self.is_available else "borrowed"
        return f"Item[{self.item_id}]: {self.title} status: {status_str} owner: {self.owner_id}"        


##Demo

print("\n--CREATING ITEM CAREGORIES & LISTINGS --")
cat_academics = ItemCategory("CO1", "Academics","Textbooks and academic gear")
calculator =Item("I101","ScientificCalculator FX-PP1EX","Casio calculator",owner_id=alice.user_id,category=cat_academics)
alice.add_owned_item(calculator)

print(calculator.get_item_details())