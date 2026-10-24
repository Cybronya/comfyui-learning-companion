# workflow/批次大小

## 节点类型

`workflow/批次大小`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `CLIP视觉:CLIP_VISION`（1 次）
- `图像:IMAGE`（1 次）
- `遮罩:MASK`（1 次）
- `Latent:LATENT`（1 次）
- `条件:CONDITIONING`（1 次）
- `风格模型:STYLE_MODEL`（1 次）

## 输出

- `遮罩:MASK`（1 次）
- `反转遮罩:MASK`（1 次）
- `Latent:LATENT`（1 次）
- `条件:CONDITIONING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["center", 10, 0, true, false, 3, 1, 1, false, 3, 1, "multiply"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
