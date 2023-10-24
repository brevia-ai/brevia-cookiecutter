ADD_GITIGNORE_PATHS = [
    '.env',
    'test_service.yml',
]

with open('.gitignore', 'a') as f:
    for item in ADD_GITIGNORE_PATHS:
        print(f'Adding {item} to .gitignore')
        f.write(f'{item}\n')
