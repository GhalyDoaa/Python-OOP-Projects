
import sys
from appliction import User , Project
import validations as v

 

_logged_user = None
class Menu:
    """Display a menu and respond to choices when run."""
    def __init__(self):
        self.choices = {
        "1": self.login,
        "2": self.sign_up,
        "3": self.add_new_project,
        "4": self.modify_project,
        "5":self.delete_project,
        "6":self.show_projects,
        "7": self.quit,
        }
    def display_menu(self):
        print("")

        print(
        """
            *-*-*-*-*-*-*-*-
            Crowd Fund Menu
            *-*-*-*-*-*-*-*-
            "1": Login
            "2": Sign up
            "3": New project
            "4": Modify project
            "5": Delete project
            "6": Show projects
            "7": Quit

            *-*-*-*-*-*-*-*-*-*   
        """
        )

    def run(self):
        """Display the menu and respond to choices."""
        while True:
            self.display_menu()
            choice = input(" *-*-*-*-*-*-*-* \n Enter an option: \n *-*-*-*-*-*-*-*")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))
    

    def _take_email():
        
        while True:
            email = input(" *-*-*-*-*-*-*-* \n inter your email \n *-*-*-*-*-*-*-*")
            if not v.check_email(email):
                print("enter a valid email pleas")
                email = input(" *-*-*-*-*-*-*-* \n re-inter your email \n *-*-*-*-*-*-*-*")
            else:
                return email

    def login(self):
        global logged_user
        email = Menu._take_email()
    
        while True:
            if User.check_user(email):
                password = input(" *-*-*-*-*-*-*-* \n inter your password \n *-*-*-*-*-*-*-*")
                user =User.login(email,password)
                if not user:
                    print("""
                    *-*-*-*-*-*-*-*-*-
                    password is wrong
                    please try again ..!
                    *-*-*-*-*-*-*-*-*-
                    """)
                else :
                    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*") 
                    print("welcome back {0} {1} ".format(user["fname"],user["lname"]))   
                    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                    global _logged_user 
                    _logged_user= user 
                    break 

            else:
                print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*
                no user with such email found..
                sign up first ..
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                """) 
                break
       


    def sign_up(self):
        while True:
            user_fname = input(" *-*-*-*-*-*-*-* \n inter your first name\n *-*-*-*-*-*-*-*")
            if not v.check_name(user_fname) :
                print("""
                        *-*-*-*-*-*-*-**-*-*-*
                        not valid first name ,
                        should be a string of chars.
                        please try again ..!
                        *-*-*-*-*-*-*-**-*-*-*
                
                    """)
            else :
                break          
        while True:
            user_lname = input(" *-*-*-*-*-*-*-* \n inter your last name\n *-*-*-*-*-*-*-*")
            if not v.check_name(user_lname) :
                print("""
                        *-*-*-*-*-*-*-**-*-*-*
                        not valid last name ,
                        should be a string of chars.
                        please try again ..!
                        *-*-*-*-*-*-*-**-*-*-*
                
                    """)
            else :
                break 

        user_email = Menu._take_email()

        while True:
            user_password = input(" *-*-*-*-*-*-*-* \n create login password: \n *-*-*-*-*-*-*-*")
            user_password_again = input("*-*-*-*-*-*-*-* \n confirm login password: \n *-*-*-*-*-*-*-*")
            if user_password != user_password_again:
                print("""
                        *-*-*-*-*-*-*-**-*-*-*
                        not matched password,
                        please try again ..!
                        *-*-*-*-*-*-*-**-*-*-*
                
                    """)
            else :
                break    

        while True:
            user_phone = input(" *-*-*-*-*-*-*-* \n create login phone: \n *-*-*-*-*-*-*-*")
            if not v.check_phone(user_phone):
                print("""
                        *-*-*-*-*-*-*-**-*-*-*
                        not correct number,
                        please try again as an Egyption number..!
                         ex:- 01xxxxxxxxx
                        *-*-*-*-*-*-*-**-*-*-*
                
                    """)
            else :
                break  

        user = User(user_fname,user_lname,user_email,user_password,user_phone)
        user.add_new_user()
        print("""
            *-*-*-*-*-*-*-**-*-*-*
            Your account is ready,
            please log in with 
            email and password..!
            *-*-*-*-*-*-*-**-*-*-*
                
        """)
        
    def show_projects(self,projects=None):
        if not projects:
            projects = Project.get_user_projects(_logged_user["id"])
            if projects:
                for project in projects:
                    print("{0}:- {1}\n{2}".format(project["project_id"], project["title"], project["details"]))
            else:
                print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                print("You havn't added any Projects yet..! ")
                print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")      
        else :
            print("{project_id}:- {title}\n{details}".format(**projects)) 
    def add_new_project(self):
        while True:
            title = input(" *-*-*-*-*-*-*-* \n inter your project title\n *-*-*-*-*-*-*-*")
            if not v.check_name(title) :
                print("""
                        *-*-*-*-*-*-*-**-*-*-*
                        not valid title ,
                        should be a string of chars.
                        please try again ..!
                        *-*-*-*-*-*-*-**-*-*-*
                
                    """)
            else :
                break         

        while True:
            details = input(" *-*-*-*-*-*-*-* \n inter your project details\n *-*-*-*-*-*-*-*")
            if not details :
                print("""
                        *-*-*-*-*-*-*-**-*-*-*
                        not valid details ,
                        should be a string of chars.
                        please try again ..!
                        *-*-*-*-*-*-*-**-*-*-*
                
                    """)
            else :
                break         

        while True:
            total_target = input(" *-*-*-*-*-*-*-* \n inter your project total_target\n *-*-*-*-*-*-*-*")
            if not total_target :
                print("""
                        *-*-*-*-*-*-*-**-*-*-*
                        not valid details ,
                        should be a string of chars.
                        please try again ..!
                        *-*-*-*-*-*-*-**-*-*-*
                
                    """)
            else :
                break
        while True:
            start_date = input(" *-*-*-*-*-*-*-* \n inter your project start date\n *-*-*-*-*-*-*-*")
            if not v.check_date(start_date) :
                print("""
                        *-*-*-*-*-*-*-**-*-*-*
                        not valid start date ,
                        please try again ..!
                        *-*-*-*-*-*-*-**-*-*-*
                
                    """)
            else :
                break
        while True:
            end_date = input(" *-*-*-*-*-*-*-* \n inter your project end date\n *-*-*-*-*-*-*-*")
            if not v.check_date(end_date) :
                print("""
                        *-*-*-*-*-*-*-**-*-*-*
                        not valid end date ,
                        please try again ..!
                        *-*-*-*-*-*-*-**-*-*-*
                
                    """)
            else :
                break
        project = Project(_logged_user["id"],title,details,total_target,start_date,end_date)
        if project.add_new_project():
            print("""
                    *-*-*-*-*-*-*-**-*-*-*
                    Project added succeccfully ..!
                    *-*-*-*-*-*-*-**-*-*-*     
                """)
            self.show_projects(project.__dict__) 


    def modify_project(self):
        project_id = input(" *-*-*-*-*-*-*-* \n enter project id to modify \n *-*-*-*-*-*-*-*")
        
        while True:
            if not project_id:
                print("""
                        *-*-*-*-*-*-*-**-*-*-*
                        re enter a valid number..!
                        *-*-*-*-*-*-*-**-*-*-*     
                    """)
                project_id = input(" *-*-*-*-*-*-*-* \n re-enter project id to modify \n *-*-*-*-*-*-*-*")
    
            else:
                break
            
        if not Project._check(project_id,_logged_user["id"]):  
            print("""
                *-*-*-*-*-*-*-**-*-*-*
                No project with such an ID..!
                *-*-*-*-*-*-*-**-*-*-*     
            """) 

        else:
            print("""
                *-*-*-*-*-*-*-**-*-*-*
                This project will be updated..!
                *-*-*-*-*-*-*-**-*-*-*  
            """)
            project =Project.get_my_project(project_id,_logged_user["id"])
            self.show_projects(project)

            title = input(" *-*-*-*-*-*-*-* \n inter your project title\n *-*-*-*-*-*-*-*")
            if not v.check_name(title) :
                title = project["title"]
                
            details = input(" *-*-*-*-*-*-*-* \n inter your project details\n *-*-*-*-*-*-*-*")
            if not details :
                details = project["details"]

            total_target = input(" *-*-*-*-*-*-*-* \n inter your project total_target\n *-*-*-*-*-*-*-*")
            if not total_target :
                total_target = project["total_target"]
        
            start_date = input(" *-*-*-*-*-*-*-* \n inter your project start date\n *-*-*-*-*-*-*-*")
            if not v.check_date(start_date) :
                start_date = project["start_date"]

            end_date = input(" *-*-*-*-*-*-*-* \n inter your project end date\n *-*-*-*-*-*-*-*")
            if not v.check_date(end_date) :
                end_date = project["end_date"]


            project = Project(_logged_user["id"],title,details,total_target,start_date,end_date)
            
            if project.modify_project(_logged_user["id"],project_id):
                print("""
                        *-*-*-*-*-*-*-**-*-*-*
                        Project updated succeccfully ..!
                        *-*-*-*-*-*-*-**-*-*-*     
                    """)
            else:
                print("""
                        *-*-*-*-*-*-*-**-*-*-*
                        Failed to update Project  ..!
                        *-*-*-*-*-*-*-**-*-*-*     
                    """)

            

    
    def delete_project(self):  
        project_id = input(" *-*-*-*-*-*-*-* \n enter project id to delete \n *-*-*-*-*-*-*-*")
        while True:
            if not project_id:
                print("""
                        *-*-*-*-*-*-*-**-*-*-*
                        re enter a valid number..!
                        *-*-*-*-*-*-*-**-*-*-*     
                    """)
                project_id = input(" *-*-*-*-*-*-*-* \n re-enter project id to delete \n *-*-*-*-*-*-*-*")
    
            else:
                break
            
        if not Project._check(project_id,_logged_user["id"]):  
            print("""
                *-*-*-*-*-*-*-**-*-*-*
                No project with such an ID..!
                *-*-*-*-*-*-*-**-*-*-*     
            """) 

        else:
            print("""
                *-*-*-*-*-*-*-**-*-*-*
                This project will be deleted..!
                *-*-*-*-*-*-*-**-*-*-*  
            """)
            project =Project.get_my_project(project_id,_logged_user["id"])
            self.show_projects(project)


            Project.delete_project(project_id,_logged_user["id"])  
            print("""
                *-*-*-*-*-*-*-**-*-*-*
                    project deleted..!
                *-*-*-*-*-*-*-**-*-*-*     
            """)                


    def quit(self):
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*") 
        print("Thank you for using Crowd Funding today.")
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*") 
        sys.exit(0) 

if __name__ == "__main__":
    Menu().run()                    