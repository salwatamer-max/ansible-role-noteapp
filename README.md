# 🚀 DevOps Project 2: Deploy Note-Taking Website on AWS EC2 with Ansible Role

## 📖 Project Overview

Deploy a Flask-based note-taking web application on AWS EC2 instances using Ansible automation. This project demonstrates Infrastructure as Code (IaC) principles, configuration management, and role-based deployment strategies.

---

## 🎯 Objective

Set up and deploy a basic note-taking web application on an AWS EC2 instance using Python Flask, connect it to an SQLite database, and automate the deployment process using Ansible roles.

---

## 📋 Project Requirements

### Infrastructure Requirements
- **Cloud Platform**: AWS EC2
- **Operating System**: Amazon Linux 2023
- **Instance Type**: t2.micro (Free Tier)
- **Security Groups**: 
  - Port 22 (SSH)
  - Port 80 (HTTP)
- **Authentication**: SSH Key Pair

### Application Requirements
- **Language**: Python (Flask Framework)
- **Database**: SQLite
- **Features**: 
  - Simple interface for writing and submitting notes
  - Notes stored with timestamps
  - Display submitted notes below input form

---

## 🏗️ Architecture

```
┌─────────────────┐    SSH/Ansible    ┌─────────────────┐
│  Controller     │ ──────────────────▶│  Target EC2     │
│  (Amazon Linux) │                    │  (Amazon Linux) │
│  - Ansible      │                    │  - Flask App    │
│  - Python3      │                    │  - SQLite DB    │
│  - AWS CLI      │                    │  - Systemd      │
└─────────────────┘                    └─────────────────┘
```

---

## 🛠️ Step-by-Step Implementation

### Phase 1: Infrastructure Setup

#### 1️⃣ Create AWS EC2 Instances

Create two EC2 instances:
- **Controller Machine**: For running Ansible
- **Target Machine**: For hosting the note-taking application

**Instance Configuration:**
- AMI: Amazon Linux 2023
- Instance Type: t2.micro
- Security Group: Allow ports 22 (SSH) and 80 (HTTP)
- Key Pair: Create or use existing SSH key

#### 2️⃣ Connect to Controller Machine

```bash
# Connect via SSH
ssh -i your-key.pem ec2-user@controller-public-ip
```

#### 3️⃣ Install Prerequisites on Controller

```bash
# Update system
sudo dnf update -y

# Install Python and Ansible
sudo dnf install -y python3 pip git
pip3 install ansible boto3 botocore

# Verify installation
ansible --version
```

---

### Phase 2: Ansible Role Development

#### 4️⃣ Create Ansible Project Structure

```bash
# Create project directory
mkdir ansible-project
cd ansible-project

# Initialize Ansible Galaxy role
ansible-galaxy init noteapp
cd noteapp
```

#### 5️⃣ Configure Role Files

**Directory Structure:**
```
noteapp/
├── tasks/main.yml           # Main automation tasks
├── files/
│   ├── app.py              # Flask application
│   └── noteapp.service     # Systemd service
├── templates/
│   └── index.html          # HTML template
├── meta/main.yml           # Role metadata
└── README.md               # Documentation
```

**tasks/main.yml:**
```yaml
---
- name: Install required packages
  ansible.builtin.yum:
    name:
      - python3
      - sqlite
    state: present

- name: Install Flask
  ansible.builtin.pip:
    name: flask

- name: Create app directory
  ansible.builtin.file:
    path: /opt/noteapp
    state: directory
    owner: ec2-user
    group: ec2-user
    mode: '0755'

- name: Create templates directory
  ansible.builtin.file:
    path: /opt/noteapp/templates
    state: directory
    owner: ec2-user
    group: ec2-user
    mode: '0755'

- name: Upload application code
  ansible.builtin.copy:
    src: app.py
    dest: /opt/noteapp/app.py
    mode: '0755'

- name: Upload HTML template
  ansible.builtin.copy:
    src: index.html
    dest: /opt/noteapp/templates/index.html
    mode: '0644'

- name: Upload systemd service
  ansible.builtin.copy:
    src: noteapp.service
    dest: /etc/systemd/system/noteapp.service

- name: Reload systemd
  ansible.builtin.systemd:
    daemon_reload: true

- name: Enable and start the note-taking app service
  ansible.builtin.systemd:
    name: noteapp
    enabled: true
    state: started
```

**files/app.py:**
```python
from flask import Flask, request, render_template
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)
DB_PATH = '/opt/noteapp/notes.db'

# Database setup
if not os.path.exists(DB_PATH):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE notes (content TEXT, created_at TEXT)''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    if request.method == 'POST':
        note = request.form['note']
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        c.execute("INSERT INTO notes VALUES (?, ?)", (note, timestamp))
        conn.commit()
    
    c.execute("SELECT content, created_at FROM notes ORDER BY created_at DESC")
    notes = c.fetchall()
    conn.close()
    
    return render_template('index.html', notes=notes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
```

**files/noteapp.service:**
```ini
[Unit]
Description=Note Taking App
After=network.target

[Service]
ExecStart=/usr/bin/python3 /opt/noteapp/app.py
WorkingDirectory=/opt/noteapp
Restart=always
User=root

[Install]
WantedBy=multi-user.target
```

**templates/index.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Note App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f2f2f2;
        }
        h1 {
            color: #333;
        }
        form {
            margin-bottom: 20px;
        }
        textarea {
            width: 100%;
            height: 100px;
            margin-top: 10px;
        }
        button {
            margin-top: 10px;
            padding: 8px 16px;
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
        }
        .note {
            background: white;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 10px;
        }
        .timestamp {
            font-size: 12px;
            color: #666;
        }
    </style>
</head>
<body>
    <h1>📒 Your Notes</h1>
    <form method="POST">
        <label for="note">Write a new note:</label><br>
        <textarea name="note" required></textarea><br>
        <button type="submit">Add Note</button>
    </form>
    
    {% for note in notes %}
    <div class="note">
        <div class="timestamp">🕒 {{ note[1] }}</div>
        <div>{{ note[0] }}</div>
    </div>
    {% endfor %}
</body>
</html>
```

**meta/main.yml:**
```yaml
---
galaxy_info:
  role_name: noteapp
  author: salwatamer-max
  description: Deploys a simple Flask-based note-taking app
  license: MIT
  min_ansible_version: "2.15"
  platforms:
    - name: Amazon
      versions:
        - "2023"
dependencies: []
```

---

### Phase 3: Dynamic Inventory & Deployment

#### 6️⃣ Create AWS Dynamic Inventory

Create `aws_ec2.yaml` in the `ansible-project` directory:

```yaml
plugin: amazon.aws.aws_ec2
regions:
  - us-east-1
filters:
  tag:Environment: production
hostnames:
  - ip-address
compose:
  ansible_host: public_ip_address
```

#### 7️⃣ Create Deployment Playbook

Create `deploy.yml` in the `ansible-project` directory:

```yaml
---
- name: Deploy Flask Note App to EC2
  hosts: all
  become: true
  roles:
    - noteapp
```

#### 8️⃣ Run the Deployment

```bash
# Navigate to project directory
cd ansible-project

# Run the playbook
ansible-playbook -i aws_ec2.yaml deploy.yml
```

#### 9️⃣ Test the Application

Visit your application in the browser:
```
http://<your-ec2-instance-public-ip>/
```

---

### Phase 4: Version Control & Galaxy Publishing

#### 🔟 Push to GitHub

```bash
# Navigate to role directory
cd noteapp

# Configure Git (replace with your details)
git config --global user.name "salwatamer-max"
git config --global user.email "salwatamer8901@gmail.com"

# Initialize repository
git init
git remote add origin https://github.com/salwatamer-max/ansible-role-noteapp.git

# Commit and push
git add .
git commit -m "Initial commit of noteapp Ansible role"
git push -u origin main --force
```

#### 1️⃣1️⃣ Publish to Ansible Galaxy

```bash
# Install role locally first (optional)
ansible-galaxy install salwatamer-max.noteapp

# Get Galaxy token from https://galaxy.ansible.com/
export GALAXY_TOKEN=your_galaxy_token_here

# Import role to Galaxy
ansible-galaxy role import --token=$GALAXY_TOKEN salwatamer-max ansible-role-noteapp
```

---

## 📸 Application Screenshot

Here's what the deployed note-taking application looks like:

<div align="center">
  <img width="80%" alt="NoteApp Interface - Flask Note-Taking Application" src="https://github.com/user-attachments/assets/22faa03b-c9e1-49a3-8230-3fa4c432e517" />
  
  *The note-taking application interface showing the text input area and previously submitted notes with timestamps*
</div>

### 🎨 Application Features Shown:

- **Clean, Responsive Interface** - Simple and user-friendly design
- **Note Input Form** - Large text area for writing notes
- **Timestamp Display** - Each note shows when it was created
- **Chronological Order** - Notes displayed with newest first
- **Professional Styling** - Clean CSS with proper spacing and colors

---

## 🔗 Links & Resources

- **GitHub Repository**: [https://github.com/salwatamer-max/ansible-role-noteapp](https://github.com/salwatamer-max/ansible-role-noteapp)
- **Ansible Galaxy Role**: [https://galaxy.ansible.com/ui/standalone/roles/salwatamer-max/noteapp/](https://galaxy.ansible.com/ui/standalone/roles/salwatamer-max/noteapp/)

---

## 📦 Installation & Usage

### Install from Ansible Galaxy

```bash
ansible-galaxy install salwatamer-max.noteapp
```

### Use in Playbook

```yaml
---
- hosts: webservers
  become: true
  roles:
    - salwatamer-max.noteapp
```

---

## 🧪 Testing

### Local Testing

```bash
# Test locally
ansible-playbook -i localhost, -c local deploy.yml
```

### Validation Commands

```bash
# Check service status
sudo systemctl status noteapp

# Check application logs
journalctl -u noteapp -f

# Test HTTP response
curl http://localhost/
```

---

## 🔧 Troubleshooting

### Common Issues

1. **Port 80 Access Denied**
   - Ensure the service runs as root in systemd
   - Check security group allows port 80

2. **SQLite Database Permissions**
   - Verify `/opt/noteapp` directory permissions
   - Ensure proper ownership for database file

3. **Flask Dependencies**
   - Verify Flask installation: `pip3 show flask`
   - Check Python path in systemd service

---

## 📈 Future Enhancements

- [ ] Add SSL/HTTPS support
- [ ] Implement user authentication
- [ ] Add database backup strategy
- [ ] Integrate with AWS RDS
- [ ] Add monitoring and logging
- [ ] Implement CI/CD pipeline

---

## 👥 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👤 Author

**Salwa Tamer**
- GitHub: [@salwatamer-max](https://github.com/salwatamer-max)
- Email: salwatamer8901@gmail.com

---

*🌟 If this project helped you, please give it a star on GitHub!*



