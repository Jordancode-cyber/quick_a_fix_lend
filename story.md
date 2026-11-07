HOSTEL ITEM BORROWING SYSTEM

## System overview and story ##

In a university hostel environment, students frequently need to borrow items from one another—ranging from academic resources like textbooks and scientific calculators to general items like phone chargers or sports equipment.

Our task resolves around creating an app using OOP pricinples and lessons learnt from previous class to come up with a system that helps students and different hostels to borrow differnt items from each other.

### Key Entities and Responsibilities
* **Hostel & Warden:** Handles student registration, room allocations, and resolves escalated disputes.
* **Students:** Act as lenders and borrowers, managing listings, requests, and returns.
* **Items & Categories:** Catalogs available items by type, description, and real-time availability status.
* **Agreement, Period & Conditions:** Establishes binding contractual terms, borrowing duration windows, and fine structures.
* **Issues:** Tracks broken rules, damaged items, or late returns requiring warden resolution.

The system operates seamlessly directly between students for standard transactions, reserving administrative intervention (**The Warden**) strictly for escalated disputes.


## System Workflow Scenarios
Our system workflow has two main aspects to the stoey combinding two different scenarios

### Scenario 1 -- Borrowing and return

[Warden Registers Students] ➔ [Alice Lists Item] ➔ [Bob Requests Item] ➔ [Agreement Created] ➔ [Bob Returns Item] ➔ [Alice Confirms Return]

**Registration & Setup**
* The **Warden** registers students (**Alice** and **Bob**) into the **Hostel** system and assigns them their respective room numbers.
* **Alice** creates a listing for a *"Calculator"* under the *"Academics"* **Item Category**, marking it available for borrowing.

**Item Request & Agreement Creation**
* **Bob** needs a calculator for an upcoming exam. He searches available items and requests Alice's calculator for a 3-day duration.
* The system generates an **Agreement** combining the start/end dates (**Period**) and agreed rules (**Conditions**, such as returning the item damage-free with a 1,000ugx per day late fee policy).
* Upon Alice's approval, the calculator's status changes from `Available` to `Borrowed`.

**Successful Return**
* Within the 3-day period, Bob returns the calculator to Alice in good condition.
* Alice inspects the item and confirms the return via the system.
* The **Agreement** status updates to `Completed`, and the calculator's status resets to `Available` for future requests.
* **Outcome:** The Warden is never involved, since the transaction completes smoothly with no issues.

### Scenario 2 -- Dispute that involves the warden

[Bob Overdue & Damaged Item] ➔ [Alice Logs Issue] ➔ [Escalated to Warden] ➔ [Warden Assesses Fine] ➔ [Issue Resolved]

**Item Borrowing**
* Bob borrows Alice's calculator under an active **Agreement** with specified return dates and late-fine conditions.

**Breach of Agreement**
* Bob fails to return the item on the expected return date. When he finally brings it back 4 days late, the screen is cracked.
* Alice declines to mark the transaction as completed due to the damage and delay.

**Escalation to Warden**
Alice logs an **Issue** through the system, attaching details of the cracked screen and the 4-day delay.* The **Agreement** status automatically shifts to `Disputed`, and the system routes the **Issue** to the Warden's administrative queue.

**Warden Resolution**
* The Warden reviews the dispute, referencing the initial **Conditions** attached and the borrowing **Period**.
* Using the daily fine rate defined in **Conditions**, the Warden calculates the overdue penalty and adds necessary repair costs for the cracked screen.
* The Warden executes `resolve_issue()`, logs the resolution details, levies the fine, and updates the **Issue** status to `Resolved by Warden`.