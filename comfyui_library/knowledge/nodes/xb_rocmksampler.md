# XB_ROCmKSampler

## 节点类型

`XB_ROCmKSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:MODEL`（2 次）
- `positive:CONDITIONING`（2 次）
- `negative:CONDITIONING`（2 次）
- `latent:LATENT`（2 次）
- `seed:INT`（2 次）
- `steps:INT`（2 次）
- `cfg:FLOAT`（2 次）
- `sampler:COMBO`（2 次）
- `scheduler:COMBO`（2 次）
- `denoise:FLOAT`（2 次）

## 输出

- `LATENT:LATENT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[573718484134302, "randomize", 4, 1, "euler", "simple", 1, "卸载显存模型"]`（1 次）
- `[1, "fixed", 4, 1, "euler", "simple", 1, "不做任何清理"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
