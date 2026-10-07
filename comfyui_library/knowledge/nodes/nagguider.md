# NAGGuider

## 节点类型

`NAGGuider`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `conditioning:CONDITIONING`（1 次）
- `nag_negative:CONDITIONING`（1 次）
- `latent_image:LATENT`（1 次）
- `nag_scale:FLOAT`（1 次）
- `nag_tau:FLOAT`（1 次）
- `nag_alpha:FLOAT`（1 次）
- `nag_sigma_end:FLOAT`（1 次）

## 输出

- `GUIDER:GUIDER`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[5, 2.5, 0.25, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
