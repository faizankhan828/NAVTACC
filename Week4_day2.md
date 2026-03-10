Local 
|
'
main
|
KAN1

1). Create branch -> local
2). Push branch -> local
3). Create PR -> remote
4). Merge PR -> remote
5). Pill fresh main -> local



Commands must run for converting the brach and do changes and remote all above tasks

git checkout -b feature-branch --> Create a new branch and switch to it.

git add . --> Add all changed files to the staging area.

git commit -m "Any message" --> Store changes in the local repository with a message.

git push origin feature-branch --> Upload your local branch to the remote repository.

gh pr merge 1 --merge --> Merge a Pull Request using GitHub CLI.

git checkout (branchname) --> Switch to another branch.

git status -->Check the current state of your repository.

git checkout -f (branchname) --> Force switch branch discarding local changes.

git pull origin master --> Download latest code from remote branch.


