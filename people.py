"""
We'll try to understand classes in python. 
Check the resources on google classroom to ensure you have gone through everything expected.

"""
###### THESE LISTS HAVE ALREADY BEEN DEFINED FOR YOU ###############
engineer_roster = [] # A list of all instantiated engineer objects
sales_roster = [] # List of all instantiated sales objects
branchmap = {  # A dictionary of dictionaries -> Maps branchcodes to cities and branch names
    0:  { "city": "NYC", "name": "Hudson Yards"},
    1:  { "city": "NYC" , "name": "Silicon Alley"},
    2:  { "city": "Mumbai", "name": "BKC"},
    3:  { "city": "Tokyo", "name": "Shibuya"},
    4:  { "city": "Mumbai", "name": "Goregaon"},
    5:  { "city": "Mumbai", "name": "Fort"}
}
####################################################################

class Employee:
    name : str 
    age : int
    ID : int
    city : str
    branches : list[int] # This is a list of branches (as branch codes) to which the employee may report
    salary : int 

    def __init__(self, name, age, ID, city,\
                 branchcodes, salary = None):
        self.name = name
        self.age = age 
        self.ID = ID
        self.city = city
        self.branches = branchcodes
        if salary is not None: self.salary = salary
        else: self.salary = 10_000 
    
    def change_city(self, new_city:str) -> bool:
        # Change the city 
        # Return true if city change, successful, return false if city same as old city
        if self.city==new_city:
            return False
        self.city=new_city
        return True
        #pass

    def migrate_branch(self, new_code:int) -> bool:
        # Should work only on those employees who have a single 
        # branch to report to. Fail for others.
        # Change old branch to new if it is in the same city, else return false.
        if len(self.branches) != 1:
            return False
        self.branches[0] = new_code
        return True
        #pass

    def increment(self, increment_amt: int) -> None:
        # Increment salary by amount specified.
        self.salary+=increment_amt
        #pass



class Engineer(Employee):
    position : str # Position in organization Hierarchy

    def __init__(self, name, age, ID, city,\
                 branchcodes, position= "Junior", salary = None):
        # Call the parent's constructor
        super().__init__(name, age, ID, city, branchcodes, salary)
        if position in ["Junior", "Senior", "Team Lead", "Director"]:
            self.position = position
        else:
            raise ValueError("Invalid position. Must be one of: Junior, Senior, Team Lead, Director") 
        # Only then set the position. 
        # Check if position is one of  "Junior", "Senior", "Team Lead", or "Director" 
        # Only then set the position. 

    
    def increment(self, amt:int) -> None:
        # While other functions are the same for and engineer,
        # and increment to an engineer's salary should add a 10% bonus on to "amt"
        self.salary+=amt+0.1*amt
        #pass
        
    def promote(self, position:str) -> bool:
        # Return false for a demotion or an invalid promotion
        # Promotion can only be to a higher position and
        # it should call the increment function with 30% of the present salary
        # as "amt". Thereafter return True.
        hierarchy = ["Junior", "Senior", "Team Lead", "Director"]
        current_index = hierarchy.index(self.position)
        new_index = hierarchy.index(position) if position in hierarchy else -1
         # Check for valid promotion
        if new_index > current_index:
            # Call the increment function with 30% of the present salary as "amt"
            self.increment(0.3 * self.salary)
            # Set the new position
            self.position = position
            return True
        else:
            return False
        # pass



class Salesman(Employee):
    """ 
    This class is to be entirely designed by you.

    Add increment (this time only a 5% bonus) and a promotion function
    This time the positions are: Rep -> Manager -> Head.

    Add an argument in init which tracks who is the superior
    that the employee reports to. This argument should be the ID of the superior
    It should be None for a "Head" and so, the argument should be optional in init.
    """
    
    # An extra member variable!
    superior : int # EMPLOYEE ID of the superior this guy reports to
    # Complete all this! Add arguments
    def __init__(self, name, age, ID, city, branchcodes, position="Rep", salary=None, superior=None):
        # Call the parent's constructor
        super().__init__(name, age, ID, city, branchcodes, salary)
        self.position = position if position in ["Rep", "Manager", "Head"] else "Rep"
        self.superior = superior
    
    # def promote 
    def promote(self, position:str) -> bool:
        hierarchy = ["Rep", "Manager", "Head"]
        current_index = hierarchy.index(self.position)
        new_index = hierarchy.index(position) if position in hierarchy else -1
         # Check for valid promotion
        if new_index > current_index:
            # Call the increment function with 30% of the present salary as "amt"
            self.increment(0.05 * self.salary)
            # Set the new position
            self.position = position
            return True
        else:
            return False

    def increment(self, amt: int) -> None:
        # Increment the salary by the amount specified with a 5% bonus
        self.salary += amt + 0.05 * amt 

    def find_superior(self) -> tuple[int, str]:
        # Return the employee ID and name of the superior
        # Report a tuple of None, None if no superior.
        if self.superior is None:
            return None, None
        for emp in engineer_roster + sales_roster:
            if emp.ID == self.superior:
                return emp.ID, emp.name
        return None, None 
    

    def add_superior(self,superior_id:int) -> bool:
        # Add superior of immediately higher rank.
        # If superior doesn't exist return false,
        if superior_id in engineer_roster or superior_id in sales_roster:
            self.superior = superior_id
            return True
        else:
            return False
        #pass


    def migrate_branch(self, new_code: int) -> bool:
        # This should simply add a branch to the list; even different cities are fine
        self.branches.append(new_code)
        return True

    





    
    