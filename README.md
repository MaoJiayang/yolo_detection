# YOLO11 Fine-Tuning on BDD100K Dataset

## 项目简介

本项目旨在使用 `BDD100K` 数据集对 `YOLO11` 模型进行微调，以提高其在城市交通场景下的目标检测性能。`BDD100K` 是一个包含 100k 视频及其标注的大型数据集，广泛应用于自动驾驶和智能交通系统的研究。在本项目中，我们将利用数据集的一个子集 `100k_images`。（其按照 7:2:1 的比例划分为训练集、验证集和测试集）

## 目录结构

```
bdd100k_yolo11_finetune/
├── datasets/
│   ├── bdd100k_det/
│   │   ├── images/
│   │   │   ├── train/    # 训练集图片
│   │   │   ├── val/      # 验证集图片
│   │   │   └── test/     # 测试集图片
│   │   ├── labels/
│   │   │   ├── train/    # 训练集标签
│   │   │   └── val/      # 验证集标签
│   │   └── bdd100K_det_yolo11.yaml  # YOLO 配置文件
├── download_bdd100k.py# 数据集下载脚本
├── label_preprocess.ipynb# 标签预处理脚本
├─── model_test.ipynb# 模型测试与可视化
├── training.py# 训练脚本
└── README.md# 项目说明文件
```

## 项目设置与数据准备

### 1. 下载数据集

本项目使用 `BDD100K` 数据集的一个子集 `100k_images` 进行训练。执行以下脚本下载数据集：

```bash
python scripts/download_bdd100k.py
```

该脚本将下载以下四个 ZIP 文件：

- `bdd100k_det_20_labels_trainval.zip`: 训练和验证集的标注文件（解压后得到两个 JSON 文件）。
- `100k_images_train.zip`: 训练集图片。
- `100k_images_val.zip`: 验证集图片。
- `100k_images_test.zip`: 测试集图片。

### 2. 解压与整理数据

建议在项目目录中新建一个 `datasets` 文件夹，并按照以下结构解压数据：

```bash
mkdir -p datasets/bdd100k_det/images/train
mkdir -p datasets/bdd100k_det/images/val
mkdir -p datasets/bdd100k_det/images/test
mkdir -p datasets/bdd100k_det/labels/train
mkdir -p datasets/bdd100k_det/labels/val
mkdir -p datasets/bdd100k_det/labels/test
```

解压下载的 ZIP 文件，将图片和标注文件分别放置在对应的目录中。

### 3. 标签预处理

运行 Jupyter Notebook `label_preprocess.ipynb` 以将 JSON 格式的标注文件转换为 YOLO 格式。确保调整脚本开头的参数以匹配实际路径。

#### `label_preprocess.ipynb` 主要功能：

- 读取训练和验证集的 JSON 标注文件。
- 转换边界框坐标为 YOLO 所需的归一化形式。
- 生成对应的 `.txt` 标签文件。
- 创建并保存 `bdd100K_det_yolo11.yaml` 配置文件。

## 下载预训练模型

你可以直接使用 YOLO 类加载预训练模型，也可以手动下载模型权重。

### 1. 直接使用 

在 `training.py` 中，通过以下方式加载预训练模型：

```python
from ultralytics import YOLO

# 加载预训练模型
model = YOLO("yolo11m")
```

### 2. 手动下载模型权重

下载预训练权重文件 

yolo11l.pt：[YOLO11M 预训练权重](https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11m.pt)

将下载的权重文件放置在项目根目录或指定的路径下，并在 `training.py` 中引用。

## 开始训练

在确认数据集已准备好且配置文件 `bdd100K_det_yolo11.yaml` 已生成后，运行以下命令开始训练：

```bash
python training.py
```

## 致谢

特别感谢 [Ultralytics](https://github.com/ultralytics) 提供的 YOLO 库，以及 BDD100K 数据集的开发者们。

