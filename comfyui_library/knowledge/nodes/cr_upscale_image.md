# CR Upscale Image

## 节点类型

`CR Upscale Image`

## 分类

Upscale

## 作用

放大类节点：提升图像/视频分辨率（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）

## 输出

- `IMAGE:IMAGE`（2 次）
- `show_help:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["4x_NMKD-Siax_200k.pth", "rescale", 1.5, 1024, "lanczos", "true", 8]`（1 次）
- `["4x-UltraSharp.pth", "resize", 2, 1536, "lanczos", "true", 8]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
