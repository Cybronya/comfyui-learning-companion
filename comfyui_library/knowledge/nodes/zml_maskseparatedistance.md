# ZML_MaskSeparateDistance

## 节点类型

`ZML_MaskSeparateDistance`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `输入遮罩:MASK`（2 次）
- `分离阈值:FLOAT`（2 次）
- `最小面积比例:FLOAT`（2 次）

## 输出

- `靠左遮罩:MASK`（2 次）
- `靠右遮罩:MASK`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.2, 0.01]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
