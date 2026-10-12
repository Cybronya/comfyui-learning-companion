# workflow/MimicMotion Sampler核心

## 节点类型

`workflow/MimicMotion Sampler核心`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `ref_image:IMAGE`（1 次）
- `pose_images:IMAGE`（1 次）

## 输出

- `scheduler:DIFFUSERS_SCHEDULER`（1 次）
- `images:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["MimicMotionMergedUnet_1-0-fp16.safetensors", "fp16", "EulerDiscreteScheduler", 0.002, 700, false, "EulerDiscreteSchedu`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
