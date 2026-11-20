# KSamplerSeq2

## 节点类型

`KSamplerSeq2`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `positive_seq:CONDITIONING`（1 次）
- `negative_seq:CONDITIONING`（1 次）
- `latent_image:LATENT`（1 次）
- `seed:INT`（1 次）
- `seed_mode_seq:COMBO`（1 次）
- `alternate_values:BOOLEAN`（1 次）
- `steps:INT`（1 次）
- `cfg:FLOAT`（1 次）
- `sampler_name:COMBO`（1 次）

## 输出

- `LATENT:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[871957653727950, "randomize", "increment", true, 20, 8, "euler", "simple", 0, 0, false, 0.5, false, "Blend", 0.5, 1, 0.`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
