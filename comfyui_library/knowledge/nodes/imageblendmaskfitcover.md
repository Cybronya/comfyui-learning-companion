# ImageBlendMaskFitCover

## 节点类型

`ImageBlendMaskFitCover`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `background_image:IMAGE`（12 次）
- `layer_image:IMAGE`（12 次）
- `layer_mask:MASK`（12 次）
- `layer_alpha_mask:MASK`（12 次）
- `blend_mode:COMBO`（12 次）
- `rotation:FLOAT`（12 次）
- `opacity:INT`（12 次）
- `invert_mask:BOOLEAN`（12 次）
- `offset_x:INT`（12 次）
- `offset_y:INT`（12 次）

## 输出

- `image:IMAGE`（12 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["normal", 0, 100, false, 0, 0, 1]`（12 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
