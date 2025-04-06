# imagecli/cli.py

import click
from imagecli.image import ImageCli, ImageSize

@click.group()
def main():
    """ImageCLI: A tool for image processing through CLI and Python package.""" 
    pass

@main.command()
@click.option('-f', '--file', required=True, type=click.Path(exists=True))
def size(file):
    """Show the size of the image."""
    size: ImageSize = ImageCli(file).size
    click.echo(f"Image Pixels Size: {size.width}x{size.height}")


@main.command()
@click.option('-f', '--file', required=True, type=click.Path(exists=True))
@click.option('-u', '--unit', default='bytes', type=click.Choice(['bytes', 'KB', 'MB', 'GB'], case_sensitive=False))
def file_size(file, unit):
    """Show the size of the file."""
    image_cli = ImageCli(file)
    formatted_size = image_cli.get_formatted_size(unit)
    click.echo(f"Image File Size: {formatted_size}")


@main.command()
@click.option('-f', '--file', required=True, type=click.Path(exists=True), help='Path to the image file.')
@click.option('-t', '--target_size', required=True, type=float, help='Target size for the compressed image.')
@click.option('-u', '--unit', default='MB', type=click.Choice(['bytes', 'KB', 'MB', 'GB'], case_sensitive=False), help='Unit for target size. Default is MB.')
def compress(file, target_size, unit):
    """Compress the image to a target file size."""
    image_cli = ImageCli(file)
    compressed_image_path = image_cli.compress_image(target_size=target_size, unit=unit)
    click.echo(f"Compressed image saved to: {compressed_image_path}")
    compressed_size = ImageCli(compressed_image_path).get_formatted_size(unit)
    click.echo(f"Compressed Image Size: {compressed_size}")

@main.command()
@click.option('-f', '--file', required=True, type=click.Path(exists=True), help='Path to the image file.')
@click.option('-c', '--color', default='BLUE', type=click.Choice(['BLUE', 'WHITE', 'RED'], case_sensitive=False), help='Background color to change to. Default is BLUE.')
def background(file, color):
    """Modify the image background color."""""
    image_cli = ImageCli(file)
    modified_image_path = image_cli.change_photo_backgroundcolor(color)
    click.echo(f"Modified image background `{color.lower()}` saved to: {modified_image_path}")


@main.command()
@click.option('-f', '--file', required=True, type=click.Path(exists=True), help='Path to the image file.')
@click.option('-d', '--direction', required=True, type=click.Choice(['LEFT', 'RIGHT'], case_sensitive=False), help='Direction to rotate the image.')
@click.option('-a', '--angle', required=True, type=int, help='Angle in degrees to rotate the image.')
def turn(file, direction, angle):
    """Compress the image to a target file size."""
    image_cli = ImageCli(file)
    modified_image_path = image_cli.turn(direction=direction, angle=angle)
    click.echo(f"Turn file {direction} {angle} degrees, saved to: {modified_image_path}")


@main.command()
@click.option('-f', '--file', required=True, type=click.Path(exists=True), help='Path to the image file.')
@click.option('-t', '--text', required=True, type=str, help='Text to use as the watermark.')
@click.option('-p', '--position', default='bottomright', type=click.Choice(['topleft', 'topright', 'bottomleft', 'bottomright', 'center'], case_sensitive=False), help='Position to place the watermark. Default is bottomright.')
@click.option('--padding', default=50, type=int, help='Padding in pixels around the watermark. Default is 50.')
@click.option('--font-size', default=100, type=int, help='Font size for the watermark text. Default is 100.')
def watermark(file, text, position, padding, font_size):
    """Add a text watermark to the image."""
    image_cli = ImageCli(file)
    watermarked_image_path = image_cli.add_watermark(
        text=text,
    )
    click.echo(f"Added text watermark '{text}' to image, saved to: {watermarked_image_path}")

if __name__ == '__main__':
    main()
