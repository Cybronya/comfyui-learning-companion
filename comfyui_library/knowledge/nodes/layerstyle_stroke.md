# LayerStyle: Stroke

## 节点类型

`LayerStyle: Stroke`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `background_image:IMAGE`（2 次）
- `layer_image:IMAGE`（2 次）
- `layer_mask:MASK`（2 次）
- `invert_mask:BOOLEAN`（1 次）
- `blend_mode:COMBO`（1 次）
- `opacity:INT`（1 次）
- `stroke_grow:INT`（1 次）
- `stroke_width:INT`（1 次）
- `blur:INT`（1 次）
- `stroke_color:STRING`（1 次）

## 输出

- `image:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[false, "normal", 100, 13, 25, 0, "#FFFFFF"]`（1 次）
- `[true, "normal", 100, 0, 8, 0, "#FF0088"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
