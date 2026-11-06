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
