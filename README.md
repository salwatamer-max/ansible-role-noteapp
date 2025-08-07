# 📒 Ansible Role: noteapp

This Ansible role deploys a simple Flask-based note-taking web application on a target Linux host (Amazon Linux 2023 or similar). The app runs on **port 80** and uses **SQLite** as the backend.

---

## 📁 Features

- 📦 Installs required packages (Python, Flask, SQLite)
- 🚀 Deploys a basic Flask web app (`app.py` + `index.html`)
- 🗃️ Creates and initializes an SQLite database
- ⚙️ Sets up a **systemd** service to run the app on boot
- 🌐 App runs on **http://your_server_ip:80**

---

## 🏗️ Role Directory Structure

noteapp/
├── defaults/
├── files/
│   ├── app.py
│   └── noteapp.service
├── handlers/
├── meta/
│   └── main.yml
├── tasks/
│   └── main.yml
├── templates/
│   └── index.html
├── tests/
└── vars/


yaml
Copy
Edit

---

## 🔧 Requirements

- ✅ Ansible 2.10+
- ✅ Python 3.x
- ✅ Systemd-based OS (Amazon Linux, RHEL, CentOS)
- ✅ Port 80 open in EC2 security group

---

## ⚙️ Variables

No default variables are required. You can override:

| Variable       | Default           | Description                        |
|----------------|-------------------|------------------------------------|
| `noteapp_port` | `80`              | Port Flask app will run on         |
| `noteapp_dir`  | `/opt/noteapp`    | Directory for app and database     |

---

## 🚀 Usage Example

### 1. Create Dynamic Inventory File

Make sure `aws_ec2.yaml` is in your project and working.

### 2. Create the Playbook `deploy.yml`:

```yaml
- name: Deploy note-taking app
  hosts: all
  become: true
  roles:
    - salwatamer-max.noteapp
3. Run the Playbook
bash
Copy
Edit
ansible-playbook -i aws_ec2.yaml deploy.yml
🌍 Access the App
After deployment, open your browser and go to:

cpp
Copy
Edit
http://<your_ec2_public_ip>
🖼️ Screenshot
Here’s what the NoteApp looks like:

<img width="800" alt="NoteApp Screenshot" src="https://github.com/user-attachments/assets/22faa03b-c9e1-49a3-8230-3fa4c432e517" />
📦 Install from Ansible Galaxy
Once published, use:

bash
Copy
Edit
ansible-galaxy install salwatamer-max.noteapp
📜 Manual Steps Summary
Create EC2 instances (1 controller, 1 agent)

Initialize Ansible Galaxy role:

bash
Copy
Edit
ansible-galaxy init noteapp
Build role (tasks, files, templates, meta)

Create inventory and playbook

Run with:

bash
Copy
Edit
ansible-playbook -i aws_ec2.yaml deploy.yml
👩‍💻 Author
Salwa Tamer

GitHub: @salwatamer-max

Ansible Galaxy: salwatamer-max.noteapp

yaml
Copy
Edit
