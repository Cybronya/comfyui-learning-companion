# workflow>自动描边

## 节点类型

`workflow>自动描边`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `color:LYCOLOR`（6 次）
- `mode:COMBO`（6 次）
- `invert_mask:BOOLEAN`（6 次）
- `grow:INT`（6 次）
- `blur:INT`（6 次）
- `blend_mode:COMBO`（6 次）
- `opacity:INT`（6 次）
- `stroke_grow:INT`（6 次）
- `stroke_width:INT`（6 次）
- `LayerMask: MaskGrow invert_mask:BOOLEAN`（5 次）

## 输出

- `图像:IMAGE`（6 次）
- `裁剪框:BOX`（2 次）
- `裁剪框预览:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["#FFFFFF", "HEX", false, "normal", 100, 10, 20, 0, true, -20, 4]`（3 次）
- `["#FFFFFF", "HEX", false, "mask_area", 20, 20, 20, 20, "8", true, -20, 4, false, "normal", 100, 10, 30, 0]`（2 次）
- `["#FFFFFF", "HEX", true, -20, 4, false, "normal", 100, 10, 20, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
