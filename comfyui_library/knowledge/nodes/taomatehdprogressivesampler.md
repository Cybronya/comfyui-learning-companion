# TaoMateHDProgressiveSampler

## 节点类型

`TaoMateHDProgressiveSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 11 个 workflow 中。

## 输入

- `model:MODEL`（11 次）
- `positive:CONDITIONING`（11 次）
- `negative:CONDITIONING`（11 次）
- `latent:LATENT`（11 次）
- `seed:INT`（11 次）
- `steps:INT`（11 次）
- `cfg:FLOAT`（11 次）
- `low_scale:FLOAT`（11 次）
- `debug:BOOLEAN`（11 次）

## 输出

- `latent:LATENT`（11 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[666, "fixed", 3, 1, 0.625, false]`（10 次）
- `[868758485602455, "randomize", 3, 1, 0.625, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
