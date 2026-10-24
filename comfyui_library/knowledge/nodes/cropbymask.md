# CropByMask

## 节点类型

`CropByMask`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `image:IMAGE`（6 次）
- `mask:MASK`（6 次）
- `padding:INT`（6 次）

## 输出

- `image:IMAGE`（6 次）
- `mask:MASK`（6 次）
- `crop_x:INT`（6 次）
- `crop_y:INT`（6 次）
- `original_width:INT`（6 次）
- `original_height:INT`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[96]`（2 次）
- `[200]`（2 次）
- `[120]`（1 次）
- `[128]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
