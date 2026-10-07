# LayerUtility: Collage

## 节点类型

`LayerUtility: Collage`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `images:IMAGE`（1 次）
- `florence2_model:FLORENCE2`（1 次）
- `canvas_width:INT`（1 次）
- `canvas_height:INT`（1 次）
- `border_width:FLOAT`（1 次）
- `rounded_rect_radius:INT`（1 次）
- `uniformity:FLOAT`（1 次）
- `background_color:STRING`（1 次）
- `seed:INT`（1 次）
- `object_prompt:STRING`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[2048, 2048, 1, 20, 1, "#000000", 189033467128577, "randomize", "subject"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
