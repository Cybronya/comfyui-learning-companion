# WanAdvancedI2V

## 节点类型

`WanAdvancedI2V`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `positive:CONDITIONING`（1 次）
- `negative:CONDITIONING`（1 次）
- `vae:VAE`（1 次）
- `start_image:IMAGE`（1 次）
- `middle_image:IMAGE`（1 次）
- `end_image:IMAGE`（1 次）
- `motion_frames:IMAGE`（1 次）
- `clip_vision_start_image:CLIP_VISION_OUTPUT`（1 次）
- `clip_vision_middle_image:CLIP_VISION_OUTPUT`（1 次）
- `clip_vision_end_image:CLIP_VISION_OUTPUT`（1 次）

## 输出

- `positive_high:CONDITIONING`（1 次）
- `positive_low:CONDITIONING`（1 次）
- `negative:CONDITIONING`（1 次）
- `latent:LATENT`（1 次）
- `trim_latent:INT`（1 次）
- `trim_image:INT`（1 次）
- `next_offset:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[832, 480, 81, 1, "NORMAL", 0.5, 0, "AUTO_CONTINUE", 1, 0.5, 1, 0, 1, true, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
