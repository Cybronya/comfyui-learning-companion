# Image Remove Background Rembg (mtb)

## 节点类型

`Image Remove Background Rembg (mtb)`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `alpha_matting:BOOLEAN`（1 次）
- `alpha_matting_foreground_threshold:INT`（1 次）
- `alpha_matting_background_threshold:INT`（1 次）
- `alpha_matting_erode_size:INT`（1 次）
- `post_process_mask:BOOLEAN`（1 次）
- `bgcolor:COLOR`（1 次）

## 输出

- `Image (rgba):IMAGE`（1 次）
- `Mask:MASK`（1 次）
- `Image:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, 240, 10, 10, true, "#000000"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
