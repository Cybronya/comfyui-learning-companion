# LucidFlux_SM_KSampler

## 节点类型

`LucidFlux_SM_KSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `model:LucidFlux_SM`（3 次）
- `vae:VAE`（3 次）
- `condition:CONDITIONING`（3 次）
- `steps:INT`（3 次）
- `seed:INT`（3 次）
- `cfg:FLOAT`（3 次）
- `wavelet:BOOLEAN`（2 次）

## 输出

- `Image:IMAGE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[8, 1347373957, "randomize", 4, true]`（1 次）
- `[8, 1964563175, "randomize", 4]`（1 次）
- `[8, 1368710850, "randomize", 4, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
