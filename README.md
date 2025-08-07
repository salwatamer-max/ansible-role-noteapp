📦 Ansible Role: noteapp
This Ansible role deploys a simple Flask-based note-taking web application on a target Linux host (Amazon Linux 2023 or similar). The app runs on port 80 and uses SQLite as the backend.

📁 Features
Installs required packages (Python, Flask, SQLite)

Deploys a basic Flask web app with app.py and index.html

Creates and initializes SQLite database

Sets up a systemd service to run the app on boot

Listens on http://<server-ip>/ (port 80)

🚀 Role Variables
No default variables needed. You can customize paths if desired.

📂 Directory structure
<img width="1000" height="1000" alt="image" src="https://github.com/user-attachments/assets/5466ace7-c166-44f6-ba63-465a2749da08" />
Steps: 
1- Step 1: Create an AWS EC2 Instances amazon linux one for the controller and other 
for the noteapp 
2- Connect to the controller machine ssh via vsc or terminal  
1. Install prerequisites 
on the controller machine
sudo dnf install -y python3   
pip3 install ansible 
ansible –version 

  ✅ 2. Create Ansible Galaxy role
ansible-galaxy init noteapp # under the ansible-project directory
cd noteapp
This gives you the standard Galaxy role structure.
  ⚙️ Step-by-step: Populate each file

🔹 tasks/main.yml

🔹 files/app.py

 🔹 Files/noteapp.service

🔹 meta/main.yml (for Galaxy)

🔹templates/index.html

If you have dynamic inventory aws_ec2.yaml under the ansible-project directory in order to run the ansibe role and test we must create the deploy.yml file under the ansible-project directory to connect the ansible role with my dynamic inventory file

Run the playbook to check that its running 
ansible-playbook -i aws_ec2.yaml deploy.yml
go to the browser http://<your-ec2-instance-public-ip>/  to see the app

🧪 Example Playbook you will create it under the ansible-project directory before running 
playbook.yaml
- name: Deploy note-taking app
  hosts: all
  become: true
  roles:
    - salwatamer-max.noteapp
 
🔧 Requirements
Ansible 2.10+

Python 3

Systemd-based host (Amazon Linux, RHEL, CentOS, etc.)

Ports 80 open in your firewall/security group

📥 Installation
After importing this role on Ansible Galaxy:
ansible-galaxy install salwatamer-max.noteapp
🌐 Accessing the App
After deployment, visit:
http://<your-server-ip>/
You should see the Note Taking App UI.
screenshots:
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/c7919cb1-1ec0-44b6-9cbb-f8f78d3caa52" />

🙋‍♂️ Author
Salwa Tamer
GitHub: salwatamer-max
