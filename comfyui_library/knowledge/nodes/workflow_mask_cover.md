# workflow>mask cover

## 节点类型

`workflow>mask cover`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `遮罩:MASK`（4 次）
- `invert_mask:BOOLEAN`（4 次）
- `grow:INT`（4 次）
- `blur:INT`（4 次）
- `threshold:INT`（4 次）
- `block_size:INT`（4 次）
- `device:COMBO`（4 次）

## 输出

- `mask:MASK`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[false, 0, 0, 20, 24, "cpu"]`（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
