import os

# 创建8个Git账户
accounts = [
    {
        'name': 'user1',
        'email': 'user1@example.com'
    },
    {
        'name': 'user2',
        'email': 'user2@example.com'
    },
    {
        'name': 'user3',
        'email': 'user3@example.com'
    },
    {
        'name': 'user4',
        'email': 'user4@example.com'
    },
    {
        'name': 'user5',
        'email': 'user5@example.com'
    },
    {
        'name': 'user6',
        'email': 'user6@example.com'
    },
    {
        'name': 'user7',
        'email': 'user7@example.com'
    },
    {
        'name': 'user8',
        'email': 'user8@example.com'
    }
]

# 遍历所有账户，创建密钥
for account in accounts:
    name = account['name']
    email = account['email']
    pub_key_name = f"id_rsa_{name.replace(' ', '_')}.pub"
    key_path = f"C:/Users/{os.getlogin()}/.ssh/id_rsa_{name}"

    # 创建密钥
    os.system(f'ssh-keygen -m PEM -t rsa -b 4096 -C {email} -f {key_path} -N "" -P ""')
    # 添加密钥到ssh-agent
    os.system(f"start-ssh-agent.cmd > $null; ssh-add {key_path}")

    # 显示创建结果
    print(f"Created SSH key for account: {name} <{email}>")
    print(f"Public key filename: {pub_key_name}")
