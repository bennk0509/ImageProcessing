import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

kernelBlur = np.array([[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]]) / 9

kernelSharpness = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])


def save_image(image, name, function, extension='.jpg'):
    #Save image
    image.save(name + '_' + function + extension)

def show_gray_image(img,reduce_img):
    # Display the original and reduced images
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    
    # Display the first image on the first subplot
    axes[0].imshow(img)
    axes[0].axis('off')  # Remove axes for the first image
    axes[0].set_title('Image 1')  # Set title for the first image
  
    # Display the second image on the second subplot
    axes[1].imshow(reduce_img, cmap='gray')
    axes[1].axis('off')  # Remove axes for the second image
    axes[1].set_title('Image 2')  # Set title for the second image

    # Adjust the spacing between subplots to add space for descriptions
    plt.subplots_adjust(bottom=0.2)

    # Add descriptions below the images
    axes[0].text(0.5, -0.15, 'Before', transform=axes[0].transAxes,
                ha='center', fontsize=12)
    axes[1].text(0.5, -0.15, 'After', transform=axes[1].transAxes,
                ha='center', fontsize=12)

    # Show the plot with both images and descriptions
    plt.show()
def show_image(img, reduce_img):
    # Display the original and reduced images
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    
    # Display the first image on the first subplot
    axes[0].imshow(img)
    axes[0].axis('off')  # Remove axes for the first image
    axes[0].set_title('Image 1')  # Set title for the first image
  
    # Display the second image on the second subplot
    axes[1].imshow(reduce_img)
    axes[1].axis('off')  # Remove axes for the second image
    axes[1].set_title('Image 2')  # Set title for the second image

    # Adjust the spacing between subplots to add space for descriptions
    plt.subplots_adjust(bottom=0.2)

    # Add descriptions below the images
    axes[0].text(0.5, -0.15, 'Before', transform=axes[0].transAxes,
                ha='center', fontsize=12)
    axes[1].text(0.5, -0.15, 'After', transform=axes[1].transAxes,
                ha='center', fontsize=12)

    # Show the plot with both images and descriptions
    plt.show()

def ChangeBrightness(image, brightness=100):
    #Convert image to array
    image_array = np.array(image)
    #add brightness and clip to 0-255 range then convert back to uint8 type
    brightened_image = np.clip(image_array.astype(int) + brightness, 0, 255).astype(np.uint8)
    # new_arr = np.stack((r_new_channel, g_new_channel, b_new_channel), axis=2)
    #image_array = np.clip(image_array + brightness,0,255)
    # for i in range(image_array.shape[0]):
    #     for j in range (image_array.shape[1]):
    #         image_array[i][j][0]= truncate(image_array[i][j][0] + brightness)
    #         image_array[i][j][1]= truncate(image_array[i][j][1] + brightness)
    #         image_array[i][j][2]= truncate(image_array[i][j][2] + brightness)
    new_img = Image.fromarray(brightened_image)
    return new_img

def ChangeContrast(image,contrast):
    #Convert image to array
    image_array = np.array(image)
    #add brightness and clip to 0-255 range then convert back to uint8 type
    factor = (259 * (contrast + 255)) / (255 * (259 - contrast))
    adjusted_image = np.clip((image_array.astype(int) - 128) * factor + 128, 0, 255).astype(np.uint8)
    # for i in range(image_array.shape[0]):
    #     for j in range (image_array.shape[1]):
    #         image_array[i][j][0]= truncate(factor*(image_array[i][j][0] - 128) + 128)
    #         image_array[i][j][1]= truncate(factor*(image_array[i][j][1] - 128) + 128)
    #         image_array[i][j][2]= truncate(factor*(image_array[i][j][2] - 128) + 128)
    new_img = Image.fromarray(adjusted_image)
    return new_img

#flip doc
def FlipImage(image):
    image_array = np.array(image)
    #flip vertical
    new_arr = np.flip(image_array,0)
    new_img = Image.fromarray(new_arr)
    return new_img

#flip ngang
def FlipImage1(image):
    image_array = np.array(image)
    #flip horizontal
    new_arr = np.flip(image_array,1)
    new_img = Image.fromarray(new_arr)
    return new_img

def GrayScale(image):
    image_array = np.array(image)
    new_arr_shape = (image_array.shape[0],image_array.shape[1])
    #create new array with shape of original array but only 1 channel
    new_arr = np.empty(new_arr_shape)
    #seperate each channel
    r_channel = image_array[:,:,0]
    g_channel = image_array[:,:,1]
    b_channel = image_array[:,:,2]
    #calculate new value for each pixel
    new_arr = np.clip(r_channel*0.299 + g_channel*0.587 + 0.114*b_channel,0,255)
    #convert to uint8 type
    new_arr = new_arr.astype(np.uint8)
    # for i in range(image_array.shape[0]):
    #     for j in range (image_array.shape[1]):
    #         new_arr[i][j] = truncate(0.299*image_array[i][j][0] + 0.587*image_array[i][j][1] + 0.114*image_array[i][j][2])
    new_img = Image.fromarray(new_arr)
    return new_img

def SepiaScale(image):
    image_array = np.array(image)
    #seperate each channel
    r_channel = image_array[:,:,0]
    g_channel = image_array[:,:,1]
    b_channel = image_array[:,:,2]
    # r_new_channel = 0.393*r_channel + 0.769*g_channel + 0.189*b_channel
    # g_new_channel = 0.349*r_channel + 0.686*g_channel + 0.168*b_channel
    # b_new_channel = 0.272*r_channel + 0.534*g_channel + 0.131*b_channel
    #calculate new value for each pixel
    r_new_channel= np.clip(0.393*r_channel + 0.769*g_channel + 0.189*b_channel,0,255)
    g_new_channel = np.clip(0.349*r_channel + 0.686*g_channel + 0.168*b_channel,0,255)
    b_new_channel = np.clip(0.272*r_channel + 0.534*g_channel + 0.131*b_channel,0,255)
    #combine 3 channels to new array
    new_arr = np.stack((r_new_channel, g_new_channel, b_new_channel), axis=2)
    # new_arr = truncate(0.393*r_channel + )
    # for i in range(image_array.shape[0]):
    #     for j in range (image_array.shape[1]):
    #         image_array[i][j][0]= truncate(0.393*image_array[i][j][0] + 0.769*image_array[i][j][1] + 0.189*image_array[i][j][2])
    #         image_array[i][j][1]= truncate(0.349*image_array[i][j][0] + 0.686*image_array[i][j][1] + 0.168*image_array[i][j][2])
    #         image_array[i][j][2]= truncate(0.272*image_array[i][j][0] + 0.534*image_array[i][j][1] + 0.131*image_array[i][j][2])
    new_arr = new_arr.astype(np.uint8)
    new_img = Image.fromarray(new_arr)
    return new_img 


def applyBlur(channel):
    blur_ch = np.zeros_like(channel)
    for i in range(1, channel.shape[0]-1):
        for j in range(1, channel.shape[1]-1):
            blur_ch[i,j] = np.sum(channel[i-1:i+2,j-1:j+2] * kernelBlur)    #apply kernel to each pixel
    return blur_ch

def BoxBlur(image):
    image_array = np.array(image)
    #seperate each channel
    r_channel = image_array[:,:,0]
    g_channel = image_array[:,:,1]
    b_channel = image_array[:,:,2]
    #apply blur to each channel
    blur_r_channel = applyBlur(r_channel)
    blur_g_channel = applyBlur(g_channel)
    blur_b_channel = applyBlur(b_channel)
    #combine 3 channels to new array
    new_arr = np.stack((blur_r_channel, blur_g_channel, blur_b_channel), axis=2)
    new_arr = new_arr.astype(np.uint8)
    new_img = Image.fromarray(new_arr)
    return new_img 

def applySharpening(channel):
    sharp_ch = np.zeros_like(channel)
    for i in range(1, channel.shape[0] - 1):
        for j in range(1, channel.shape[1] - 1):
            sharp_ch[i,j] = np.clip(np.sum(channel[i-1:i+2,j-1:j+2] * kernelSharpness),0,255) #apply kernel to each pixel
    return sharp_ch
def Sharpening(image):
    image_array = np.array(image)
    #seperate each channel
    r_channel = image_array[:,:,0]
    g_channel = image_array[:,:,1]
    b_channel = image_array[:,:,2]
    #apply sharpening to each channel
    sharp_r_channel = applySharpening(r_channel)
    sharp_g_channel = applySharpening(g_channel)
    sharp_b_channel = applySharpening(b_channel)
    #combine 3 channels to new array
    new_arr = np.stack((sharp_r_channel, sharp_g_channel, sharp_b_channel), axis=2)
    new_arr = new_arr.astype(np.uint8)
    new_img = Image.fromarray(new_arr)
    return new_img 
    

def CropCenter(image, crop_size=350):
    image_array = np.array(image)
    #find center of image
    center_y = image_array.shape[0] // 2
    center_x = image_array.shape[1] // 2
    #find the starting point and ending point of the crop
    start_y = center_y - crop_size // 2
    end_y = center_y + crop_size // 2 + 1
    start_x = center_x - crop_size // 2
    end_x = center_x + crop_size // 2 + 1
    #crop the image by getting sub array from starting point to ending point
    center_cropped_image = image_array[start_y:end_y,start_x:end_x]
    center_cropped_image = center_cropped_image.astype(np.uint8)
    new_img = Image.fromarray(center_cropped_image)
    return new_img 
    

def CropCircular(image):
    image_array = np.array(image)
    #find center of image
    center_y = image_array.shape[0]//2
    center_x = image_array.shape[1]//2
    radius = min(center_y,center_x) #radius of the circle
    yy,xx = np.ogrid[:image_array.shape[0],:image_array.shape[1]] #create meshgrid
    mask = (yy-center_y)**2 + (xx-center_x)**2 <= radius**2 #create mask
    circular_image = np.copy(image_array) #copy image
    circular_image[~mask] = 0 #apply mask
    circular_image = circular_image.astype(np.uint8)
    new_img = Image.fromarray(circular_image)
    return new_img
    

# def CropEllipse(image):
#     image_array = np.array(image)
#     center_y = image_array.shape[0]//2
#     center_x = image_array.shape[1]//2
#     radius = min(center_y,center_x)


def main():
    #read image and convert to numpy array
    print("Enter the name of the image file: ")
    image_name = input()
    image = Image.open(image_name)
    last_dot_index = image_name.rfind('.')
    if last_dot_index != -1:
        name = image_name[:last_dot_index]
        extension = image_name[last_dot_index:]
    else:
        name = image_name
        extension = ""
    while(True):
        print("Enter the number of the operation you want to perform: ")
        print("1. Change brightness")
        print("2. Change contrast")
        print("3. Flip Image horizontally")
        print("4. Flip Image vertically")
        print("5. Convert to grayscale")
        print("6. Convert to sepia")
        print("7. Apply box blur")
        print("8. Apply sharpening")
        print("9. Crop center")
        print("10. Crop circular")
        print("11. Crop elliptical")
        print("0. All of the above")
        operation = int(input())
        match operation:
            case 1:
                new_img = ChangeBrightness(image,brightness=100)
                show_image(image, new_img)
                save_image(new_img, name, 'brightness', extension)
            case 2:
                new_img = ChangeContrast(image,contrast=200)
                show_image(image, new_img)
                save_image(new_img, name, 'contrast', extension)
            case 3:
                new_img = FlipImage1(image)
                show_image(image, new_img)
                save_image(new_img, name, 'flipngang', extension)
            case 4:
                new_img = FlipImage(image)
                show_image(image, new_img)
                save_image(new_img, name, 'flipdoc', extension)
            case 5:
                new_img = GrayScale(image)
                show_gray_image(image, new_img)
                save_image(new_img, name, 'grayscale', extension)
            case 6:
                new_img = SepiaScale(image)
                show_image(image, new_img)
                save_image(new_img, name, 'sepia', extension)
            case 7:
                new_img = BoxBlur(image)
                show_image(image, new_img)
                save_image(new_img, name, 'boxblur', extension)
            case 8:
                new_img = Sharpening(image)
                show_image(image, new_img)
                save_image(new_img, name, 'sharpening', extension)
            case 9:
                new_img = CropCenter(image,crop_size=350)
                show_image(image, new_img)
                save_image(new_img, name, 'center_cropped', extension)
            case 10:
                new_img = CropCircular(image)
                show_image(image, new_img)
                save_image(new_img, name, 'circular_cropped', extension)
            # case 11:
            #     CropEllipse(image)
            case 0:
                save_image(ChangeBrightness(image,brightness=100), name, 'brightness', extension)
                save_image(ChangeContrast(image,contrast=200), name, 'contrast', extension)
                save_image(FlipImage(image), name, 'flipdoc', extension)
                save_image(FlipImage1(image), name, 'flipngang', extension)
                save_image(GrayScale(image), name, 'grayscale', extension)
                save_image(SepiaScale(image), name, 'sepia', extension)
                save_image(BoxBlur(image), name, 'boxblur', extension)
                save_image(Sharpening(image), name, 'sharpening', extension)
                save_image(CropCenter(image,crop_size=350), name, 'center_cropped', extension)
                save_image(CropCircular(image), name, 'circular_cropped', extension)
                # CropEllipse(image)
            case _:
                print("Invalid input")
        print("Do you want to perform another operation? (y/n)")
        choice = input()
        if choice == 'n':
            break

        


main()
