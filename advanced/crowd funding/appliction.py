import validations as v
import os
import json

class User():
    def __init__(self,fname,lname,email,password,phone):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.password = password
        self.phone = phone
        self.id = User.get_max_id() +1
        #print(locals)
        #print(globals)
        #print(help(User))


    def check_user(email):
        """check if user exists"""
        for user in User.get_users():
            if email in user["email"]:
                return True
        return False         


    def get_max_id():
        user_id =[]
        for user in User.get_users():
            user_id.append(user["id"])
        return max(user_id) if user_id else 0

    def add_new_user(self):
        users = User.get_users()
        try:
            handler = open("users.json", "w")
        except:
            return False
        users.append(self.__dict__)
        handler.write(json.dumps(users))        
        handler.close()
        return True

    def get_user_info(self,user_id):
        """return user dictionry"""
        for user in User.get_users():
            if user_id in user["id"]:
                return user

    def get_users():
        """return a list of users dictionaries from json"""
        if os.stat("users.json").st_size != 0 :
            handler = open("users.json", "r")
            users = json.load(handler)
            handler.close()
            #print(users)
            return users 
        return []

        
    def get_user_id(self):
        """returns user id """
        return self.id

    def login(email, password):
        for user in User.get_users():
            if user["email"] == email and user["password"] == password:
                return user
        return False


class Project():
    
    def __init__(self,user_id,title,details,total_target,start_date,end_date):
        self.user_id = user_id
        self.title = title
        self.details = details
        self.total_target = total_target
        self.start_date = start_date
        self.end_date = end_date
        self.project_id = Project.get_max_id() +1   

    def get_max_id():
        projects_ids = [ project["project_id"] for project in Project.get_projects() ]
        return max(projects_ids) if projects_ids else 0

    def _check(project_id,user_id):
        projects = Project.get_user_projects(user_id)
        for project in projects:
            if project["project_id"] ==int(project_id) :
                print("found")
                return True
        
        return False        
        



    def get_projects():
        #return a list of projects dictionaries from json
        if os.stat("projects.json").st_size != 0 :
            handler = open("projects.json", "r")
            projects = json.load(handler)
            handler.close()
            #print(projects)
            return projects 
        return []        
        

    def get_user_projects(user_id):  
        #return all projects for aspecific user dictionry
        projects = Project.get_projects()
        #user_ids=[project['user_id'] for project in projects]
        user_projects=[]
        for project in projects:
            if project["user_id"] ==user_id:
                user_projects.append(project)
        return user_projects           

    def get_my_project(project_id,user_id):
        projects = Project.get_user_projects(user_id)

        for project in projects:
            if project["project_id"] == int(project_id ):
                return project



    def delete_project(project_id,user_id): 
        projects = Project.get_user_projects(user_id)
        for index,project in enumerate(projects):
            if project["project_id"] ==int(project_id):
                #print("project is heeeeeeere")
                del projects[index]           
        try:
            handler = open("projects.json", "w")
        except:
            return False
        #print(projects)
        handler.write(json.dumps(projects))        
        handler.close()
        return True

    def add_new_project(self):
        projects = Project.get_projects()
        try:
            handler = open("projects.json", "w")
        except:
            return False
        projects.append(self.__dict__)  #A dictionary or other mapping object used to store an object’s (writable) attributes.
        handler.write(json.dumps(projects))        
        handler.close()
        return True
        
    def modify_project(self,user_id,project_id):
        project = Project.get_my_project(project_id,user_id)
        Project.delete_project(project_id,user_id)
        projects = Project.get_projects()
        #print("my prooo",project)
        if project != None:    
            project.update(title=self.title , details='value2',total_target=self.total_target,start_date=self.start_date,end_date=self.end_date)
    
            try:
                handler = open("projects.json", "w")
            except:
                return False
            projects.append(project)    
            handler.write(json.dumps(projects))
            handler.close()
            return True
        return False


# resourses https://towardsdatascience.com/6-approaches-to-validate-class-attributes-in-python-b51cffb8c4ea

