# Course work, facial recognition system for personal identification (fat client)

**General pipeline**
1. Image Capture: The system initiates its operation by capturing an image, which can be obtained from a camera or another video source.

2. Face Detection: In this step, the system applies the FaceBoxes network to detect faces in the image. FaceBoxes employs convolutional neural networks to localize and highlight regions where faces are present, accurately determining the position and sizes of faces in the image.

3. Image Preprocessing: After face detection, the system performs image preprocessing. This step may involve normalization, resizing, and other operations to standardize images and enhance recognition quality.

4. Face Feature Extraction: Next, the system applies the ArcFace network to extract unique facial features from preprocessed images. ArcFace transforms facial images into vector representations known as embeddings. These embeddings are highly informative and unique for each face.

5. Comparison and Identification: When an identification request is made, the system compares the face embeddings obtained from the current image with stored embeddings in the database. Cosine similarity is used for comparison. Based on the comparison results, the system determines whether there is a match with registered faces and identifies the person if a match is found.


# Video review
https://drive.google.com/file/d/12VRE3c_iNCon9Ia11srhQ3MAqph3idfa/view

# Screenshots

![image](https://github.com/iRespectOnlyYen/CourseWork1/assets/90966720/4de4228d-c073-4a84-b8e7-b3af2068f336)

![image](https://github.com/iRespectOnlyYen/CourseWork1/assets/90966720/eada10f1-289d-47ca-8dca-9dd70f3aa089)

![image](https://github.com/iRespectOnlyYen/CourseWork1/assets/90966720/67f25e68-4387-4ee6-8198-ae8fba72de50)

![image](https://github.com/iRespectOnlyYen/CourseWork1/assets/90966720/52e22c7d-79ac-4e5c-9e23-aaeac584e4b1)

![image](https://github.com/iRespectOnlyYen/CourseWork1/assets/90966720/95986843-bfdd-4616-964e-525cd26b82de)

![image](https://github.com/iRespectOnlyYen/CourseWork1/assets/90966720/287b1d4e-0f14-4b0c-90aa-52def00fab3d)

![image](https://github.com/iRespectOnlyYen/CourseWork1/assets/90966720/3a5b2f65-e2f8-45f6-ae03-902c1ed1705f)

![image](https://github.com/iRespectOnlyYen/CourseWork1/assets/90966720/e7e14f56-014c-4eb1-a75e-a77d10ebf903)
