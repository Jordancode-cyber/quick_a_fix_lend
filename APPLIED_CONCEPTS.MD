The following are some of the OOP concepts we were able to apply while doing the assigned project.

1. Encapsulation
### **Application in Design**
* **Attribute Visibility:** Class attributes such as `_is_available` in `Item`, `_status` in `Agreement`, and `_is_resolved` in `Issue` are marked as private/protected.
* **Controlled Access:** External code cannot directly alter internal states. For example, `Item` availability can only be toggled through dedicated methods like `set_availability()`, and `Agreement` status is updated through formal workflows such as `confirm_return()`.

2. Abstraction
### **Application in Design**
* **Interactions:** The `Student` class interacts with `Agreement` and `Issue` objects without needing to understand how fine calculations or date durations are executed internally.
* Date arithmetic and duration logic are encapsulated inside `Period.calculate_duration_in_days()`, hiding raw date calculations from the primary borrowing workflow.

3. Inheritance
### **Application in Design**
* **Shared Classes:** Both `Student` and `Warden` inherit from a common base `Person` class.
* **Reusable Attributes:** Common properties such as `user_id`, `name`, and `contact` are defined once in `Person`, preventing redundant code declarations across `Student` and `Warden`.

4. Polymorphosim
### **Application in Design**
* **User Roles:** System components treat `Student` and `Warden` as generic `Person` entities when evaluating baseline access, while executing role-specific behaviors when handling domain events (e.g., logging an issue vs. resolving an issue).


### **Application in Design**
* **`Item`:** Focuses purely on physical item attributes and availability state.
* **`Period`:** Responsible solely for start/end date calculations and extension logic.
* **`Conditions`:** Handles terms, physical state records, and fine rate definitions.
* **`Agreement`:** Binds `Item`, `Period`, and `Conditions` together into a transaction contract.
* **`Issue`:** Manages dispute tracking and escalation workflows independently.
* **`Warden`:** Handles administrative hostelling duties and dispute resolution.