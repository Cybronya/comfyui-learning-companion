# AILab_LoadImage

## 节点类型

`AILab_LoadImage`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image_path_or_URL:STRING`（1 次）
- `image:COMBO`（1 次）
- `upscale_method:COMBO`（1 次）
- `megapixels:FLOAT`（1 次）
- `scale_by:FLOAT`（1 次）
- `resize_mode:COMBO`（1 次）
- `size:INT`（1 次）
- `upload:IMAGEUPLOAD`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）
- `MASK:MASK`（1 次）
- `WIDTH:INT`（1 次）
- `HEIGHT:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "6.png", "lanczos", 1, "longest_side", 2048, "image", "image"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
