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

📂 Directory Structure
css
Copy
Edit
noteapp/
├── tasks/
│   └── main.yml
├── files/
│   ├── app.py
│   ├── index.html
│   └── noteapp.service
├── meta/
│   └── main.yml
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
