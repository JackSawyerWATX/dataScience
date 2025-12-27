from PIL import Image
import numpy as np


def count_pixels(image_path="photo.jpg", print_hex=True):
    """Iterate every pixel in the image, optionally print each pixel as hex,
    and return the total number of pixels processed.
    """
    img = Image.open(image_path).convert("RGBA")   # normalize to RGBA
    arr = np.array(img)                             # shape (h, w, 4)
    h, w = arr.shape[:2]

    total = 0
    for y in range(h):
        row = arr[y]
        for x in range(w):
            px = row[x]
            if px.shape[0] == 4:
                r, g, b, a = px
                if print_hex:
                    print(f"#{r:02x}{g:02x}{b:02x}{a:02x}")
            else:
                r, g, b = px
                if print_hex:
                    print(f"#{r:02x}{g:02x}{b:02x}")
            total += 1
    return total


if __name__ == "__main__":
    total_pixels = count_pixels("photo.jpg", print_hex=True)
    print(f"Total pixels counted: {total_pixels}")


    # Total pixels counted: 3145728