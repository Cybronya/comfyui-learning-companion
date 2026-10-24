# LayerStyle: Stroke V2

## 节点类型

`LayerStyle: Stroke V2`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `background_image:IMAGE`（6 次）
- `layer_image:IMAGE`（6 次）
- `layer_mask:MASK`（6 次）
- `stroke_color:STRING`（5 次）
- `invert_mask:BOOLEAN`（2 次）
- `blend_mode:COMBO`（2 次）
- `opacity:INT`（2 次）
- `stroke_grow:INT`（2 次）
- `stroke_width:INT`（2 次）
- `blur:INT`（2 次）

## 输出

- `image:IMAGE`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, "normal", 100, 0, 8, 0, "#FF0000"]`（2 次）
- `[false, "normal", 80, 0, 4, 0, "#FF0000"]`（1 次）
- `[true, "normal", 100, -20, 15, 0, "#FF0000"]`（1 次）
- `[true, "normal", 100, 0, 15, 0, "#FF0000"]`（1 次）
- `[true, "normal", 100, -40, 15, 0, "#FF0000"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
