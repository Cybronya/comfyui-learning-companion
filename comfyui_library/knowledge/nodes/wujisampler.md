# WujiSampler

## 节点类型

`WujiSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `模型:MODEL`（1 次）
- `正向条件:CONDITIONING`（1 次）
- `负向条件:CONDITIONING`（1 次）
- `潜空间图像:LATENT`（1 次）
- `VAE:VAE`（1 次）
- `添加噪波:COMBO`（1 次）
- `种子:INT`（1 次）
- `步数:INT`（1 次）
- `CFG:FLOAT`（1 次）
- `采样器:COMBO`（1 次）

## 输出

- `潜空间:LATENT`（1 次）
- `图像:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["enable", 878491901328209, "randomize", 8, 1, "euler", "simple", 0, 10000, "disable", 1, "普通解码"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
