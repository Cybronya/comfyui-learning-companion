# DyPE_KSampler

## 节点类型

`DyPE_KSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `model:MODEL`（5 次）
- `positive:CONDITIONING`（5 次）
- `seed:INT`（5 次）
- `steps:INT`（5 次）
- `cfg:FLOAT`（5 次）
- `offload:BOOLEAN`（5 次）
- `num_blocks_per_group:INT`（5 次）

## 输出

- `LATENT:LATENT`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[429828889, "randomize", 12, 1, true, 1]`（1 次）
- `[1462691419, "randomize", 20, 4.5, true, 1]`（1 次）
- `[124585767, "randomize", 18, 1, true, 1]`（1 次）
- `[1903603915, "randomize", 12, 1, true, 1]`（1 次）
- `[81738121, "randomize", 12, 1, true, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
