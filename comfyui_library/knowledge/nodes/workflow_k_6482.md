# workflow>K采样器

## 节点类型

`workflow>K采样器`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `模型:MODEL`（1 次）
- `条件:CONDITIONING`（1 次）
- `BasicGuider model:MODEL`（1 次）

## 输出

- `采样器:SAMPLER`（1 次）
- `噪波生成:NOISE`（1 次）
- `Sigmas:SIGMAS`（1 次）
- `Latent:LATENT`（1 次）
- `条件:CONDITIONING`（1 次）
- `引导:GUIDER`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["euler", 887507588705528, "randomize", "simple", 8, 1, 1024, 1024, 1, 3.5]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
