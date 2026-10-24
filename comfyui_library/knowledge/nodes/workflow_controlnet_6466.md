# workflow>controlnet

## 节点类型

`workflow>controlnet`

## 分类

Conditioning

## 作用

ControlNet 控制类节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `图像:IMAGE`（2 次）
- `model:MODEL`（2 次）
- `vae:VAE`（2 次）
- `mask:MASK`（2 次）
- `name:COMBO`（2 次）
- `preprocessor:COMBO`（2 次）
- `resolution:INT`（2 次）
- `strength:FLOAT`（2 次）

## 输出

- `图像:IMAGE`（2 次）
- `MODEL:MODEL`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["qwen_image_canny_diffsynth_controlnet.safetensors", "CannyEdgePreprocessor", 512, 0.7000000000000002]`（1 次）
- `["qwen_image_depth_diffsynth_controlnet.safetensors", "DepthAnythingPreprocessor", 512, 0.7000000000000002]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
