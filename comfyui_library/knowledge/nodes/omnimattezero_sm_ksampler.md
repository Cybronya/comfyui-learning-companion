# OmnimatteZero_SM_KSampler

## 节点类型

`OmnimatteZero_SM_KSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（2 次）
- `images:IMAGE`（2 次）
- `mask:IMAGE`（2 次）
- `positive:CONDITIONING`（2 次）
- `negative:CONDITIONING`（2 次）
- `width:INT`（2 次）
- `height:INT`（2 次）
- `num_frames:INT`（2 次）
- `guidance_scale:FLOAT`（2 次）
- `steps:INT`（2 次）

## 输出

- `IMAGE:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1280, 704, 121, 3, 20, 99557854, "randomize", 5]`（1 次）
- `[1280, 704, 81, 3, 20, 1150759720, "randomize", 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
