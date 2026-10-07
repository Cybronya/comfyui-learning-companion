# NAGCFGGuider

## 节点类型

`NAGCFGGuider`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（6 次）
- `positive:CONDITIONING`（6 次）
- `negative:CONDITIONING`（6 次）
- `nag_negative:CONDITIONING`（6 次）
- `latent_image:LATENT`（6 次）

## 输出

- `GUIDER:GUIDER`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, 5, 2.5, 0.25, 0.75]`（2 次）
- `[1, 1, 2.5, 0.25, 0]`（2 次）
- `[4, 5, 2.5, 0.25, 0.75]`（1 次）
- `[4, 1, 2.5, 0.25, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
