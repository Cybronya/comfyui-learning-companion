# KSamplerMod

## 节点类型

`KSamplerMod`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（3 次）
- `positive:CONDITIONING`（3 次）
- `negative:CONDITIONING`（3 次）
- `latent_image:LATENT`（3 次）
- `seed:INT`（3 次）

## 输出

- `LATENT:LATENT`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[409372558770606, "randomize", 32, 1, "euler", "simple", 1, "bf16"]`（1 次）
- `[999489505085576, "randomize", 32, 1, "euler", "simple", 1, "bf16"]`（1 次）
- `[896909223779965, "randomize", 32, 1, "euler", "simple", 1, "bf16"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
