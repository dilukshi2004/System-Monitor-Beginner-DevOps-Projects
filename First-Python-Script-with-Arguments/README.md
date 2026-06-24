#  DevOps CLI Tool — AWS Resource Manager

A professional command-line interface (CLI) tool built with Python that allows you to interactively manage and inspect your AWS resources directly from the terminal. Built as part of a DevOps internship learning journey at SLT Mobitel.

---

##  What It Does

- ✅ Lists all **EC2 instances** with Instance ID, state, and instance type
- ✅ Lists all **S3 buckets** in your AWS account
- ✅ Lists all **IAM users** with creation dates
- ✅ Lists **all resources at once** with a single command
- ✅ Provides a **help menu** with usage instructions
- ✅ Accepts **command line arguments** for full user control

---

##  Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3 | Core programming language |
| Boto3 | Official AWS SDK for Python |
| Argparse | Python built-in CLI argument parser |
| AWS EC2 | Cloud virtual machines |
| AWS S3 | Cloud object storage |
| AWS IAM | Identity and access management |
| AWS CLI | Credential configuration |

---

##  Prerequisites

Before running this tool, make sure you have:

- Python 3 installed
- AWS CLI installed and configured
- Boto3 installed
- An AWS account with EC2, S3, and IAM access

---
##  Setup & Installation

**Step 1 — Clone the repository:**
```bash
git clone https://github.com/dilukshi2004/System-Monitor-Beginner-DevOps-Projects.git
cd System-Monitor-Beginner-DevOps-Projects
cd First-Python-Script-with-Arguments
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

**Step 4 — Make the script executable:**
```bash
chmod +x devops_tool.py
```

---

##  Usage

**See the help menu:**
```bash
python3 devops_tool.py --help
```

**List EC2 instances only:**
```bash
python3 devops_tool.py --action ec2
```

**List S3 buckets only:**
```bash
python3 devops_tool.py --action s3
```

**List IAM users only:**
```bash
python3 devops_tool.py --action iam
```

**List all resources at once:**
```bash
python3 devops_tool.py --action all
```

---

##  Sample Output

```
==============================
   DevOps CLI Tool
   Author: Dilukshi Warangana
==============================

============================
       EC2 Instances
============================
ID     : i-0abc12345def67890
State  : running
Type   : t2.micro
----------------------------
ID     : i-0xyz98765abc43210
State  : stopped
Type   : t3.medium
----------------------------

============================
        S3 Buckets
============================
Bucket : dilukshi-test-bucket-2026
----------------------------

============================
        IAM Users
============================
User   : dilukshi-admin
Created: 2026-06-06 17:55:16+00:00
----------------------------
```

---

##  How It Works

```
--action ec2   →  calls list_ec2()   →  boto3 describe_instances()
--action s3    →  calls list_s3()    →  boto3 list_buckets()
--action iam   →  calls list_iam()   →  boto3 list_users()
--action all   →  calls list_all()   →  runs all three functions
```

**Argparse flow:**
```
user types --action ec2
     ↓
argparse reads the argument
     ↓
validates it is one of [ec2, s3, iam, all]
     ↓
passes it to the if/elif block
     ↓
calls the correct function
```

---

## Project Structure

```
First-Python-Script-with-Arguments/
│
├── devops_tool.py     # Main CLI Python script
└── README.md          # Project documentation
```

---

## Difference From Stage 1

| Feature | Stage 1 (aws_check.py) | Stage 2 (devops_tool.py) |
|---------|----------------------|--------------------------|
| User control | ❌ None | ✅ Full control |
| Arguments | ❌ No arguments | ✅ --action flag |
| Help menu | ❌ No | ✅ Yes |
| Resources | EC2 + S3 only | EC2 + S3 + IAM |
| Feel | Basic script | Professional CLI tool |

---

##  Security Note

- Never hardcode your AWS credentials in the script
- Always use `aws configure` to store credentials securely
- Never commit your credentials to GitHub
- Use IAM users with least privilege instead of root account credentials
- Run `chmod 600 ~/.aws/credentials` to restrict access to your credentials file

---

##  What I Learned

- Building professional CLI tools using Python `argparse`
- Connecting to multiple AWS services using Boto3
- Structuring Python code with functions for reusability
- Handling empty AWS responses gracefully
- Using `if __name__ == "__main__"` Python best practice
- Securing AWS credentials properly

---

##  Future Improvements

- [ ] Add `--region` flag to specify AWS region
- [ ] Add `--output` flag for JSON/CSV export
- [ ] Add Lambda function listing
- [ ] Add error handling for expired credentials
- [ ] Add color-coded output using `colorama`
- [ ] Dockerize the CLI tool
- [ ] Add GitHub Actions CI/CD pipeline

---

##  Author

**Dilukshi Warangana**
Computer Science Undergraduate — IIT (University of Westminster)
DevOps Intern @ SLT Mobitel

[![GitHub](https://img.shields.io/badge/GitHub-dilukshi2004-black?logo=github)](https://github.com/dilukshi2004)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Dilukshi%20Warangana-blue?logo=linkedin)](https://linkedin.com/in/dilukshi-warangana)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).