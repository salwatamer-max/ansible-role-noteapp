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

```
noteapp/
├── tasks/
│   └── main.yml
├── files/
│   ├── app.py
│   └── noteapp.service
├── templates/
│   └── index.html
├── meta/
│   └── main.yml
└── README.md
```

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
```

### 3️⃣ Create and Configure the Role

```bash
cd ansible-project
ansible-galaxy init noteapp
cd noteapp
```

### 4️⃣ Add Your Files

Populate these with your code:
- `tasks/main.yml`
- `files/app.py`
- `files/noteapp.service`
- `templates/index.html`
- `meta/main.yml` (for Galaxy metadata)

---

## 🚀 Usage Example

### 5️⃣ Create Dynamic Inventory File
Make sure `aws_ec2.yaml` is in your project root and correctly configured.

### 6️⃣ Create the Playbook `deploy.yml`
Create this in the `ansible-project/` root:

```yaml
---
- name: Deploy note-taking app
  hosts: all
  become: true
  roles:
    - salwatamer-max.noteapp
```

### 7️⃣ Run the Playbook

```bash
ansible-playbook -i aws_ec2.yaml deploy.yml
```

---

## 🌐 Accessing the App

Once deployed, visit the app in your browser:

```
http://<public-ec2-ip>
```

✅ **Ensure port 80 is open in your EC2 instance's security group!**

---

## 🖼️ Screenshot

<img width="100%" alt="Screenshot (NoteApp)" src="https://github.com/user-attachments/assets/22faa03b-c9e1-49a3-8230-3fa4c432e517" />

---

## 🔧 Requirements

- Ansible 2.10+
- Python 3.x
- Amazon Linux or compatible system
- Open ports in firewall/security groups

---

## 📥 Installation via Galaxy

Once published:

```bash
ansible-galaxy install salwatamer-max.noteapp
```

Or add to your `requirements.yml`:

```yaml
---
- name: salwatamer-max.noteapp
  version: ">=1.0.0"
```

Then install:

```bash
ansible-galaxy install -r requirements.yml
```

---

## 📚 Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `app_port` | `80` | Port for the Flask application |
| `app_user` | `noteapp` | System user to run the application |
| `app_dir` | `/opt/noteapp` | Directory where the app is installed |

Example usage in playbook:

```yaml
---
- hosts: webservers
  become: true
  roles:
    - role: salwatamer-max.noteapp
      vars:
        app_port: 8080
        app_user: webapp
```

---

## 🧪 Testing

Test the role locally:

```bash
# Install the role
ansible-galaxy install salwatamer-max.noteapp

# Create a test playbook
cat > test.yml << EOF
---
- hosts: localhost
  become: true
  roles:
    - salwatamer-max.noteapp
EOF

# Run the test
ansible-playbook test.yml
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙋‍♀️ Author

**Salwa Tamer**
- GitHub: [@salwatamer-max](https://github.com/salwatamer-max)
- Ansible Galaxy: [salwatamer-max.noteapp](https://galaxy.ansible.com/salwatamer-max/noteapp)

---

## 🔗 Links

- [Ansible Galaxy Role](https://galaxy.ansible.com/salwatamer-max/noteapp)
- [GitHub Repository](https://github.com/salwatamer-max/ansible-role-noteapp)
- [Ansible Documentation](https://docs.ansible.com/)

---

*⭐ If this role helped you, please consider giving it a star on GitHub!*
