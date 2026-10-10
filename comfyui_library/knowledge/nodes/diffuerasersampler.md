# DiffuEraserSampler

## 节点类型

`DiffuEraserSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL_DiffuEraser`（1 次）
- `images:IMAGE`（1 次）
- `fps:FLOAT`（1 次）
- `video_mask:IMAGE`（1 次）
- `seed:INT`（1 次）
- `num_inference_steps:INT`（1 次）
- `guidance_scale:FLOAT`（1 次）
- `video_length:INT`（1 次）
- `mask_dilation_iter:INT`（1 次）
- `ref_stride:INT`（1 次）

## 输出

- `images:IMAGE`（1 次）
- `propainter_img:IMAGE`（1 次）
- `output_path:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[515151, "fixed", 2, 0, 10, 8, 10, 10, 50, false, "briaai/RMBG-2.0", false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
