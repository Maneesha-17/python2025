# python2025

## Git Commands

To clone a repository(not needed in codespace, needed for local development):

    git clone https URL

To list the local branches:

    git branch

To create a branch:

    git checkout -b class01

To see the latest local status:

    git status

To exactly see the changes made on a single file:

    git diff

To stage the changes for particular file:

    git add <filename>

To stage all the changes at once:

    git add *
     
To commit the changes:

    git commit -m "commit message"

To push the changes:

    git push origin <sourceBranch>

        class01 -> main
    ex: git push origin class01

### Daily

To check the branch is clean,

    git status

To check to the main branch

    git checkout main

To get the latest changes

     git pull origin main

To create new branch

    git checkout -b <new branch name>