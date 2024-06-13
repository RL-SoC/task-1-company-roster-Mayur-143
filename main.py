"""
This is where the actual working of the program will happen!
We'll be Querying stuff for testing whether your classes were defined correctly

Whenever something inappropriate happens (like a function returning false in people.py),
raise a Value Error.
"""
from people import * # import everything!

if __name__ == "__main__":  # Equivalent to int main() {} in C++.
    last_input = 99
    while last_input != 0:
        last_input = int(input("Please enter a query number:"))

        if last_input == 1:
            name = input("Name:")
            age = int(input("Age: "))
            ID = int(input("ID:"))
            city = input("City:")
            branchcodes = input("Branch(es):")
            branchcodes = list(map(int, branchcodes.split(',')))  # Convert branch codes to a list of integers
            # How will you convert this to a list, given that
            # the user will always enter a comma separated list of branch codes?
            # eg>   2,5
            salary = input("Salary: ")
            salary = int(salary) if salary else None
            # position = input("Position (Junior, Senior, Team Lead, Director): ")
            # position = position if position in ["Junior", "Senior", "Team Lead", "Director"] else "Junior"

            # Create a new Engineer with given details.
            engineer = Engineer(name, age, ID, city, branchcodes,salary=salary) # Change this
            engineer_roster.append(engineer) # Add him to the list! See people.py for definiton
            
        
        elif last_input == 2:
            # Gather input to create a Salesperson
            # Then add them to the roster
            name = input("Name:")
            age = int(input("Age: "))
            ID = int(input("ID:"))
            city = input("City:")
            branchcodes = input("Branch(es):")
            branchcodes = list(map(int, branchcodes.split(',')))
            salary = input("Salary: ")
            salary = int(salary) if salary else None
            Superior = input("Superior ID (leave blank if none): ")
            Superior = int(Superior) if Superior else None  # Convert superior to an integer, or set to None if not provided
            salesman = Salesman(name, age, ID, city, branchcodes, salary=salary, superior=Superior) # Change this
            sales_roster.append(salesman)

        elif last_input == 3:
            ID = int(input("ID: "))
            # Print employee details for the given employee ID that is given. 
            
            found_employee = None
            for employee in engineer_roster + sales_roster:
                if employee.ID == int(ID):
                    found_employee = employee
                    break
            
            if not found_employee: print("No such employee")
            else:
                print(f"Name: {found_employee.name} and Age: {found_employee.age}")
                print(f"City of Work: {found_employee.city}")

                ## Write code here to list the branch names to
                ## which the employee reports as a comma separated list
                ## eg> Branches: Goregaon,Fort
                branch_names = [branchmap[code]['name'] for code in found_employee.branches]
                print(f"Branches: {', '.join(branch_names)}")

                ## ???? what comes here??
                # print(f"Branches: " + ???? )
                print(f"Salary: {found_employee.salary}")
                print(f"Employee ID: {employee.ID}, Superior ID: {employee.superior}")


        elif last_input == 4:
            #### NO IF ELSE ZONE ######################################################
            # Change branch to new branch or add a new branch depending on class
            # Inheritance should automatically do this. 
            # There should be no IF-ELSE or ternary operators in this zone
            ID = int(input("ID: "))
            new_branch = int(input("New Branch Code: "))

            found_employee = None
            for employee in engineer_roster + sales_roster:
                if employee.ID == ID:
                    found_employee = employee
                    break

            if not found_employee:
                print("No such employee")
            else:
                found_employee.migrate_branch(new_branch)
                print("Branch updated successfully")
            #### NO IF ELSE ZONE ENDS #################################################

        elif last_input == 5:
            ID = int(input("Enter Employee ID to promote: "))
            # promote employee to next position
            new_position = input("New Position: ")

            found_employee = None
            for employee in engineer_roster + sales_roster:
                if employee.ID == ID:
                    found_employee = employee
                    break

            if not found_employee:
                print("No such employee")
            else:
                if found_employee.promote(new_position):
                    print("Employee promoted successfully")
                else: 
                    print("Employee already on higher position")

        elif last_input == 6:
            ID = int(input("Enter Employee ID to give increment: "))
            # Increment salary of employee.
            increment_amt = int(input("Increment Amount: "))

            found_employee = None
            for employee in engineer_roster + sales_roster:
                if employee.ID == ID:
                    found_employee = employee
                    break

            if not found_employee:
                print("No such employee")
            else:
                found_employee.increment(increment_amt)
        
        elif last_input == 7:
            ID = int(input("Enter Employee ID to find superior: "))
            # Print superior of the sales employee.
            found_employee = None
            for employee in sales_roster:
                if employee.ID == ID:
                    found_employee = employee
                    break

            if not found_employee:
                print("No such employee")
            else:
                superior_id, superior_name = found_employee.find_superior()
                if superior_id is None:
                    print("No superior found")
                else:
                    print(f"Superior ID: {superior_id}, Name: {superior_name}")
        
        elif last_input == 8:
            ID_E = int(input("Enter Employee ID to add superior: "))
            ID_S = int(input("Enter Employee ID of superior: "))
             # Add superior of a sales employee
            employee = None
            superior = None
            for emp in sales_roster:
                if emp.ID == ID_E:
                    employee = emp
                elif emp.ID == ID_S:
                    superior = emp
                    
            if not employee or not superior: 
                print("No such employee or superior")
            else:
                if employee.add_superior(ID_S):
                    print("Superior added successfully")
                else:
                    print("Failed to add superior")
            

        else:
            raise ValueError("No such query number defined")

            
            

            


            


        






