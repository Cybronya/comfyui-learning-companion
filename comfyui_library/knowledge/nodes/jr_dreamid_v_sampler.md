# JR_DreamID-V_Sampler

## 节点类型

`JR_DreamID-V_Sampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `pipeline:RH_DreamID-V_Pipeline`（1 次）
- `video:VIDEO`（1 次）
- `ref_image:IMAGE`（1 次）
- `size:COMBO`（1 次）
- `frame_num:INT`（1 次）
- `sample_steps:INT`（1 次）
- `fps:INT`（1 次）
- `seed:INT`（1 次）
- `pose_backend:COMBO`（1 次）
- `dwpose_fallback:BOOLEAN`（1 次）

## 输出

- `frames:IMAGE`（1 次）
- `video:VIDEO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["832*480", 81, 20, 24, 11916412040942, "randomize", "dwpose", 480, 832, 480]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
