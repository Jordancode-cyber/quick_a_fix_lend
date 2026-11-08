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
print("\n-- 2.CREATING ITEM CAREGORIES & LISTINGS --")
cat_academics = ItemCategory("CO1", "Academics","Textbooks and academic gear")
calculator =Item("I101","ScientificCalculator FX-PP1EX","Casio calculator",owner_id=alice.user_id,category=cat_academics)
alice.add_owned_item(calculator)

print(calculator.get_item_details())

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

class Period:
    def __Init__(self, period_id, start_time, end_time):
        self.period_id = period_id
        self.start_time = start_time
        self.end_time = end_time
        self.expected_return_time = end_time

    def calculate_duration_in_hours(self):
        return max((self.end_time - self.start_time).days, 1)

    def extend_period(self, additional_hours):
        self.end_time += timedelta(hours=additional_hours)
        self.expected_return_time = self.end_time
        return self.end_time

class Conditions:
    def __init__(self, condition_id, initial status, return_terms, damage_fine_per_hour):
        self.condition_id = condition_id
        self.initial_status = initial_status
        self.return_terms = return_terms
        self.damage_fine_per_hour = damage_fine_per_hour

    def get_terms(self):
        return f"Condition: {self.initial_status} | Terms: {self.return_terms} | Late Fine/Hour: ${self.damage_fine_per_hour:.2f}"

class Agreement:
    def __init__(self, agreement_id, item, lender_id, borrower_id, period, condition):
        self.agreement_id = agreement_id
        self.item = item
        self.lender_id = lender_id
        self.borrower_id = borrower_id
        self.period = period
        self.condition = condition
        self._status = "Active"  # Statuses: Active, Completed, Overdue, Disputed

    @property
    def status(self):
        return self._status

    def set_status(self, new_status):
        self._status = new_status

    def confirm_return(self):
        self._status = "Completed"
        self.item.set_availability(True)

    def is_overdue(self, current_time):
        if current_time > self.period.expected_return_time and self._status == "Active":
            self._status = "Overdue"
            return True
        return self._status == "Overdue"


    print("\n--- 3. Borrowing Process ---")
    now = datetime.now()
    period = Period(period_id=1, start_time=now, end_time=now + timedelta(days=7))
    condition = Conditions("CONDO1", "Good Condition", "Return without scratches", damage_fine_per_hour=2.50)       
