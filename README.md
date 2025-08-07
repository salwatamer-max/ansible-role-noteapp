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
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/5466ace7-c166-44f6-ba63-465a2749da08" />

.
└── ansible-project
    ├── ansible.cfg
    ├── ansible.pem
    ├── aws_ec2.yaml
    ├── deploy.yml
    └── noteapp
        ├── README.md
        ├── defaults
        │   └── main.yml
        ├── files
        │   ├── app.py
        │   ├── index.html
        │   └── noteapp.service
        ├── handlers
        │   └── main.yml
        ├── meta
        │   └── main.yml
        ├── playbook.yml
        ├── requirements.yml
        ├── tasks
        │   └── main.yml
        ├── templates
        │   └── index.html.j2
        ├── tests
        │   ├── inventory
        │   └── test.yml
        └── vars
            └── main.yml


🧪 Example Playbook
yaml
- name: Deploy note-taking app
  hosts: webservers
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

📝 License
MIT

🙋‍♂️ Author
Salwa Tamer
GitHub: salwatamer-max
