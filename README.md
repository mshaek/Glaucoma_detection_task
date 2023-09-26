# Glaucoma_detection_task
Glaucoma Detection Task

# Introduction
Glaucoma is a leading cause of blindness worldwide. It is a progressive eye disease that damages the optic nerve, which carries visual information from the eye to the brain. Early diagnosis and treatment are essential to prevent vision loss.
Traditional methods of glaucoma diagnosis involve subjective assessment of the optic disc by a clinician. However, this process can be time-consuming and prone to errors. In recent years, there has been growing interest in using deep learning to develop automated glaucoma detection systems.

# Dataset Description
The dataset used in this study consists of fundus images (168 Glaucoma class and 482 Sanas Class) of patients. The images were of varying quality, difficult one for the task of glaucoma detection. 
Some of the images may have been wrongly classified. Training a model with this dataset is a very challenging task.
 
Figure 1: Sample images from Glaucoma Class

<img src="https://github.com/mshaek/Glaucoma_detection_task/blob/main/glaucoma%20images.png">


The images above are 5 sample images randomly displayed from the glaucoma class. Image name “Im0488_g_ORIGA.jpg”, third image from the left in Fig-1 appear to be almost sanas class. There are multiple examples of similar issues. 
 
Figure 2 Sample images from Sanas class

<img src="https://github.com/mshaek/Glaucoma_detection_task/blob/main/sanas%20images.png">

Similar issues were found in the images within Sanas Class. For example, “Im0001_ORIGA.jpg” appears to be a glaucoma image.
Also, some images have similar brightness around the circumference of the retina as optical disc region.

# Data Preprocessing Techniques
The following data preprocessing techniques were used:

•	Image resizing: All images were resized to a standard size of 299x299 pixels. This helps to reduce the computational cost of training the model.

•	Image normalization: The intensity values of all images were normalized to a range of 0 and 1. 

•	Optic disc cropping: This is a suggested image preprocessing step. The optic disc region was cropped from each image. This helps to focus the model on the most important part of the image for glaucoma detection.

# Model Architecture and Training
A pre-trained Xception model was used for glaucoma detection. A couple of feature extraction layers and a classification layer were added according to the task. The model was fine-tuned on the dataset of fundus images to learn the discriminative features of glaucoma.
The model was trained using the Adam optimizer and a cross-entropy loss function. The model was trained for 10 epochs.

# Model Evaluation Scores
The model was evaluated on a held-out test set of 100 fundus images. The following evaluation scores were obtained:

AUC: 0.5174 (95% CI: 0.4884, 0.5465)

Sensitivity: 0.7349 (95% CI: 0.7076, 0.7623)

Specificity: 0.3 (95% CI: 0.2716, 0.3284)

# Discussion
The model achieved an AUC score of 0.5174 on the test set, which is below the expected range of 0.90 for medical diagnostic tasks. This is likely due to the small size and low quality of the dataset. However, the model was able to achieve a sensitivity of 0.7349, which means that it was able to correctly identify 73% of the patients with glaucoma. This suggests that the model cannot be used as a screening tool for glaucoma with confidence as accuracy of similar medical diagnostics are expected to be around 90%.

# Challenges of the Task
The task of glaucoma detection is challenging due to the following reasons:

•	The optic disc is a small and complex structure, which can make it difficult for the model to learn the discriminative features of glaucoma.

•	Glaucoma is a progressive disease, which means that the appearance of the optic disc can vary depending on the stage of the disease.

•	The dataset used in this study was small and of varying quality. Labelling of images may be incorrect.

# Possible Improvements
The following improvements could be made to the model:

•	Use a larger and higher quality dataset.

•	Double check the image class/label

•	Use a more powerful GPU to allow for more complex model architectures.

•	Explore different data augmentation techniques to improve the performance of the model on the training set.

•	Consider using image segmentation techniques to identify the optic disc region more accurately.

# Conclusion
This study demonstrated the feasibility of using deep learning to develop an automated glaucoma detection system. The model achieved a sensitivity of 0.7349 on the test set. However, further work is needed to improve the performance of the model using a larger and higher-quality dataset.
