# DSDImageGenerator

## 节点类型

`DSDImageGenerator`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `dsd_model:DSD_MODEL`（1 次）
- `image:IMAGE`（1 次）
- `prompt:STRING`（1 次）
- `negative_prompt:STRING`（1 次）
- `resize_params:RESIZE_PARAMS`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `reference_image:IMAGE`（1 次）
- `seed:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Side view of anime character.", "text, watermark, blurry", 4, "fixed", 3.5, 1, 1, 28, 1024, 512, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
