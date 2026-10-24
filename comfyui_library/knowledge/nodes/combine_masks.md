# Combine Masks

## 节点类型

`Combine Masks`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image1:IMAGE`（3 次）
- `image2:IMAGE`（3 次）
- `op:COMBO`（3 次）
- `clamp_result:COMBO`（3 次）
- `round_result:COMBO`（3 次）

## 输出

- `IMAGE:IMAGE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["difference", "yes", "no"]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
