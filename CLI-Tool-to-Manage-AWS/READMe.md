# 🌩️ AWS Resource Checker

A beginner-friendly Python script that connects to your AWS account and lists all **EC2 instances** and **S3 buckets** using the **Boto3 SDK**. Built as part of a DevOps internship learning journey.

---

## 📌 What It Does

- ✅ Lists all **EC2 instances** with their Instance ID and current state (running/stopped)
- ✅ Lists all **S3 buckets** in your AWS account
- ✅ Connects to AWS programmatically using Python — no AWS Console needed!

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3 | Core programming language |
| Boto3 | Official AWS SDK for Python |
| AWS EC2 | Cloud virtual machines |
| AWS S3 | Cloud object storage |
| AWS CLI | Credential configuration |

---

## 📋 Prerequisites

Before running this script, make sure you have:

- Python 3 installed
- AWS CLI installed and configured
- An AWS account with EC2 and S3 access

---

## ⚙️ Setup & Installation

**Step 1 — Clone the repository:**
```bash
https://github.com/dilukshi2004/System-Monitor-Beginner-DevOps-Projects.git
cd System-Monitor-Beginner-DevOps-Projects
cd CLI-Tool-to-Manage-AWS
```

**Step 2 — Install dependencies:**
```bash
pip3 install boto3
```

**Step 3 — Configure AWS credentials:**
```bash
aws configure
```
You will be prompted to enter:
- AWS Access Key ID
- AWS Secret Access Key
- Default region (e.g. `us-east-1`)
- Default output format (e.g. `json`)

---

## 🚀 Usage

Run the script:
```bash
python3 aws_check.py
```

---

## 📤 Sample Output

```
=== EC2 Instances ===
ID: i-0abc12345def67890 | State: running
ID: i-0xyz98765abc43210 | State: stopped

=== S3 Buckets ===
Bucket: dilukshi-test-bucket-2026
Bucket: my-project-assets
```

If no resources exist, the sections will appear empty — which means the script is working correctly and your AWS account simply has no resources yet!

---

## 🧠 How It Works

```
aws configure          →  saves your credentials locally
boto3.client('ec2')    →  connects to AWS EC2 service
describe_instances()   →  fetches all EC2 instance data
boto3.client('s3')     →  connects to AWS S3 service
list_buckets()         →  fetches all S3 bucket names
```

The script uses **Boto3** — the official Amazon Web Services SDK for Python — to make API calls to your AWS account and retrieve resource information programmatically.

---

## 📁 Project Structure

```
aws-resource-checker/
│
├── aws_check.py       # Main Python script
└── README.md          # Project documentation
```

---

## 🔐 Security Note

- Never hardcode your AWS credentials in the script
- Always use `aws configure` to store credentials securely
- Never commit your credentials to GitHub
- Use IAM users with least privilege instead of root account credentials

---

## 🌱 What I Learned

- Connecting to AWS programmatically using Python and Boto3
- Working with AWS EC2 and S3 APIs
- Iterating through nested JSON responses from AWS
- Using f-strings for formatted output in Python
- Securing AWS credentials using AWS CLI

---

## 🔮 Future Improvements

- [ ] Add support for listing IAM users
- [ ] Add support for listing Lambda functions
- [ ] Add argparse for CLI argument support
- [ ] Add error handling for missing credentials
- [ ] Dockerize the script

---

## 👩‍💻 Author

**Dilukshi Warangana**
Computer Science Undergraduate — IIT (University of Westminster)
DevOps Intern @ SLT Mobitel

[![GitHub](https://img.shields.io/badge/GitHub-dilukshi2004-black?logo=github)](https://github.com/dilukshi2004)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Dilukshi%20Warangana-blue?logo=linkedin)](https://linkedin.com/in/dilukshi-warangana)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).