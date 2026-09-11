import os
import glob

folder = os.getcwd()
html_files = glob.glob(os.path.join(folder, '*.html'))

curated_urls = {
    'hero': 'https://images.unsplash.com/photo-1600566752355-35792bedcfea?auto=format&fit=crop&w=1800&q=90',
    'editorial': 'https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?auto=format&fit=crop&w=1500&q=90',
    'collection_card': 'https://images.unsplash.com/photo-1600566753376-12c8ab7fb75b?auto=format&fit=crop&w=1100&q=90',
    'product_detail': 'https://images.unsplash.com/photo-1600566752355-35792bedcfea?auto=format&fit=crop&w=1000&q=90',
    'premium_architecture': 'https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?auto=format&fit=crop&w=1500&q=90',
}

# Keep all stock images on the same premium editorial direction.
photo_map = {
    'https://images.unsplash.com/photo-1586528116493-da8b5f7c4e85?auto=format&fit=crop&w=1400&q=90': curated_urls['hero'],
    'https://images.unsplash.com/photo-1601584115197-04ecc0da31d8?auto=format&fit=crop&w=1100&q=90': curated_urls['editorial'],
    'https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&w=900&q=90': curated_urls['collection_card'],
    'https://images.unsplash.com/photo-1565891741441-64926e441838?auto=format&fit=crop&w=900&q=90': curated_urls['collection_card'],
    'https://images.unsplash.com/photo-1590496793929-36417d3117de?auto=format&fit=crop&w=900&q=90': curated_urls['product_detail'],
}

# Also normalize any earlier local image file names still listed in embedded product scripts.
legacy_local_map = {
    '20ft container.jpg': curated_urls['collection_card'],
    '40ft container.jpg': curated_urls['collection_card'],
    '20ft high cube.jpg': curated_urls['collection_card'],
    '40ft high cube.jpg': curated_urls['collection_card'],
    '40ft reefer containers.jpg': curated_urls['premium_architecture'],
    '20ft open sided container.jpg': curated_urls['premium_architecture'],
    '20ft office unit.jpg': curated_urls['product_detail'],
}

for file_path in html_files:
    original = open(file_path, encoding='utf-8', errors='replace').read()
    updated = original
    for old_value, new_value in photo_map.items():
        updated = updated.replace(old_value, new_value)
    for old_value, new_value in legacy_local_map.items():
        updated = updated.replace(old_value, new_value)
    if updated != original:
        open(file_path, 'w', encoding='utf-8').write(updated)

print(f'Applied branded premium editorial image set to {len(html_files)} HTML files in {folder}')
