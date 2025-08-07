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
yaml
Copy
Edit

---

### ✅ With this fixed version:

```markdown
## 🚀 Usage Example

### 1. Create Dynamic Inventory File

Make sure `aws_ec2.yaml` is in your project and working.

### 2. Create the Playbook `deploy.yml`

Create a file named `deploy.yml` and add the following content:

```yaml
- name: Deploy note-taking app
  hosts: all
  become: true
  roles:
    - salwatamer-max.noteapp
3. Run the Playbook
Use the following command to run the playbook:

bash
Copy
Edit
ansible-playbook -i aws_ec2.yaml deploy.yml
