import unittest
import os
from PIL import Image as PillowImage
from imagecli.image import ImageCli  # Assuming image_cli.py contains the ImageCli class


class TestImageCli(unittest.TestCase):
    def setUp(self):
        # Create a temporary test image
        self.test_image_path = 'test_image.jpg'
        self.compressed_image_path = 'compressed_test_image.jpg'
        image = PillowImage.new('RGB', (100, 100), color='red')
        image.save(self.test_image_path)

        self.image_cli = ImageCli(self.test_image_path)

    def tearDown(self):
        # Remove the test images
        if os.path.exists(self.test_image_path):
            os.remove(self.test_image_path)
        if os.path.exists(self.compressed_image_path):
            os.remove(self.compressed_image_path)

    def test_size(self):
        size = self.image_cli.size
        self.assertEqual(size.width, 100)
        self.assertEqual(size.height, 100)

    def test_file_size(self):
        # Check that the file size is positive
        self.assertGreater(self.image_cli.file_size, 0)

    def test_compress_image_to_smaller_size(self):
        # Attempt to compress to 1KB
        compressed_path = self.image_cli.compress_image(1, unit='KB')
        compressed_size = os.path.getsize(compressed_path)
        self.assertLessEqual(compressed_size, 1024)

    def test_compress_image_to_same_size(self):
        # Attempt to compress to the same size or greater
        current_size_bytes = self.image_cli.file_size
        compressed_path = self.image_cli.compress_image(current_size_bytes / 1024, unit='KB')
        compressed_size = os.path.getsize(compressed_path)
        self.assertEqual(compressed_size, current_size_bytes)

    def test_get_formatted_size(self):
        bytes_size = self.image_cli.get_formatted_size(unit='bytes')
        kb_size = self.image_cli.get_formatted_size(unit='KB')
        mb_size = self.image_cli.get_formatted_size(unit='MB')
        gb_size = self.image_cli.get_formatted_size(unit='GB')

        self.assertIn('bytes', bytes_size)
        self.assertIn('KB', kb_size)
        self.assertIn('MB', mb_size)
        self.assertIn('GB', gb_size)

    def test_pillow_image_call_valid_method(self):
        # Test calling a method of PillowImage instance
        format = self.image_cli.pillow_image_call('format')
        self.assertEqual(format, 'JPEG')


if __name__ == '__main__':
    unittest.main()
