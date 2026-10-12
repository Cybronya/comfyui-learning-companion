# RunningHub_TurboDiffusion_TurboWan_Sampler

## 节点类型

`RunningHub_TurboDiffusion_TurboWan_Sampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `pipeline:RH_TurboWan_Pipeline`（1 次）
- `ref_image:IMAGE`（1 次）
- `prompt:STRING`（1 次）
- `num_frames:INT`（1 次）
- `aspect_ratio_mode:COMBO`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `seed:INT`（1 次）
- `steps:INT`（1 次）

## 输出

- `images:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["a beautiful woman", 77, "custom", 480, 640, 12629657421572, "randomize", 4]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
