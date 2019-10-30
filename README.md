# Chicago-ds-102819

Welcome to the class! We're SO EXCITED to have you here 😊 


## Instructions

- You want to **keep your fork updated**, ideally every day.

### First time Setup

- Fork this GitHub repo `learn-co-students/chicago-102819` to `<your_github_username>/chicago-102819`.
![Forking a github Repo](https://help.github.com/assets/images/help/repository/fork_button.jpg)

If you still need help with forking a github repo, here are [more resources](https://help.github.com/en/github/getting-started-with-github/fork-a-repo).

In the terminal, `cd` inside the directory you are going to keep this program's files and work.

```bash
git clone https://github.com/<your_github_username>/chicago-102819.git
cd chicago-102819
git remote add upstream https://github.com/learn-co-students/chicago-102819.git
```

## Get the changes from the Class' Repo
Keeping your personal fork updated with the class' github repo us very important, as the Instruction team updates it almost every day.

Each time you want to update, you have to be in your local master branch `git checkout master`:

```bash
git fetch upstream
git rebase upstream/master
```

## Update your personal fork's changes

While in your local master branch, type in the terminal

```bash
git push origin master
```
