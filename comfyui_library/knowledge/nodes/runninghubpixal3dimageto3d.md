# RunningHubPixal3DImageTo3D

## 节点类型

`RunningHubPixal3DImageTo3D`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `pipe:PIXAL3D_PIPE`（1 次）
- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `seed:INT`（1 次）
- `resolution:COMBO`（1 次）
- `ss_guidance_strength:FLOAT`（1 次）
- `ss_guidance_rescale:FLOAT`（1 次）
- `ss_sampling_steps:INT`（1 次）
- `ss_rescale_t:FLOAT`（1 次）
- `shape_slat_guidance_strength:FLOAT`（1 次）

## 输出

- `asset:PIXAL3D_ASSET`（1 次）
- `camera_info:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[822524234, "randomize", "1024", 7.5, 0.7000000000000002, 12, 5, 7.5, 0.5000000000000001, 12, 3, 1, 0, 12, 3, 1.00000000`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
