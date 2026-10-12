# workflow/MimicMotion 

## 节点类型

`workflow/MimicMotion `

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `ref_image:IMAGE`（1 次）
- `pose_images:IMAGE`（1 次）
- `MimicMotionSampler ref_image:IMAGE`（1 次）
- `MimicMotionSampler pose_images:IMAGE`（1 次）
- `optional_scheduler:DIFFUSERS_SCHEDULER`（1 次）

## 输出

- `poses_with_ref:IMAGE`（1 次）
- `pose_images:IMAGE`（1 次）
- `images:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["MimicMotionMergedUnet_1-0-fp16.safetensors", "fp16", true, true, true, 20, 2, 2, 679953850442877, "randomize", 15, 0, `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
