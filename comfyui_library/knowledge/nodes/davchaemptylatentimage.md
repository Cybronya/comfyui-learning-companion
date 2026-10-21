# DavchaEmptyLatentImage

## 节点类型

`DavchaEmptyLatentImage`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `width:INT`（1 次）
- `height:INT`（1 次）
- `option:COMBO`（1 次）
- `batch_size:INT`（1 次）

## 输出

- `latent:LATENT`（1 次）
- `upscale_factor:FLOAT`（1 次）
- `batch_size:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[512, 768, "512x768: 1", 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
