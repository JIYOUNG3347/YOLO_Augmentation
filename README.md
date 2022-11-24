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
![HorizontalFlip](https://user-images.githubusercontent.com/77952928/203719159-38c47ff9-234a-4cda-828a-d57a16e1f466.png)

### 3. translation
- -0.2 ~ 0.2 비율 안에서 랜덤으로 움직임
```python
python translation.py data_original
```
![Translation](https://user-images.githubusercontent.com/77952928/203719166-14cdb418-2c04-470c-9f7f-39d2de8799b2.png)

### 4. Crop
- 1.0 ~ 1.5 비율 안에서 랜덤하게 Crop
```python
python crop.py data_original
```
![Crop](https://user-images.githubusercontent.com/77952928/203719174-c3303a64-eaa4-47d0-9fef-0f9c4ba95b09.png)

### 5. 결과 확인
```python
python check_label.py <폴더 이름>
```
