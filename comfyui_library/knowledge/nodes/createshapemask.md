# CreateShapeMask

## 节点类型

`CreateShapeMask`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输出

- `mask:MASK`（3 次）
- `mask_inverted:MASK`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["square", 1, 0, 0, 0, 512, 512, 512, 512]`（1 次）
- `["square", 1, 0, 0, 0, 512, 512, 512, 1024]`（1 次）
- `["square", 1, 512, 0, 0, 512, 512, 512, 1024]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
