# workflow>MimicMotion Sampler

## 节点类型

`workflow>MimicMotion Sampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `mimic_pipeline:MIMICPIPE`（1 次）
- `ref_image:IMAGE`（1 次）
- `pose_images:IMAGE`（1 次）
- `MimicMotionDecode mimic_pipeline:MIMICPIPE`（1 次）

## 输出

- `images:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["EulerDiscreteScheduler", 0.002, 700, false, 25, 2, 2, 1091862197836670, "randomize", 15, 0, 16, 6, true, 1, 0, 1, 1, 4`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
