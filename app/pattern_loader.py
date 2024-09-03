import os

def __load_patterns():
        base_directory = 'patterns'
        directories = [os.path.join(base_directory, d) for d in os.listdir(base_directory) if os.path.isdir(os.path.join(base_directory, d))]
        patterns = {}
        for directory in directories:
            label = os.path.basename(directory)
            content = {}
            system_path = os.path.join(directory, 'system.md')
            user_path = os.path.join(directory, 'user.md')

            if os.path.exists(system_path):
                with open(system_path, 'r') as file:
                    content['system'] = file.read()

            if os.path.exists(user_path):
                with open(user_path, 'r') as file:
                    content['user'] = file.read()

            patterns[label] = content

        return patterns

patterns = __load_patterns()

# for label, content in patterns.items():
#      print(label)
#      print(content.get('system'))
#      print(type(content))