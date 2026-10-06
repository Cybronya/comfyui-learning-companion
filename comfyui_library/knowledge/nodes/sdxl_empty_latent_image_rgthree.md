# SDXL Empty Latent Image (rgthree)

## 节点类型

`SDXL Empty Latent Image (rgthree)`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `dimensions:COMBO`（3 次）
- `clip_scale:FLOAT`（3 次）
- `batch_size:INT`（3 次）

## 输出

- `LATENT:LATENT`（3 次）
- `CLIP_WIDTH:INT`（3 次）
- `CLIP_HEIGHT:INT`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[" 768 x 1344  (portrait)", 2, 1]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
