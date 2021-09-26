# CNN 용어정리


## CNN모델

 - Feature Extraction + Classification
   (이미지의 특징을 추출하는 부분 + 이미지 클래스를 분류하는 부분)

 - 이미지 값의 위치정보까지 학습시킬 수 있음

### Feature Extraction

 - Convolution Layer와 Pooling Layer들의 연속
 - Convolution Layer : (필수) 필터를 적용하고 활성화 함수를 가지는 레이어
 - Pooling Layer : (선택) 

### Convolution
 - 합성곱 : 일정 크기의 필터를 통해 전체 입력데이터를 순회하며 합성곱을 계산하고, 해당 결과로 Feature Map을 만드는 과정
 - Convolution Layer

### Channel
 - 필터의 종류의 수에 따라 Feature Map의 채널수가 결정됨
 - ex. 컬러 이미지 데이터의 각 RGB 실수값 -> 3차원데이터 -> 3개의 채널로 구성

### Filter & Stride
 - CNN에서Filter와 Kernel은 같은 의미
 - Filter : 이미지의 특징을 찾아내기 위한 파라미터 / 추출맵
 - Stride : 합성곱 계산을 위해 Filter를 이동시키는 일정한/지정된 간격
 - Stride값에 따라 Filter를 이동시켜 전체 데이터 값의 합성곱을 계산-> 각 Channel의 결과값의 합으로 Feature Map 생성

### Padding(패딩)
 - Filter와 Stride에 따라 출력값의 크기가 줄어드는데 이를 방지하기 위함
 - 입력 데이터의 외곽에 지정된 픽셀을 특정 값(일반적으로 0)으로 채우는 것(Zero Padding)
 - padding = valid : 입력보다 출력크기가 작아짐
 - padding = same : 입력과 출력의 크기가 같음
            -> same일 때 연산량이 많아지기 때문에 Pooling Layer를 적용

### Pooling Layer
 - Convolution Layer의 출력데이터를 강조하기 위해서 또는 크기를 줄이기 위해서 사용됨
 - 종류 : Max Pooling Layer, Average Pooling, Min Pooling
 - 보편적인 활용법 : Max Pooling Layer를 사용하며, Pooling 크기와 Stride 크기를 같게 설정하여 모든 원소가 한번만 처리되게끔 한다.


## Classification (Fully Connected Layer)
 - Flatten Layer : 이미지 형태를 배열 형태로 전환하는 레이어(FC형태로 변경)

