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
