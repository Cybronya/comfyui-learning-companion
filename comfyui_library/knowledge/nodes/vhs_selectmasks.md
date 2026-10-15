# VHS_SelectMasks

## 节点类型

`VHS_SelectMasks`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `mask:MASK`（5 次）
- `indexes:STRING`（5 次）
- `err_if_missing:BOOLEAN`（5 次）
- `err_if_empty:BOOLEAN`（5 次）

## 输出

- `MASK:MASK`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `{"err_if_empty": true, "err_if_missing": true, "indexes": "0"}`（3 次）
- `{"err_if_empty": true, "err_if_missing": true, "indexes": "-1"}`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
