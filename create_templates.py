from PIL import Image, ImageDraw, ImageFont

# Define the font names and corresponding font paths
font_names = ['HighwayGothic', 'Clearview',
              'Eurostile', 'Frutiger']
font_names = ['HighwayGothic', 'Clearview',
              'Frutiger', 'Eurostile', 'SourceSansPro-Bold',
              'SourceSansPro-Italic',
              'Roboto-Bold', 'Roboto-Italic']
font_paths = ['./fonts/HighwayGothic.ttf', './fonts/Clearview.ttf',
              './fonts/Frutiger.ttf', './fonts/Eurostile.ttf', './fonts/SourceSansPro-Bold.ttf',
              './fonts/SourceSansPro-Italic.ttf',
              './fonts/Roboto-Bold.ttf', './fonts/Roboto-Italic.ttf']

# Create a blank canvas for drawing digits
canvas = Image.new('RGB', (32, 32), color='white')
draw = ImageDraw.Draw(canvas)

# Iterate over each font
for font_name, font_path in zip(font_names, font_paths):
    print(font_path)
    font = ImageFont.truetype(font_path, size=28)  # Adjust size as needed

    # Iterate over each digit (0-9)
    for digit in range(10):
        digit_image = canvas.copy()

        # Draw the digit using the specified font
        draw = ImageDraw.Draw(digit_image)
        digit_width, digit_height = draw.textsize(str(digit), font=font)
        position = ((32 - digit_width) // 2, (32 - digit_height) // 2)
        draw.text(position, str(digit), fill='black', font=font)

        # Save the digit image
        save_path = f'./templates/{font_name}_{digit}.png'
        digit_image.save(save_path)
        print(f'Saved image: {save_path}')
