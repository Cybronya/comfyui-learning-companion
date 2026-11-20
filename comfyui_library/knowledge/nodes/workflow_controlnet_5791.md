# workflow>Controlnet

## 节点类型

`workflow>Controlnet`

## 分类

Conditioning

## 作用

ControlNet 控制类节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `model:MODEL`（1 次）
- `vae:VAE`（1 次）
- `inpaint_image:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `name:COMBO`（1 次）
- `preprocessor:COMBO`（1 次）
- `resolution:INT`（1 次）
- `strength:FLOAT`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）
- `MODEL:MODEL`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Z-Image-Turbo-Fun-Controlnet-Union.safetensors", "LineartStandardPreprocessor", 1024, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
