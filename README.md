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
Copy
Edit
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

bash
Copy
Edit
ansible-galaxy install salwatamer-max.noteapp
🌐 Accessing the App
After deployment, visit:

cpp
Copy
Edit
http://<your-server-ip>/
You should see the Note Taking App UI.

📝 License
MIT

🙋‍♂️ Author
Salwa Tamer
GitHub: salwatamer-maxRole Name
=========

A brief description of the role goes here.

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
