To better match the original identicon, we need to ensure the algorithm generates the correct symmetrical pattern. Here's the updated algorithm with adjustments for generating an identicon:

```python
import hashlib
from PIL import Image, ImageDraw

def generate_identicon(username, size=250, grid_size=5, save_path="identicon.png"):
    # Step 1: Hash the username
    hash = hashlib.md5(username.encode('utf-8')).hexdigest()
    
    # Step 2: Determine the color
    color = tuple(int(hash[i:i+2], 16) for i in (0, 2, 4))
    
    # Step 3: Create the grid
    grid = []
    for i in range(0, 15, 3):
        grid.append([int(hash[i:i+1], 16) % 2, int(hash[i+1:i+2], 16) % 2, int(hash[i+2:i+3], 16) % 2])
    # Mirror the grid to ensure symmetry
    for row in grid:
        row.extend(row[:-1][::-1])
    
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
    img.save(save_path)
    print(f"Identicon saved to {save_path}")

# Example usage
generate_identicon("username", save_path="username_identicon.png")
```

### Explanation

1. **Hash the Input**: The `hashlib.md5` function creates a hash from the username.
2. **Determine Colors**: Extract the first three bytes of the hash for the RGB color.
3. **Create a Grid**: The grid is determined by the next few bytes of the hash.
4. **Draw the Identicon**: Use the Pillow library to draw the identicon based on the grid and color.
5. **Save the Image**: The `img.save(save_path)` function saves the generated identicon to the specified file path.

This code will generate and save the identicon image as "username_identicon.png". Adjust the `save_path` parameter as needed to save the image to a different file or location.

Here’s a visualization of how the identicon is constructed:
- Each cell in the grid is determined by a portion of the hash.
- The grid is mirrored to ensure symmetry.
- The identicon is drawn based on the grid pattern and the color derived from the hash.
