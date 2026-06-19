import os
from PIL import Image

def convert_images_to_webp(static_dir, output_dir):
    """
    Converts all JPEG images in a directory to WebP format.
    WebP files are saved alongside the original JPEGs.
    """
    image_extensions = ('.jpg', '.jpeg')
    
    print(f"Starting WebP conversion in: {static_dir}")
    print(f"Outputting WebP files to: {output_dir}")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    converted_count = 0
    for root, _, files in os.walk(static_dir):
        for file in files:
            if file.lower().endswith(image_extensions):
                input_path = os.path.join(root, file)
                # Create corresponding path in output_dir
                relative_path = os.path.relpath(input_path, static_dir)
                output_path = os.path.join(output_dir, os.path.splitext(relative_path)[0] + '.webp')

                # Ensure output directory exists for the WebP file
                os.makedirs(os.path.dirname(output_path), exist_ok=True)

                try:
                    with Image.open(input_path) as img:
                        # Use a quality between 75-85 for good balance of size and quality
                        img.save(output_path, "webp", quality=80)
                        print(f"Converted: {file} -> {os.path.basename(output_path)}")
                        converted_count += 1
                except Exception as e:
                    print(f"Error converting {file}: {e}")
    
    print(f"\nFinished converting {converted_count} images to WebP.")
    print("Remember to update your HTML templates and Service Worker to use the .webp files.")

if __name__ == "__main__":
    # Assuming your Flask app structure is:
    # pekimdev/
    #   app.py
    #   app/
    #     static/
    #       images/
    #         image15.jpg
    #     templates/
    #   convert_images.py (this script)
    
    # Adjust static_images_path if your static folder is elsewhere
    script_dir = os.path.dirname(os.path.abspath(__file__))
    static_images_path = os.path.join(script_dir, 'app', 'static', 'images')
    
    # WebP files will be saved in a new 'webp' subdirectory within static/images
    webp_output_path = os.path.join(static_images_path, 'webp')
    
    convert_images_to_webp(static_images_path, webp_output_path)
