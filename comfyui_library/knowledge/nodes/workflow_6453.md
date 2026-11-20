# workflow>脸部优化

## 节点类型

`workflow>脸部优化`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `CLIP:CLIP`（1 次）
- `图像:IMAGE`（1 次）
- `模型:MODEL`（1 次）
- `FaceDetailer clip:CLIP`（1 次）
- `VAE:VAE`（1 次）
- `Segm检测:SEGM_DETECTOR`（1 次）
- `细化约束:DETAILER_HOOK`（1 次）
- `scheduler_func_opt:SCHEDULER_FUNC`（1 次）
- `目标图像:IMAGE`（1 次）
- `model_name:COMBO`（1 次）

## 输出

- `SEGM检测:SEGM_DETECTOR`（1 次）
- `高度:INT`（1 次）
- `细化图像:IMAGE`（1 次）
- `细化部分:IMAGE`（1 次）
- `细化节点束:DETAILER_PIPE`（1 次）
- `ControlNet图像:IMAGE`（1 次）
- `宽度:INT`（1 次）
- `ImageResize+ 高度:INT`（1 次）
- `图像:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["bbox/face_yolov8n_v2.pt", "insightface", "CUDA", "sam_vit_h_4b8939.pth", "Prefer GPU", "masterpiece,best quality,finel`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
