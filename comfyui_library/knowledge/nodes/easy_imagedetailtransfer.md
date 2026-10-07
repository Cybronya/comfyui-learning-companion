# easy imageDetailTransfer

## 节点类型

`easy imageDetailTransfer`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `target:IMAGE`（2 次）
- `source:IMAGE`（2 次）
- `mask:MASK`（2 次）
- `mode:COMBO`（2 次）
- `blur_sigma:FLOAT`（2 次）
- `blend_factor:FLOAT`（2 次）
- `image_output:COMBO`（2 次）
- `save_prefix:STRING`（2 次）

## 输出

- `image:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["add", 2, 1, "Hide", "ComfyUI"]`（1 次）
- `["add", 1.0000000000000002, 1, "Hide", "ComfyUI"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
