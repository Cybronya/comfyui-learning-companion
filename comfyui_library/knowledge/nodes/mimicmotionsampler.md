# MimicMotionSampler

## 节点类型

`MimicMotionSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 20 个 workflow 中。

## 输入

- `mimic_pipeline:MIMICPIPE`（20 次）
- `ref_image:IMAGE`（20 次）
- `pose_images:IMAGE`（20 次）
- `optional_scheduler:DIFFUSERS_SCHEDULER`（20 次）

## 输出

- `samples:LATENT`（20 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[25, 2, 2, 42, "fixed", 15, 0, 16, 6, false, 1, 0, 1, 1]`（6 次）
- `[20, 2, 2, 879396988281791, "randomize", 15, 0, 16, 6, false, 1, 0, 1, 1]`（1 次）
- `[25, 2, 4, 1076614621331014, "randomize", 25, 0, 16, 6, true, 1, 0, 1, 1]`（1 次）
- `[20, 2.5, 3.1, 42, "fixed", 30, 0.18, 72, 6, false, 0.6, 0, 1, 0.6]`（1 次）
- `[20, 2, 2, 898536318458502, "randomize", 30, 0, 72, 6, false, 1, 0, 1, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
