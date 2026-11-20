# TutuEquirectSourceComposite

## 节点类型

`TutuEquirectSourceComposite`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `generated:IMAGE`（2 次）
- `source_equirect:IMAGE`（2 次）
- `outpaint_mask:MASK`（2 次）
- `tone_match:FLOAT`（2 次）
- `feather_px:INT`（2 次）
- `tone_equalize:FLOAT`（2 次）
- `wrap_w:BOOLEAN`（2 次）

## 输出

- `composited:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, 12, 0.7, true]`（1 次）
- `[0, 12, 0, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
