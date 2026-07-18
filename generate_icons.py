from PIL import Image, ImageDraw

def create_icon(size, filename):
    img = Image.new('RGBA', (size, size), color=(5, 150, 105, 255)) # Emerald 600
    d = ImageDraw.Draw(img)
    # Just a simple text 'F'
    # We won't use a custom font to avoid Missing Font errors, just raw shapes or text
    # Let's just draw a simple plant-like shape (a circle with a leaf)
    d.ellipse([(size*0.2, size*0.2), (size*0.8, size*0.8)], fill=(255, 255, 255, 255))
    img.save(filename)

create_icon(192, 'public/pwa-192x192.png')
create_icon(512, 'public/pwa-512x512.png')
create_icon(180, 'public/apple-touch-icon.png')
