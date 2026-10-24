# FitDiTTryOn

## 节点类型

`FitDiTTryOn`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `model:FITDIT_MODEL`（5 次）
- `vton_image:IMAGE`（5 次）
- `garm_image:IMAGE`（5 次）
- `mask:IMAGE`（5 次）
- `pose_image:IMAGE`（5 次）

## 输出

- `result:IMAGE`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[20, 2, 1129, "randomize", 1, "768x1024"]`（1 次）
- `[20, 2, 1060, "randomize", 1, "1152x1536"]`（1 次）
- `[20, 2, 121, "fixed", 1, "768x1024"]`（1 次）
- `[20, 2, 376, "randomize", 1, "768x1024"]`（1 次）
- `[20, 2, 1236, "randomize", 1, "768x1024"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
