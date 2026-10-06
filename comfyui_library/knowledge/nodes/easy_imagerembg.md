# easy imageRemBg

## 节点类型

`easy imageRemBg`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `images:IMAGE`（3 次）
- `rem_mode:COMBO`（3 次）
- `image_output:COMBO`（3 次）
- `save_prefix:STRING`（3 次）
- `torchscript_jit:BOOLEAN`（3 次）
- `add_background:COMBO`（3 次）
- `refine_foreground:BOOLEAN`（3 次）

## 输出

- `image:IMAGE`（3 次）
- `mask:MASK`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["BEN2", "Preview", "ComfyUI", false, "white", false]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
