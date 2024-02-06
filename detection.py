import os
from ultralytics import YOLO
import cv2
import numpy as np

def define_hot_cold_regions(image):

    center = (image.shape[1] // 2, image.shape[0] // 2)

    
    cold_radius = 100  


    labels = np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8)

  
    distances = np.sqrt((np.arange(image.shape[0])[:, np.newaxis] - center[1])**2 +
                        (np.arange(image.shape[1])[np.newaxis, :] - center[0])**2)


    labels[distances <= cold_radius] = 0  
    labels[distances > cold_radius] = 1   

    return labels

def calculate_distance(box1, box2):

    center1 = ((box1[0] + box1[2]) / 2, (box1[1] + box1[3]) / 2)
    center2 = ((box2[0] + box2[2]) / 2, (box2[1] + box2[3]) / 2)


    distance = np.sqrt((center1[0] - center2[0])**2 + (center1[1] - center2[1])**2)

    return distance


frame = cv2.imread('./random3.jpg')


model = YOLO("runs/detect/train7/weights/best.pt")  

threshold = 0.1


hot_cold_labels = define_hot_cold_regions(frame)

total_objects_detected = 0
total_efficiency_score = 0


results = model(frame)
print(results)
for result in results.boxes.data.tolist():
    x1, y1, x2, y2, score, class_id = result
    if score > threshold:
        total_objects_detected += 1

        box_center = ((x1 + x2) // 2, (y1 + y2) // 2)
        if hot_cold_labels[box_center[1], box_center[0]] == 0:

            efficiency_score = 0.5 
        else:
 
            efficiency_score = 1.5  

        visibility_score = calculate_visibility(frame)
        # Calculate distance score (assuming you have two bounding boxes to compare)
        distance_score = calculate_distance((x1, y1, x2, y2), (x1_other, y1_other, x2_other, y2_other))
        # Calculate the final efficiency score
        final_efficiency_score = efficiency_score * visibility_score * distance_score
        total_efficiency_score += final_efficiency_score
        # Display or save the processed frame
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
        cv2.putText(frame, f"{results.names[int(class_id)].upper()} Score: {final_efficiency_score:.2f}", 
                    (int(x1), int(y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
    

# Display or save the total efficiency score
print(f"Total Objects Detected: {total_objects_detected}")
print(f"Total Efficiency Score: {total_efficiency_score:.2f}")


cv2.destroyAllWindows()
