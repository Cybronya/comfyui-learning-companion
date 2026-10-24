# MegaStyleSampler

## 节点类型

`MegaStyleSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `pipe:MEGASTYLE_PIPE`（5 次）
- `conditioning:MEGASTYLE_COND`（5 次）
- `ref_latent:MEGASTYLE_LATENT`（5 次）
- `negative_conditioning:MEGASTYLE_COND`（5 次）
- `height:INT`（5 次）
- `width:INT`（5 次）
- `num_inference_steps:INT`（5 次）
- `embedded_guidance:FLOAT`（5 次）
- `seed:INT`（5 次）
- `sigma_shift:FLOAT`（5 次）

## 输出

- `latent:MEGASTYLE_LATENT`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[512, 512, 30, 3.5, 42, 3, 1, 1]`（2 次）
- `[512, 768, 30, 3.5, 42, 3, 1, 1]`（2 次）
- `[512, 512, 30, 3.5, 142903524, "randomize", 1.0000000000000002, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
