# FSamplerAdvanced

## 节点类型

`FSamplerAdvanced`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（2 次）
- `positive:CONDITIONING`（2 次）
- `negative:CONDITIONING`（2 次）
- `latent_image:LATENT`（2 次）
- `seed:INT`（2 次）
- `steps:INT`（2 次）
- `cfg:FLOAT`（2 次）
- `scheduler:COMBO`（2 次）
- `sampler:COMBO`（2 次）
- `protect_first_steps:INT`（2 次）

## 输出

- `LATENT:LATENT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[920195792645317, "randomize", 25, 4, "beta57", "euler", 2, 1, "none", 0.999, "h2/s2", 4, 4, 0, 13, 0, "whitened", 1, tr`（1 次）
- `[1120395034021497, "randomize", 25, 4, "beta57", "euler", 2, 1, "none", 0.999, "h2/s2", 4, 4, 13, 25, 0, "whitened", 1, `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
