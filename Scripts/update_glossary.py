import re

def update_glossary(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Split content into sections
    sections = re.split(r'\n##\s+', content)
    header = sections.pop(0)  # Remove and store the header

    # Sort sections
    sections.sort(key=lambda s: s.strip()[0].upper())

    # Rejoin content
    sorted_content = header + '## ' + '\n## '.join(sections)

    # Write back to file
    with open(file_path, 'w') as file:
        file.write(sorted_content)

update_glossary('../Resources/PKI_Glossary.md')
print("Glossary updated and sorted.")