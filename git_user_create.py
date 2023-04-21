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

# 遍历所有账户，创建账户
for account in accounts:
    name = account['name']
    email = account['email']

    # 创建账户
    os.system(f"git config --global user.name '{name}'")
    os.system(f"git config --global user.email '{email}'")

    # 显示创建结果
    print(f"Created Git account: {name} <{email}>")
