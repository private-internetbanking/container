import os
import glob

folder = os.getcwd()
html_files = glob.glob(os.path.join(folder, '*.html'))

# Map the older local screenshot-on-site image file names to curated premium remote image URLs.
local_to_remote = {
    '../containers.html/20ft container.jpg': 'https://images.unsplash.com/photo-1518005020951-ecc8930a6e0d?auto=format&fit=crop&w=1200&q=90',
    '../containers.html/40ft container.jpg': 'https://images.unsplash.com/photo-1600566752355-35792bedcfea?auto=format&fit=crop&w=1200&q=90',
    '../containers.html/20ft high cube.jpg': 'https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?auto=format&fit=crop&w=1200&q=90',
    '../containers.html/40ft high cube.jpg': 'https://images.unsplash.com/photo-1600566753376-12c8ab7fb75b?auto=format&fit=crop&w=1200&q=90',
    '../containers.html/40ft reefer containers.jpg': 'https://images.unsplash.com/photo-1494526585095-c41746248156?auto=format&fit=crop&w=1200&q=90',
    '../containers.html/20ft open sided container.jpg': 'https://images.unsplash.com/photo-1501785888041-af3ef285b470?auto=format&fit=crop&w=1200&q=90',
    '../containers.html/20ft office unit.jpg': 'https://images.unsplash.com/photo-1600566752355-35792bedcfea?auto=format&fit=crop&w=1200&q=90',
}

# Also map the stored default product image values in the admin inventory and product JS blocks.
product_image_swap = {
    'https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&w=900&q=90': 'https://images.unsplash.com/photo-1518005020951-ecc8930a6e0d?auto=format&fit=crop&w=1200&q=90',
    'https://images.unsplash.com/photo-1565891741441-64926e441838?auto=format&fit=crop&w=900&q=90': 'https://images.unsplash.com/photo-1600566753376-12c8ab7fb75b?auto=format&fit=crop&w=1200&q=90',
    'https://images.unsplash.com/photo-1590496793929-36417d3117de?auto=format&fit=crop&w=900&q=90': 'https://images.unsplash.com/photo-1600566752355-35792bedcfea?auto=format&fit=crop&w=1200&q=90',
}

# The homepage and editorial art also need a classic premium look.
page_image_swap = {
    'https://images.unsplash.com/photo-1586528116493-da8b5f7c4e85?auto=format&fit=crop&w=1400&q=90': 'https://images.unsplash.com/photo-1600566752355-35792bedcfea?auto=format&fit=crop&w=1600&q=90',
    'https://images.unsplash.com/photo-1601584115197-04ecc0da31d8?auto=format&fit=crop&w=1100&q=90': 'https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?auto=format&fit=crop&w=1600&q=90',
}

# Replace in each page.
for file_path in html_files:
    original = open(file_path, encoding='utf-8', errors='replace').read()
    updated = original
    for old_value, new_value in local_to_remote.items():
        updated = updated.replace(old_value, new_value)
    for old_value, new_value in product_image_swap.items():
        updated = updated.replace(old_value, new_value)
    for old_value, new_value in page_image_swap.items():
        updated = updated.replace(old_value, new_value)
    if updated != original:
        open(file_path, 'w', encoding='utf-8').write(updated)

print(f'Updated {len(html_files)} HTML files in {folder}')
