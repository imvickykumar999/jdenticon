import hashlib
from PIL import Image, ImageDraw

def generate_identicon(username, size=250, grid_size=5):
    # Step 1: Hash the username
    hash = hashlib.md5(username.encode('utf-8')).hexdigest()
    
    # Step 2: Determine the color
    color = tuple(int(hash[i:i+2], 16) for i in (0, 2, 4))
    
    # Step 3: Create the grid
    grid = []
    for i in range(0, 15, 3):
        grid.append([int(hash[i:i+1], 16) % 2, int(hash[i+1:i+2], 16) % 2, int(hash[i+2:i+3], 16) % 2])
    # Mirror the grid to ensure symmetry
    grid = [row + row[::-1] for row in grid]
    
    # Step 4: Draw the identicon
    img = Image.new('RGB', (grid_size*size//5, grid_size*size//5), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    for y in range(grid_size):
        for x in range(grid_size):
            if grid[y][x]:
                draw.rectangle(
                    [x*size//5, y*size//5, (x+1)*size//5, (y+1)*size//5],
                    fill=color
                )
    
    img = img.resize((size, size), Image.NEAREST)
    img.show()

# Example usage
generate_identicon("username")
