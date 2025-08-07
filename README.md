# 📦 Ansible Role: noteapp

This Ansible role deploys a simple **Flask-based note-taking web application** on a target Linux host (Amazon Linux 2023 or similar). The app runs on **port 80** and uses **SQLite** as the backend.

---

## 📁 Features

- Installs required packages (Python, Flask, SQLite)
- Deploys a basic Flask web app (`app.py`, `index.html`)
- Initializes an SQLite database
- Sets up a `systemd` service to run the app on boot
- Listens on `http://<server-ip>:80`

---

## 🧾 Role Directory Structure

noteapp/
├── tasks/
│ └── main.yml
├── files/
│ ├── app.py
│ └── noteapp.service
├── templates/
│ └── index.html
├── meta/
│ └── main.yml

yaml
Copy
Edit

---

## ✅ Step-by-Step Setup

### 1️⃣ Create AWS EC2 Instances

- One EC2 instance for the **Ansible controller**
- One EC2 instance as the **managed host** (where the app will run)

### 2️⃣ Install Prerequisites on the Controller

```bash
sudo dnf install -y python3 pip
pip3 install ansible boto3 botocore
ansible --version
🛠️ Create and Configure the Role
3️⃣ Create the Role
bash
Copy
Edit
cd ansible-project
ansible-galaxy init noteapp
cd noteapp
4️⃣ Add Your Files
Populate these with your code:

tasks/main.yml

files/app.py

files/noteapp.service

templates/index.html

meta/main.yml (for Galaxy metadata)

🚀 Usage Example
5️⃣ Create Dynamic Inventory File
Make sure aws_ec2.yaml is in your project root and correctly configured.

6️⃣ Create the Playbook deploy.yml
Create this in the ansible-project/ root:

yaml
Copy
Edit
- name: Deploy note-taking app
  hosts: all
  become: true
  roles:
    - salwatamer-max.noteapp
7️⃣ Run the Playbook
bash
Copy
Edit
ansible-playbook -i aws_ec2.yaml deploy.yml
🌐 Accessing the App
Once deployed, visit the app in your browser:

cpp
Copy
Edit
http://<public-ec2-ip>
✅ Ensure port 80 is open in your EC2 instance’s security group!

🖼️ Screenshot
<img width="100%" alt="Screenshot (NoteApp)" src="https://github.com/user-attachments/assets/22faa03b-c9e1-49a3-8230-3fa4c432e517" />
🔧 Requirements
Ansible 2.10+

Python 3.x

Amazon Linux or compatible system

Open ports in firewall/security groups

📥 Installation via Galaxy
Once published:

bash
Copy
Edit
ansible-galaxy install salwatamer-max.noteapp
🙋‍♀️ Author
Salwa Tamer

GitHub: salwatamer-max



