# 📒 Ansible Role: noteapp

An Ansible Galaxy role that deploys a simple Flask-based note-taking web application on Linux hosts (tested on Amazon Linux 2023). This role automates the installation, configuration, and management of a minimal note-taking app using Flask and SQLite.

---

## 🚀 Features

- ✅ Installs required packages (Python 3, Flask, SQLite)
- ✅ Deploys `app.py` and `index.html`
- ✅ Initializes an SQLite database
- ✅ Sets up a `systemd` service to auto-start the app
- ✅ App listens on port **80**
- ✅ Compatible with dynamic EC2 inventory

---

## 🧾 Requirements

- Ansible 2.10+
- Python 3 on target machines
- Systemd-based Linux distro (Amazon Linux 2023, RHEL, CentOS, etc.)
- Port 80 open in security group (for web access)

---

## 📦 Role Variables

No variables are required by default. You may optionally override:

```yaml
noteapp_app_dir: /opt/noteapp
noteapp_port: 80
🗂️ Directory Structure



ansible-project/
├── aws_ec2.yaml              # Dynamic inventory file (optional)
├── deploy.yml                # Playbook to call the role
├── noteapp/                  # Ansible Galaxy role directory
│   ├── tasks/
│   │   └── main.yml
│   ├── files/
│   │   ├── app.py
│   │   └── noteapp.service
│   ├── templates/
│   │   └── index.html
│   ├── meta/
│   │   └── main.yml
⚙️ Setup Steps
1. ✅ Prepare Environment
Launch two EC2 instances (Amazon Linux 2023):

controller → where Ansible runs

agent → where the Flask app is deployed

SSH into controller:

bash

sudo dnf install -y python3
pip3 install ansible
ansible --version
2. ✅ Create and Build Your Role

mkdir ansible-project && cd ansible-project
ansible-galaxy init noteapp
Populate:

tasks/main.yml

files/app.py

files/noteapp.service

templates/index.html

meta/main.yml

3. ✅ Create the Deployment Playbook
deploy.yml:


- name: Deploy Flask Note Taking App
  hosts: all
  become: true

  roles:
    - salwatamer-max.noteapp
4. ✅ Run the Playbook
If you're using EC2 dynamic inventory:


ansible-playbook -i aws_ec2.yaml deploy.yml
🌐 Accessing the App
Once deployed successfully, open a browser and navigate to:


http://<your-ec2-public-ip>/
You should see the Note Taking App UI.


📥 Installation from Galaxy
Once your role is published to Galaxy:


ansible-galaxy install salwatamer-max.noteapp
Then include it in any playbook:

yaml

roles:
  - salwatamer-max.noteapp
👩‍💻 Author
Salwa Tamer

GitHub: salwatamer-max

Ansible Galaxy: salwatamer-max.noteapp


📷 Screenshots

<img width="1920" height="1080" alt="Screenshot (112)" src="https://github.com/user-attachments/assets/22faa03b-c9e1-49a3-8230-3fa4c432e517" />


