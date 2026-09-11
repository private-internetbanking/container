import os
import glob

folder = os.getcwd()
files = glob.glob(os.path.join(folder, '*.html'))

mapping = {
    '../containers.html/20ft container.jpg': '20ft container.jpg',
    '../containers.html/40ft container.jpg': '40ft container.jpg',
    '../containers.html/20ft high cube.jpg': '20ft high cube.jpg',
    '../containers.html/40ft high cube.jpg': '40ft high cube.jpg',
    '../containers.html/40ft reefer containers.jpg': '40ft reefer containers.jpg',
    '../containers.html/20ft open sided container.jpg': '20ft open sided container.jpg',
    '../containers.html/20ft office unit.jpg': '20ft office unit.jpg',
}

remote_mapping = {
    'https://images.unsplash.com/photo-1586528116493-da8b5f7c4e85?auto=format&fit=crop&w=1400&q=90': '20ft container.jpg',
    'https://images.unsplash.com/photo-1601584115197-04ecc0da31d8?auto=format&fit=crop&w=1100&q=90': '40ft container.jpg',
    'https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&w=900&q=90': '20ft container.jpg',
    'https://images.unsplash.com/photo-1565891741441-64926e441838?auto=format&fit=crop&w=900&q=90': '40ft high cube.jpg',
    'https://images.unsplash.com/photo-1590496793929-36417d3117de?auto=format&fit=crop&w=900&q=90': '20ft office unit.jpg',
}

for file_path in files:
    original = open(file_path, encoding='utf-8', errors='replace').read()
    updated = original
    for src, dst in mapping.items():
        updated = updated.replace(src, dst)
    for src, dst in remote_mapping.items():
        updated = updated.replace(src, dst)
    if updated != original:
        open(file_path, 'w', encoding='utf-8').write(updated)

print(f'Fixed {len(files)} HTML files in {folder}')
