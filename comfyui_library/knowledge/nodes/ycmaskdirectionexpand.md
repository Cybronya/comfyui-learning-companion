# YCMaskDirectionExpand

## 节点类型

`YCMaskDirectionExpand`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 8 个 workflow 中。

## 输入

- `mask:MASK`（32 次）
- `top:INT`（32 次）
- `bottom:INT`（32 次）
- `left:INT`（32 次）
- `right:INT`（32 次）

## 输出

- `mask:MASK`（32 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[800, 80, 80, 80]`（16 次）
- `[800, 250, 250, 250]`（16 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
