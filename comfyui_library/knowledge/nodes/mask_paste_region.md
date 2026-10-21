# Mask Paste Region

## 节点类型

`Mask Paste Region`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `mask:MASK`（6 次）
- `crop_mask:MASK`（6 次）
- `crop_data:CROP_DATA`（6 次）
- `crop_blending:FLOAT`（6 次）
- `crop_sharpening:INT`（6 次）

## 输出

- `RESULT_MASK:MASK`（6 次）
- `CROP_MASK:MASK`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 0]`（6 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
