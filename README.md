# yolo_augmentation

## Directory structure
	.
	├── check_label.py
	├── rotation.py
	├── flip.py
	├── translation.py
	├── crop.py
	├── data_original
	│   ├── images
	│   │   └── Zidane.jpg
	│   └── labels
	│       └── zidane.txt
	└── data_rotational
	    ├── images
	    │   ├── zidane_015.jpg
	    │   ├── zidane_030.jpg
	    │   ├── zidane_330.jpg
	    │   ├── zidane_345.jpg
	    │   ├── zidane_crop.jpg
	    │   ├── zidane_flip.jpg
	    │   └── ...
	    └── labels
	        ├── zidane_015.txt
	        ├── zidane_030.txt
	        ├── zidane_330.txt
	        ├── zidane_345.txt
	        ├── zidane_crop.txt
	        ├── zidane_flip.txt
	        └── ...



사용법


### 1. Rotation
- Default 30, 330 회전 이미지 얻어짐
```python
python rotation.py data_original
```
![rotation_30](https://user-images.githubusercontent.com/77952928/203884349-985bdefe-81f0-4860-ae76-4cee3e2d716f.png)

- 회전 각 바꾸고 싶으면 ( 입력한 값, 360 - 입력한 값) 회전 이미지 얻어짐
```python
python rotation.py data_original -a 15
```
![rotation_15](https://user-images.githubusercontent.com/77952928/203884400-7ab8a5fb-9172-4cd8-b030-e4ca4cc8a01d.png)

### 2. Flip
- Horizontal flip만 구현되어져 있음
```python
python flip.py data_original
```
![flip](https://user-images.githubusercontent.com/77952928/203884563-984c6c57-99fb-4664-b3b9-249b77999fb1.png)

### 3. Translation
- -0.2 ~ 0.2 비율 안에서 랜덤으로 움직임
```python
python translation.py data_original
```
![translation](https://user-images.githubusercontent.com/77952928/203884786-8d66ead2-2f4e-4f96-a02f-0fe4a4ba92bc.png)

- 비율 바꾸려면
```python
python translation.py data_original -r 0.3
```

### 4. Crop
- 1.0 ~ 1.5 비율 안에서 랜덤하게 Crop
```python
python crop.py data_original
```
![crop](https://user-images.githubusercontent.com/77952928/203884672-18b11c4b-52e0-4429-a247-e5db77a7d794.png)

- 비율 바꾸려면
```python
python crop.py data_original -r 0.3
```

### 5. 결과 확인
```python
python check_label.py data_result
```


