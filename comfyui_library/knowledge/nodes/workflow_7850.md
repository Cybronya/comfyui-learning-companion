# workflow>自定义采样器

## 节点类型

`workflow>自定义采样器`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `模型:MODEL`（1 次）
- `正面条件:CONDITIONING`（1 次）
- `负面条件:CONDITIONING`（1 次）
- `Latent:LATENT`（1 次）
- `steps:INT`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `noise_seed:INT`（1 次）
- `sampler_name:COMBO`（1 次）
- `cfg:FLOAT`（1 次）

## 输出

- `输出:LATENT`（1 次）
- `降噪输出:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[4, 1024, 1024, 270198550524375, "randomize", "euler", 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
