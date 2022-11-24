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
	│   │   └── test00.png
	│   └── labels
	│       └── test00.txt
	└── data_rotational
	    ├── images
	    │   ├── test00_000.jpg
	    │   ├── test00_030.jpg
	    │   └── ...
	    └── labels
	        ├── test00_000.txt
	        ├── test00_030.txt
	        └── ...



사용법


### 1. Rotation
- Default 30, 330 회전 이미지 얻어짐
```python
python rotation.py data_original
```

- 회전 각 바꾸고 싶으면 ( 입력한 값, 입력한 값 + 330) 회전 이미지 얻어짐
```python
python rotation.py data_original -a 45
```

### 2. flip
- Horizontal flip만 구현되어져 있음
```python
python flip.py data_original
```
![HorizontalFlip](https://user-images.githubusercontent.com/77952928/203718696-c5ae0b24-af20-4078-bd15-cd245410e230.png)

### 3. translation
- -0.2 ~ 0.2 비율 안에서 랜덤으로 움직임
```python
python translation.py data_original
```
![Translation](https://user-images.githubusercontent.com/77952928/203718739-b8d7640c-2b6d-4311-9fbd-e094fcf04f3a.png)

### 4. Crop
- 1.0 ~ 1.5 비율 안에서 랜덤하게 Crop
```python
python crop.py data_original
```
![Crop](https://user-images.githubusercontent.com/77952928/203718782-2d45f5c3-e0f6-4d13-b2d2-2b710f4ee19a.png)

### 5. 결과 확인
```python
python check_label.py <폴더 이름>
```
