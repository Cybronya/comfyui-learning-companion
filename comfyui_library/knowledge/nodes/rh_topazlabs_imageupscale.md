# RH_TopazLabs_ImageUpscale

## 节点类型

`RH_TopazLabs_ImageUpscale`

## 分类

Upscale

## 作用

放大类节点：提升图像/视频分辨率（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `scale:COMBO`（1 次）
- `model:COMBO`（1 次）
- `subject_detection:COMBO`（1 次）
- `face_enhancement:BOOLEAN`（1 次）
- `face_enhancement_creativity:FLOAT`（1 次）
- `face_enhancement_strength:FLOAT`（1 次）

## 输出

- `upscaled_image:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["2", "Standard V2", "None", false, 0, 0.8]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
