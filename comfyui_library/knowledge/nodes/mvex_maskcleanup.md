# MVEx_MaskCleanup

## 节点类型

`MVEx_MaskCleanup`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 8 个 workflow 中。

## 输入

- `masks:MASK`（8 次）
- `threshold:FLOAT`（8 次）
- `method:COMFY_DYNAMICCOMBO_V3`（8 次）
- `method.shrink:INT`（8 次）
- `method.min_frames:INT`（8 次）
- `edge_grow:INT`（8 次）

## 输出

- `masks:MASK`（8 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.3, "shrink_grow", 12, 4, 16]`（8 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
