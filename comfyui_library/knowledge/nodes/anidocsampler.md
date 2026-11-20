# AniDocSampler

## 节点类型

`AniDocSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `anidoc_pipeline:ANIDOC_PIPELINE`（1 次）
- `controlnet_images:IMAGE`（1 次）
- `reference_image:IMAGE`（1 次）
- `cotracker:ANIDOC_COTRACKER`（1 次）

## 输出

- `video_frames:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[false, 7, 25, 0.02, 797340628055677, "randomize", 127, 8]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
