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

git checkout -b feature-branch

git add .

git commit -m "Any message"

git push origin feature-branch

gh pr merge 1 --merge

git checkout (branchname)

git status

git checkout -f (branchname)

git pull origin master