import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
image_paths = ['5.jpg', 'image1.jpg', 'image2.jpg']

def create_pixel_art(image, pixel_size):
    h, w = image.shape[:2]
    small = cv2.resize(image, (w // pixel_size, h // pixel_size), interpolation=cv2.INTER_NEAREST)
    pixel_art = cv2.resize(small, (w, h), interpolation=cv2.INTER_NEAREST)
    return pixel_art

def apply_color_effect(image, effect_type):
    if effect_type == "red":
        image[:, :, 1] = 0  
        image[:, :, 2] = 0  
    elif effect_type == "green":
        image[:, :, 0] = 0  
        image[:, :, 2] = 0 
    elif effect_type == "blue":
        image[:, :, 0] = 0 
        image[:, :, 1] = 0  
    elif effect_type == "sepia":
        kernel = np.array([[0.272, 0.534, 0.131],
                           [0.349, 0.686, 0.168],
                           [0.393, 0.769, 0.189]])
        image = cv2.transform(image, kernel)
        image = np.clip(image, 0, 255)
    elif effect_type == "negative":
        image = cv2.bitwise_not(image)
    return image

def save_image(image, output_path):
    cv2.imwrite(output_path, image)
color_effects = ["red", "green", "blue", "sepia", "negative"]

def display_images(image_paths, pixel_size=10, cols=2):
    num_images = len(image_paths)
    rows = num_images // cols + num_images % cols  
    
    plt.figure(figsize=(12, rows * 6 // cols))  
    
    for i, image_path in enumerate(image_paths):
        if not os.path.exists(image_path):
            print(f"Image not found: {image_path}")
            continue
        image = cv2.imread(image_path)
        pixel_art_image = create_pixel_art(image, pixel_size)
  
        effect = color_effects[i % len(color_effects)]
        colored_image = apply_color_effect(pixel_art_image, effect)
        
        plt.subplot(rows, cols, i + 1)
        plt.title(f'{effect.capitalize()} Pixel Art {i+1}', fontsize=16, fontweight='bold', color='teal')
        plt.imshow(cv2.cvtColor(colored_image, cv2.COLOR_BGR2RGB))
        plt.axis('off')
       
        save_image(colored_image, f'pixel_art_{effect}_{i+1}.jpg')

    plt.tight_layout()
    plt.show()


display_images(image_paths, pixel_size=10, cols=2)
