# ZML_MaskCropNode

## 节点类型

`ZML_MaskCropNode`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `图像:IMAGE`（3 次）
- `遮罩:MASK`（3 次）
- `遮罩缩放系数:FLOAT`（3 次）
- `保持原始分辨率:BOOLEAN`（3 次）

## 输出

- `裁剪图像:IMAGE`（3 次）
- `反转裁剪:IMAGE`（3 次）
- `反转遮罩:MASK`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, true]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
