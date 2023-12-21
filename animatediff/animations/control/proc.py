import cv2

def resize_video(input_file, output_file, new_width, new_height):
    # Open the video file
    cap = cv2.VideoCapture(input_file)

    # Get the original video's properties
    original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Create a VideoWriter object to save the resized video
    fourcc = cv2.VideoWriter_fourcc('H','2','6','4')  # You can change the codec if needed
    out = cv2.VideoWriter(output_file, fourcc, fps, (new_width, new_height))

    while True:
        ret, frame = cap.read()

        if not ret:
            break  # Break the loop if the video has ended

        # Resize the frame
        resized_frame = cv2.resize(frame, (new_width, new_height))

        # Write the resized frame to the output video file
        out.write(resized_frame)


    # Release the video capture and writer objects
    cap.release()
    out.release()



if __name__ == "__main__":
    # Input and output file paths
    input_file_path = 'video_original.mp4'
    output_file_path = 'v.mp4'

    # Specify the new width and height
    new_width = 768
    new_height = 768

    # Resize the video
    resize_video(input_file_path, output_file_path, new_width, new_height)
