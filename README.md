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

