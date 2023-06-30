from PIL import Image
import colorsys

def create_color_palette(image_path, palette_size=50):
    image = Image.open(image_path)
    image.thumbnail((200, 200))
    image = image.convert('RGB')

    colors = image.getcolors(image.size[0] * image.size[1])
  
    sorted_colors = sorted(colors, key=lambda x: x[0], reverse=True)

    unique_colors = []
    for count, color in sorted_colors:
        hex_color = f"#{''.join(f'{c:02x}' for c in color)}" # type: ignore
        if hex_color not in unique_colors:
            unique_colors.append(hex_color)
        if len(unique_colors) == palette_size:
            break

    print(f"Color Palette ({len(unique_colors)} colors):")
    for hex_color in unique_colors:
        print(hex_color)

    # Display the color palette as an image
    palette_image = Image.new('RGB', (len(unique_colors) * 100, 100))
    for i, hex_color in enumerate(unique_colors):
        r, g, b = colorsys.rgb_to_hsv(int(hex_color[1:3], 16) / 255, int(hex_color[3:5], 16) / 255, int(hex_color[5:7], 16) / 255)
        r, g, b = colorsys.hsv_to_rgb(r, 1.0, 1.0)
        r, g, b = int(r * 255), int(g * 255), int(b * 255)
        palette_image.paste((r, g, b), (i * 100, 0, (i + 1) * 100, 100))

    palette_image.show()
image_path = 'YOUR IMAGE PATH'
create_color_palette(image_path)
