#!/usr/bin/python3
from colorama import init, Fore, Style
from models.task import Task
from models.goal import Goal
from models import storage
from models.goal_type import Goal_type
from datetime import date as dt
from models.project import Project
from models.resource import Resource
from models.task_member import Task_member
from models.user import User
from models.collaboration import Collaboration
from models.collaboration_member import Collaboration_member
from models.project_member  import Project_member

init(autoreset=True)

storage.close()
storage.reload()

def add_new_users():
    for i in range(30):
        new_user = User(
        first_name = f"{i}FirstName",
        last_name = f"{i}LasttName",
        skills = ["js", "debugging", "machine", "learning"],
        profile_picture="profile_picture_for_user" + str(i),
        username=f"user No.{i}",
        email= f"userNo.{i}@example.com",
        password= f"passwordforuserNo.{i}"
    )
    
    
        new_user.save()
    print(f"{Fore.BLUE}users successfully inserted!")

def add_new_goal_type(goal_types):
    print(f"adding new goal type")
    for goal_type in goal_types:
        print(goal_type)

    def get_placeholder_description(name):
        return f"Goals related to {name}"

    for goal_type in goal_types:
        # Create a new Goal_type object with unique data (modify as needed)
        print(f"adding new goal type {goal_type}")
        name = goal_type
        description = get_placeholder_description(name) 
        new_goal_type = Goal_type(name=name, description=description)
        new_goal_type.save()
      
    print(f"{Fore.BLUE}goal types successfully inserted!")



########################################




# #create some goals
 
def add_goals(goal_type_ids):
    for i in range(len(goal_type_ids)):
  # Create a new Goal object with unique data (modify as needed)
        new_goal = Goal(
            name=f"Sample Goal {i+1}",
            description=f"This is a sample goal description for goal {i+1}",
            target_completion_date=dt(year=2024, month=8, day=1+i),  
            is_public=True if i % 2 == 0 else False,  
            type= goal_type_ids[i]
        )
        new_goal.save()

    print(f"{Fore.BLUE}goals successfully inserted!")




# ###################################################

 



# Create some Collaboration objects with sample data
def add_collab(user_ids, goal_ids):
    for i in range(len(goal_ids)):
        new_collab = Collaboration(admin_id=user_ids[i],
                             goal_id=goal_ids[i],
                             is_public=True if i % 2 == 0 else False,
                             description=f"Helping John achieve his personal goal{i}")
        new_collab.save()

    print(f"{Fore.BLUE}collaborations successfully inserted!")




def add_projects(goal_ids, collab_ids):
    for i in range(len(goal_ids)):
        new_prject = Project(
            name=f"Sample Project {i+1}",
            description=f"This is a sample project description for project {i+1}",
            collab_id = collab_ids[i],
            goal_id=goal_ids[i],
            is_public=True if i % 2 == 0 else False,
            start_date=dt(year=2024, month=7, day=1+i),
            end_date=dt(year=2024, month=8, day=1+i)
        )
        new_prject.save()
    print(f"{Fore.BLUE}projects added successfully")

def add_project_member(project_ids,user_ids, goal_ids):
    for i in range(len(project_ids)):
        new_project_member = Project_member(
                project_id = project_ids[i],
                goal_id = goal_ids[i],
                user_id = user_ids[i]
        )
        new_project_member.save()
    print(f"{Fore.BLUE}project members added sucessfully")






def add_new_resource(user_ids, collab_ids):
    for i in range(len(collab_ids)):
        new_resource = Resource(
            name=f"Sample Resource {i+1}",
            description=f"This is a sample resource description for resource {i+1}",
            collaboration_id = collab_ids[i],
            url=f"http://the_for_{i}",
            uploader=user_ids[i],
            visible=True if i % 2 == 0 else False,
        )
        new_resource.save()
    print(f"{Fore.BLUE}resources added successfully")
        
        
def new_task(user_ids, goal_ids, project_ids ):
    for i in range(len(project_ids)):
        new_task=Task(
            goal_id = goal_ids[i],
            project_id = project_ids[i],
            name = f"the name for task - {i}",
            description = f"the description for task - {i}",
            start_date =  dt(year=2024, month=7, day=1+i),
            end_date =  dt(year=2024, month=8, day=1+i),
            uploader = user_ids[i]
            )
        new_task.save()
    print(f"{Fore.BLUE}tasks added successfully")

def new_task_member(task_ids, user_ids, project_ids):
    for i in range(len(task_ids)):
        new_task_member = Task_member(
            user_id=user_ids[i],
            task_id=task_ids[i],
            project_id = project_ids[i]
        )
        new_task_member.save()
    print(f"{Fore.BLUE}new task member added")

def new_collab_m(user_ids, collab_ids):
    for i in range(len(collab_ids)):
        for j in range(len(user_ids)):
            new_collab_m = Collaboration_member(
                           user_id = user_ids[i],
                           collaboration_id = collab_ids[i]
                           )
            new_collab_m.save()
    print(f"{Fore.BLUE}new c member added")



if __name__ == "__main__":
    
    try:

        goal_types = [
            "Personal", "Professional", "Financial", "Health & Fitness",
            "Education", "Travel", "Relationships", "Creative",
            "Productivity", "Community", "Environmental", "Social Justice",
            "Spiritual", "Relaxation", "Adventure", "Learning",
            "Career Development", "Family", "Wellbeing"
        ]


        add_new_users()
        users = storage.all(User).items()
        user_ids = [k.split(".")[-1] for k,v  in users]


        add_new_goal_type(goal_types)
        goal_types = storage.all(Goal_type).items()
        goal_type_ids = [k.split(".")[-1] for k,v  in goal_types]


        add_goals(goal_type_ids)
        goals = storage.all(Goal).items()
        goal_ids = [k.split(".")[-1] for k,v  in goals]




        add_collab(user_ids, goal_ids)
        collabs =storage.all(Collaboration).items()
        collab_ids = [k.split(".")[-1] for k,v  in collabs]

        
        new_collab_m(user_ids, collab_ids)
        
        add_new_resource(user_ids, collab_ids)


        add_projects(goal_ids, collab_ids)
        projects = storage.all(Project).items()
        project_ids = [k.split(".")[-1] for k,v  in projects]

        add_project_member(project_ids, user_ids, goal_ids)


        new_task(user_ids, goal_ids, project_ids)
        tasks = storage.all(Task).items()
        task_ids = [k.split(".")[-1] for k,v  in tasks]

        new_task_member(task_ids, user_ids, project_ids)

    except Exception as e:
        print(f"{Fore.RED}failed {e}")
    else:
        print(f"\n\n{Style.BRIGHT}{Fore.GREEN}The code processed successfully........\n\n")
      
    
   