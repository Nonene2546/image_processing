import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
import cv2
import matplotlib.animation as animation

def plot_image_grid(img_arr, shape=(4, 5)):
    fig = plt.figure(figsize=shape)
    grid = ImageGrid(fig, (0, 0, 7, 7), shape, axes_pad=0.1)

    for ax, im in zip(grid, img_arr):
        # Iterating over the grid returns the Axes.
        ax.imshow(im)
        ax.set_axis_off()
    plt.show()

def write_images_to_video(image_array, output_file, frame_rate=10):
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    height, width = image_array[0].shape[:2]
    out = cv2.VideoWriter(output_file, fourcc, frame_rate, (width, height))

    for image in image_array:
        out.write(image)

def create_animation(image_arr, interval=100):
    fig = plt.figure()
    artists = []
    for image in image_arr:
        artists.append([plt.imshow(image, animated=True)])

    ani = animation.ArtistAnimation(fig, artists, interval)
    return ani

def subplot(axs, img, title, cmap="viridis"):
    axs.imshow(img, cmap=cmap)
    axs.set_title(title)
    axs.axis('off')