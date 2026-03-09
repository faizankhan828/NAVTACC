'''
Git & GitHub Version Control System
'''

#Version Control System (VCS) is a software tool that helps developers manage changes to their code over time. 
# It allows multiple developers to collaborate on a project, track changes, and revert to previous versions
#  if needed. Git is one of the most popular VCS, and GitHub is a web-based platform that
#  provides hosting for Git repositories.

'''
Types of Version Control Systems:
1. Local Version Control Systems: These systems store all the version history on the local machine. 
   Examples include RCS and SCCS.
2. Centralized Version Control Systems: These systems have a central server that stores all the version history.
   Examples include CVS and Subversion.
3. Distributed Version Control Systems: These systems allow each developer to have a complete copy of the 
repository,including the entire version history.
    Examples include Git and Mercurial.
'''

'''
Git Workflow:
Local --> Our PC stored repository. It can access by us only.
Remote --> GitHub stored repository. It can access by everyone.

'''

#The new verion we have bitbucket and gitlab as well.Same as github but they have some different features.
#Git is a free and open source distrubuted version control system designed 
#to handle everything from small to very large projects with speed and efficiency.

#We make github remote changes and use pipeline continuos integration (CI) and continuos deployment (CD) for our project.
#and upload on the server and we can access it from anywhere and we can share it with anyone.

'''
Repo---> There are 3 branches make:
1. dev branch---> for development
2. staging branch---> for testing
3. main branch---> for production

When changes in main branch it can make pipeline and deploy on the server. IT DO THE GIT ACTIONS AUTOMATICALLY.
When we make changes in dev branch we can do unit testing

'''

'''
Git Architecture:
Modified files --> You have changed the files but not yet staged or commited it your database yet.
Staged files --> You have marked the modified files to go into your next commit snapshot.
Committed files --> You have safely stored your changes in your local database.

'''

'''
Git Object Types in easy words:
Blob --> A blob is a file in Git. It stores the content of a file.
Tree --> stores a directory listing (filenames + pointers to blobs/subtrees).
Commit --> stores a pointer to a tree + metadata (author, message, parent commmits).
Tag --> stores a pointer to a specific commit with extra metadata (name, message).
'''


#We can't update changes in main branch we make new branch then update.
#We change in main only when we pull from remote branch and merge it with main branch.

'''
Git Important Commands in easy words:
git init  -> Initialize a new Git repository.
git add . -> Stage all changes in the current directory for the next commit.
git commit -m "message" -> Commit the staged changes with a descriptive message.
git status -> Show the status of the working directory and staging area.
git log -> Show the commit history.
git branch -> List all branches in the repository.
git checkout -b branch_name -> Create and switch to a new branch.
git merge branch_name -> Merge the specified branch into the current branch.
git push origin branch_name -> Push the local branch to the remote repository.
git clone repository_url -> Clone a remote repository to your local machine.
git pull origin branch_name -> Fetch and merge changes from the remote branch to your local branch.
'''''''''''''''''''''

