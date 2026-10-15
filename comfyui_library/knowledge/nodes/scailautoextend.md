# SCAILAutoExtend

## 节点类型

`SCAILAutoExtend`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `model:MODEL`（3 次）
- `positive:CONDITIONING`（3 次）
- `negative:CONDITIONING`（3 次）
- `vae:VAE`（3 次）
- `sampler:SAMPLER`（3 次）
- `sigmas:SIGMAS`（3 次）
- `pose_video:IMAGE`（3 次）
- `pose_video_mask:IMAGE`（3 次）
- `reference_image:IMAGE`（3 次）
- `reference_image_mask:IMAGE`（3 次）

## 输出

- `images:IMAGE`（3 次）
- `frame_count:INT`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[7424, 896, 8, "fixed", 1, 81, 5, "fixed", true, true, 1, 0, 1, true]`（1 次）
- `[7424, 896, 190813152747064, "randomize", 1, 81, 5, "increment", true, false, 1, 0, 1, true]`（1 次）
- `[896, 512, 850545140994409, "randomize", 1, 81, 5, "increment", true, true, 1, 0, 1, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
